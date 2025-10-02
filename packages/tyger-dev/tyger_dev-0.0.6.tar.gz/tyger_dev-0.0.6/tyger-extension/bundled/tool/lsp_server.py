# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Implementation of tool support over LSP."""
from __future__ import annotations

import copy
import json
import os
import pathlib
import re
import sys
import threading
import time
import traceback
from typing import Any, Dict, Optional, Sequence, List


# **********************************************************
# Update sys.path before importing any bundled libraries.
# **********************************************************
def update_sys_path(path_to_add: str, strategy: str) -> None:
    """Add given path to `sys.path`."""
    if path_to_add not in sys.path and os.path.isdir(path_to_add):
        if strategy == "useBundled":
            sys.path.insert(0, path_to_add)
        elif strategy == "fromEnvironment":
            sys.path.append(path_to_add)


# Ensure that we can import LSP libraries, and other bundled libraries.
update_sys_path(
    os.fspath(pathlib.Path(__file__).parent.parent / "libs"),
    os.getenv("LS_IMPORT_STRATEGY", "useBundled"),
)

# **********************************************************
# Imports needed for the language server goes below this.
# **********************************************************
# pylint: disable=wrong-import-position,import-error
import lsp_jsonrpc as jsonrpc
import lsp_utils as utils
import lsprotocol.types as lsp
from pygls import server, uris, workspace

WORKSPACE_SETTINGS = {}
GLOBAL_SETTINGS = {}
RUNNER = pathlib.Path(__file__).parent / "lsp_runner.py"

MAX_WORKERS = 5
LSP_SERVER = server.LanguageServer(
    name="Tyger", version="0.0.1", max_workers=MAX_WORKERS
)

# Debounce tracker of timers for each document
PENDING_LINT_TASKS: Dict[str, threading.Timer] = {}

# **********************************************************
# Tool specific code goes below this.
# **********************************************************

TOOL_MODULE = "tyger"
TOOL_DISPLAY = "Tyger"
TOOL_ARGS = ["--json"]  # default arguments always passed to your tool.


# **********************************************************
# Linting features start here
# **********************************************************

#  See `pylint` implementation for a full featured linter extension:
#  Pylint: https://github.com/microsoft/vscode-pylint/blob/main/bundled/tool


@LSP_SERVER.feature(lsp.TEXT_DOCUMENT_DID_OPEN)
def did_open(params: lsp.DidOpenTextDocumentParams) -> None:
    """LSP handler for textDocument/didOpen request."""
    document = LSP_SERVER.workspace.get_text_document(params.text_document.uri)
    diagnostics: list[lsp.Diagnostic] = _linting_helper(document)
    LSP_SERVER.publish_diagnostics(document.uri, diagnostics)


@LSP_SERVER.feature(lsp.TEXT_DOCUMENT_DID_CHANGE)
def did_change(params: lsp.DidChangeTextDocumentParams) -> None:
    """LSP handler for textDocument/didChange request."""
    document = LSP_SERVER.workspace.get_text_document(params.text_document.uri)
    _schedule_debounced_lint(document)


def _schedule_debounced_lint(document: workspace.Document) -> None:
    """Schedule a debounced lint task for the document.

    This ensures that we don't run the linter on every keystroke, but rather
    wait until the user has stopped typing for a short period.

    Args:
        document: The document to lint
    """
    if os.getenv("DISABLE_LINTING_DEBOUNCE", "false").lower() == "true":
        # If debounce is disabled, run lint immediately
        _perform_lint(document)
        return

    # Cancel any pending lint for this document
    uri = document.uri
    if uri in PENDING_LINT_TASKS:
        PENDING_LINT_TASKS[uri].cancel()

    settings = copy.deepcopy(_get_settings_by_document(document))
    delay_seconds = settings.get("lintingDelay", 500) / 1000  # To seconds

    # Create a new timer for this document
    timer = threading.Timer(
        delay_seconds,
        _perform_lint,
        args=[document],
    )
    PENDING_LINT_TASKS[uri] = timer
    timer.start()


def _perform_lint(document: workspace.Document) -> None:
    """Execute the linting process for a document.

    This is called after the debounce delay.

    Args:
        document: The document to lint
    """
    # Remove this task from pending tasks
    if document.uri in PENDING_LINT_TASKS:
        del PENDING_LINT_TASKS[document.uri]

    diagnostics: list[lsp.Diagnostic] = _linting_helper(document)
    LSP_SERVER.publish_diagnostics(document.uri, diagnostics)


@LSP_SERVER.feature(lsp.TEXT_DOCUMENT_DID_SAVE)
def did_save(params: lsp.DidSaveTextDocumentParams) -> None:
    """LSP handler for textDocument/didSave request."""
    document = LSP_SERVER.workspace.get_text_document(params.text_document.uri)
    diagnostics: list[lsp.Diagnostic] = _linting_helper(document)
    LSP_SERVER.publish_diagnostics(document.uri, diagnostics)


@LSP_SERVER.feature(lsp.TEXT_DOCUMENT_DID_CLOSE)
def did_close(params: lsp.DidCloseTextDocumentParams) -> None:
    """LSP handler for textDocument/didClose request."""
    document = LSP_SERVER.workspace.get_text_document(params.text_document.uri)
    # Publishing empty diagnostics to clear the entries for this file.
    LSP_SERVER.publish_diagnostics(document.uri, [])


def _linting_helper(document: workspace.Document) -> list[lsp.Diagnostic]:
    """Run Tyger on a document and return diagnostics.

    Args:
        document: The document to lint

    Returns:
        A list of LSP diagnostic objects
    """
    try:
        # Tyger supports passing file content via stdin with --stdin flag
        # This allows us to lint on change
        result = _run_tool_on_document(document, use_stdin=True)
        if not result:
            return []

        settings = copy.deepcopy(_get_settings_by_document(document))
        return (
            _parse_tyger_json_output(result.stdout, severity=settings["severity"])
            if result.stdout
            else []
        )
    except Exception:  # pylint: disable=broad-except
        LSP_SERVER.show_message_log(
            f"Tyger failed with error:\r\n{traceback.format_exc()}",
            lsp.MessageType.Error,
        )
        return []


def _parse_tyger_json_output(
    content: str, severity: Dict[str, str]
) -> list[lsp.Diagnostic]:
    """Parse the JSON output from Tyger and convert to LSP diagnostics.

    Args:
        content: The JSON output from Tyger
        severity: A mapping of Tyger message types to LSP diagnostic severities

    Returns:
        A list of LSP diagnostic objects
    """
    diagnostics: list[lsp.Diagnostic] = []

    try:
        if not content or not content.strip():
            log_warning("Tyger output is empty")
            return diagnostics

        json_data = json.loads(content)
        if not json_data or "results" not in json_data:
            log_to_output("Tyger output missing 'results' field")
            return diagnostics

        for result in json_data["results"]:
            if "diagnostics" not in result:
                continue

            for data in result["diagnostics"]:
                start = lsp.Position(
                    line=data.get("lineno", 1) - 1,  # LSP is 0-based
                    character=data.get("col_offset", 0),
                )
                end = lsp.Position(
                    line=data.get("end_lineno", start.line + 1) - 1,
                    character=data.get("end_col_offset", start.character),
                )

                diagnostic = lsp.Diagnostic(
                    range=lsp.Range(start=start, end=end),
                    message=data.get("message"),
                    severity=_get_severity(data.get("severity"), severity),
                    code=f"{data.get('message-id')}:{data.get('symbol')}",
                    source=TOOL_DISPLAY,
                )
                diagnostics.append(diagnostic)

    except json.JSONDecodeError:
        log_error(f"Failed to parse Tyger JSON output: {content}")

    return diagnostics


# Follow the flow of severity from the settings in package.json to the server.
def _get_severity(error_type: str, severity: Dict[str, str]) -> lsp.DiagnosticSeverity:
    """Determine the severity of a Tyger diagnostic.

    Args:
        error_type: The type of error reported by Tyger
        severity: Dictionary mapping from Tyger error types to VS Code severity levels

    Returns:
        The LSP diagnostic severity
    """
    value = severity.get(error_type, "Error")

    try:
        return lsp.DiagnosticSeverity[value]
    except KeyError:
        pass

    return lsp.DiagnosticSeverity.Error


# **********************************************************
# Linting features end here
# **********************************************************


# **********************************************************
# Required Language Server Initialization and Exit handlers.
# **********************************************************
@LSP_SERVER.feature(lsp.INITIALIZE)
def initialize(params: lsp.InitializeParams) -> None:
    """LSP handler for initialize request."""
    log_to_output(f"CWD Server: {os.getcwd()}")

    paths = "\r\n   ".join(sys.path)
    log_to_output(f"sys.path used to run Server:\r\n   {paths}")

    GLOBAL_SETTINGS.update(**params.initialization_options.get("globalSettings", {}))

    settings = params.initialization_options["settings"]
    _update_workspace_settings(settings)
    log_to_output(
        f"Settings used to run Server:\r\n{json.dumps(settings, indent=4, ensure_ascii=False)}\r\n"
    )
    log_to_output(
        f"Global settings:\r\n{json.dumps(GLOBAL_SETTINGS, indent=4, ensure_ascii=False)}\r\n"
    )


@LSP_SERVER.feature(lsp.EXIT)
def on_exit(_params: Optional[Any] = None) -> None:
    """Handle clean up on exit."""
    for timer in PENDING_LINT_TASKS.values():
        timer.cancel()
    PENDING_LINT_TASKS.clear()

    jsonrpc.shutdown_json_rpc()


@LSP_SERVER.feature(lsp.SHUTDOWN)
def on_shutdown(_params: Optional[Any] = None) -> None:
    """Handle clean up on shutdown."""
    for timer in PENDING_LINT_TASKS.values():
        timer.cancel()
    PENDING_LINT_TASKS.clear()

    jsonrpc.shutdown_json_rpc()


def _get_global_defaults():
    return {
        "path": GLOBAL_SETTINGS.get("path", []),
        "interpreter": GLOBAL_SETTINGS.get("interpreter", [sys.executable]),
        "args": GLOBAL_SETTINGS.get("args", []),
        "severity": GLOBAL_SETTINGS.get(
            "severity",
            {
                "error": "Error",
                "warning": "Warning",
                "info": "Information",
                "hint": "Hint",
            },
        ),
        "importStrategy": GLOBAL_SETTINGS.get("importStrategy", "useBundled"),
        "showNotifications": GLOBAL_SETTINGS.get("showNotifications", "off"),
        "lintingDelay": GLOBAL_SETTINGS.get("lintingDelay", 500),
    }


def _update_workspace_settings(settings):
    if not settings:
        key = os.getcwd()
        WORKSPACE_SETTINGS[key] = {
            "cwd": key,
            "workspaceFS": key,
            "workspace": uris.from_fs_path(key),
            **_get_global_defaults(),
        }
        return

    for setting in settings:
        key = uris.to_fs_path(setting["workspace"])
        WORKSPACE_SETTINGS[key] = {
            "cwd": key,
            **setting,
            "workspaceFS": key,
        }


def _get_settings_by_path(file_path: pathlib.Path):
    workspaces = {s["workspaceFS"] for s in WORKSPACE_SETTINGS.values()}

    while file_path != file_path.parent:
        str_file_path = str(file_path)
        if str_file_path in workspaces:
            return WORKSPACE_SETTINGS[str_file_path]
        file_path = file_path.parent

    setting_values = list(WORKSPACE_SETTINGS.values())
    return setting_values[0]


def _get_document_key(document: workspace.Document):
    if WORKSPACE_SETTINGS:
        document_workspace = pathlib.Path(document.path)
        workspaces = {s["workspaceFS"] for s in WORKSPACE_SETTINGS.values()}

        # Find workspace settings for the given file.
        while document_workspace != document_workspace.parent:
            if str(document_workspace) in workspaces:
                return str(document_workspace)
            document_workspace = document_workspace.parent

    return None


def _get_settings_by_document(document: workspace.Document | None):
    if document is None or document.path is None:
        return list(WORKSPACE_SETTINGS.values())[0]

    key = _get_document_key(document)
    if key is None:
        # This is either a non-workspace file or there is no workspace.
        key = os.fspath(pathlib.Path(document.path).parent)
        return {
            "cwd": key,
            "workspaceFS": key,
            "workspace": uris.from_fs_path(key),
            **_get_global_defaults(),
        }

    return WORKSPACE_SETTINGS[str(key)]


# *****************************************************
# Internal execution APIs.
# *****************************************************
def _run_tool_on_document(
    document: workspace.Document,
    use_stdin: bool = False,
    extra_args: Optional[Sequence[str]] = None,
) -> utils.RunResult | None:
    """Runs tool on the given document.

    if use_stdin is true then contents of the document is passed to the
    tool via stdin.
    """
    if extra_args is None:
        extra_args = []

    if str(document.uri).startswith("vscode-notebook-cell"):
        log_warning(
            f"Skipping linting for notebook cell [Not Supported]: {str(document.uri)}"
        )
        return None

    if utils.is_stdlib_file(document.path):
        log_warning(
            f"Skipping linting for standard library file [stdlib excluded]: {document.path}"
        )
        return None

    # deep copy here to prevent accidentally updating global settings.
    settings = copy.deepcopy(_get_settings_by_document(document))

    code_workspace = settings["workspaceFS"]
    cwd = settings["cwd"]

    use_path = False
    use_rpc = False
    if settings["path"]:
        # 'path' setting takes priority over everything.
        use_path = True
        argv = settings["path"]
    elif settings["interpreter"] and not utils.is_current_interpreter(
        settings["interpreter"][0]
    ):
        # If there is a different interpreter set use JSON-RPC to the subprocess
        # running under that interpreter.
        argv = [TOOL_MODULE]
        use_rpc = True
    else:
        # if the interpreter is same as the interpreter running this
        # process then run as module.
        argv = [TOOL_MODULE]

    argv += TOOL_ARGS + settings["args"] + extra_args

    resolved_path = str(pathlib.Path(document.path).resolve())

    if use_stdin:
        argv += ["--stdin", resolved_path]
    else:
        argv += [resolved_path]

    if use_path:
        # This mode is used when running executables.
        log_to_output(" ".join(argv))
        log_to_output(f"CWD Server: {cwd}")
        result = utils.run_path(
            argv=argv,
            use_stdin=use_stdin,
            cwd=cwd,
            source=document.source.replace("\r\n", "\n"),
        )
        if result.stderr:
            log_to_output(result.stderr)
    elif use_rpc:
        # This mode is used if the interpreter running this server is different from
        # the interpreter used for running this server.
        log_to_output(" ".join(settings["interpreter"] + ["-m"] + argv))
        log_to_output(f"CWD Linter: {cwd}")

        result = jsonrpc.run_over_json_rpc(
            workspace=code_workspace,
            interpreter=settings["interpreter"],
            module=TOOL_MODULE,
            argv=argv,
            use_stdin=use_stdin,
            cwd=cwd,
            source=document.source,
        )
        if result.exception:
            log_error(result.exception)
            result = utils.RunResult(result.stdout, result.stderr)
        elif result.stderr:
            log_to_output(result.stderr)
    else:
        # In this mode the tool is run as a module in the same process as the language server.
        log_to_output(" ".join([sys.executable, "-m"] + argv))
        log_to_output(f"CWD Linter: {cwd}")
        # This is needed to preserve sys.path, in cases where the tool modifies
        # sys.path and that might not work for this scenario next time around.
        with utils.substitute_attr(sys, "path", sys.path[:]):
            try:
                result = utils.run_module(
                    module=TOOL_MODULE,
                    argv=argv,
                    use_stdin=use_stdin,
                    cwd=cwd,
                    source=document.source,
                )
            except Exception:
                log_error(traceback.format_exc(chain=True))
                raise
        if result.stderr:
            log_to_output(result.stderr)

    log_to_output(f"{document.uri} :\r\n{result.stdout}")
    return result


def _run_tool(extra_args: Sequence[str]) -> utils.RunResult:
    """Runs tool."""
    # deep copy here to prevent accidentally updating global settings.
    settings = copy.deepcopy(_get_settings_by_document(None))

    code_workspace = settings["workspaceFS"]
    cwd = settings["workspaceFS"]

    use_path = False
    use_rpc = False
    if len(settings["path"]) > 0:
        # 'path' setting takes priority over everything.
        use_path = True
        argv = settings["path"]
    elif len(settings["interpreter"]) > 0 and not utils.is_current_interpreter(
        settings["interpreter"][0]
    ):
        # If there is a different interpreter set use JSON-RPC to the subprocess
        # running under that interpreter.
        argv = [TOOL_MODULE]
        use_rpc = True
    else:
        # if the interpreter is same as the interpreter running this
        # process then run as module.
        argv = [TOOL_MODULE]

    argv += TOOL_ARGS + extra_args

    # For Tyger, we include --stdin flag when needed
    if "--stdin" not in argv:
        argv.append("--stdin")

    if use_path:
        # This mode is used when running executables.
        log_to_output(" ".join(argv))
        log_to_output(f"CWD Server: {cwd}")
        result = utils.run_path(argv=argv, use_stdin=True, cwd=cwd)
        if result.stderr:
            log_to_output(result.stderr)
    elif use_rpc:
        # This mode is used if the interpreter running this server is different from
        # the interpreter used for running this server.
        log_to_output(" ".join(settings["interpreter"] + ["-m"] + argv))
        log_to_output(f"CWD Linter: {cwd}")
        result = jsonrpc.run_over_json_rpc(
            workspace=code_workspace,
            interpreter=settings["interpreter"],
            module=TOOL_MODULE,
            argv=argv,
            use_stdin=True,
            cwd=cwd,
        )
        if result.exception:
            log_error(result.exception)
            result = utils.RunResult(result.stdout, result.stderr)
        elif result.stderr:
            log_to_output(result.stderr)
    else:
        # In this mode the tool is run as a module in the same process as the language server.
        log_to_output(" ".join([sys.executable, "-m"] + argv))
        log_to_output(f"CWD Linter: {cwd}")
        # This is needed to preserve sys.path, in cases where the tool modifies
        # sys.path and that might not work for this scenario next time around.
        with utils.substitute_attr(sys, "path", sys.path[:]):
            try:
                result = utils.run_module(
                    module=TOOL_MODULE, argv=argv, use_stdin=True, cwd=cwd
                )
            except Exception:
                log_error(traceback.format_exc(chain=True))
                raise
        if result.stderr:
            log_to_output(result.stderr)

    log_to_output(f"\r\n{result.stdout}\r\n")
    return result


# *****************************************************
# Logging and notification.
# *****************************************************
def log_to_output(
    message: str, msg_type: lsp.MessageType = lsp.MessageType.Log
) -> None:
    """Log message to output channel."""
    LSP_SERVER.show_message_log(message, msg_type)


def log_error(message: str) -> None:
    """Log error message to output channel."""
    LSP_SERVER.show_message_log(message, lsp.MessageType.Error)
    if os.getenv("LS_SHOW_NOTIFICATION", "off") in ["onError", "onWarning", "always"]:
        LSP_SERVER.show_message(message, lsp.MessageType.Error)


def log_warning(message: str) -> None:
    """Log warning message to output channel."""
    LSP_SERVER.show_message_log(message, lsp.MessageType.Warning)
    if os.getenv("LS_SHOW_NOTIFICATION", "off") in ["onWarning", "always"]:
        LSP_SERVER.show_message(message, lsp.MessageType.Warning)


def log_always(message: str) -> None:
    """Log message to output channel."""
    LSP_SERVER.show_message_log(message, lsp.MessageType.Info)
    if os.getenv("LS_SHOW_NOTIFICATION", "off") in ["always"]:
        LSP_SERVER.show_message(message, lsp.MessageType.Info)


# *****************************************************
# Start the server.
# *****************************************************
if __name__ == "__main__":
    LSP_SERVER.start_io()
