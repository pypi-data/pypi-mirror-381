"""
Test for linting over LSP.
"""

from threading import Event
import os
import tempfile
from pathlib import Path

from hamcrest import assert_that, is_, greater_than

from .lsp_test_client import constants, defaults, session, utils

TEST_FILE_PATH = constants.TEST_DATA / "tyger_sample" / "sample.py"
TEST_FILE2_PATH = constants.TEST_DATA / "tyger_sample" / "sample2.py"
TEST_FILE_URI = utils.as_uri(str(TEST_FILE_PATH))
TEST_FILE2_URI = utils.as_uri(str(TEST_FILE2_PATH))
SERVER_INFO = utils.get_server_info_defaults()
LINTER = utils.get_server_info_defaults()
TIMEOUT = 10  # 10 seconds


class Severity:
    ERROR = 1
    WARNING = 2
    INFORMATION = 3
    HINT = 4


def test_publish_diagnostics_on_open():
    """test that linting is done on file open."""
    contents = TEST_FILE_PATH.read_text(encoding="utf-8")
    actual = []
    os.environ["DISABLE_LINTING_DEBOUNCE"] = "true"
    with session.LspSession() as ls_session:
        ls_session.initialize(defaults.VSCODE_DEFAULT_INITIALIZE)

        done = Event()

        def _handler(params):
            nonlocal actual
            actual = params
            done.set()

        ls_session.set_notification_callback(session.PUBLISH_DIAGNOSTICS, _handler)

        ls_session.notify_did_open(
            {
                "textDocument": {
                    "uri": TEST_FILE_URI,
                    "languageId": "python",
                    "version": 1,
                    "text": contents,
                }
            }
        )

        # wait for some time to receive all notifications
        done.wait(TIMEOUT)

    expected = {
        "uri": TEST_FILE_URI,
        "diagnostics": [
            {
                "range": {
                    "start": {"line": 1, "character": 0},
                    "end": {"line": 1, "character": 10},
                },
                "severity": Severity.WARNING,
                "code": "TYG903:redefine-variable-warning",
                "message": "Variable 'x' already defined",
                "source": LINTER["name"],
            }
        ],
    }

    assert_that(actual, is_(expected))


def test_publish_diagnostics_on_save():
    """test that linting is done on file save."""
    contents = TEST_FILE_PATH.read_text(encoding="utf-8")
    actual = []
    with session.LspSession() as ls_session:
        ls_session.initialize(defaults.VSCODE_DEFAULT_INITIALIZE)

        done = Event()

        def _handler(params):
            nonlocal actual
            actual = params
            done.set()

        ls_session.set_notification_callback(session.PUBLISH_DIAGNOSTICS, _handler)

        ls_session.notify_did_open(
            {
                "textDocument": {
                    "uri": TEST_FILE_URI,
                    "languageId": "python",
                    "version": 1,
                    "text": contents,
                }
            }
        )

        ls_session.notify_did_save(
            {
                "textDocument": {
                    "uri": TEST_FILE_URI,
                    "version": 1,
                }
            }
        )

        # wait for some time to receive all notifications
        done.wait(TIMEOUT)

    expected = {
        "uri": TEST_FILE_URI,
        "diagnostics": [
            {
                "range": {
                    "start": {"line": 1, "character": 0},
                    "end": {"line": 1, "character": 10},
                },
                "severity": Severity.WARNING,
                "code": "TYG903:redefine-variable-warning",
                "message": "Variable 'x' already defined",
                "source": LINTER["name"],
            }
        ],
    }

    assert_that(actual, is_(expected))


def test_publish_diagnostics_on_close():
    """test that linting is done on file close."""
    contents = TEST_FILE_PATH.read_text(encoding="utf-8")
    actual = []
    with session.LspSession() as ls_session:
        ls_session.initialize(defaults.VSCODE_DEFAULT_INITIALIZE)

        done = Event()

        def _handler(params):
            nonlocal actual
            actual = params
            done.set()

        ls_session.set_notification_callback(session.PUBLISH_DIAGNOSTICS, _handler)

        ls_session.notify_did_open(
            {
                "textDocument": {
                    "uri": TEST_FILE_URI,
                    "languageId": "python",
                    "version": 1,
                    "text": contents,
                }
            }
        )

        done.wait(TIMEOUT)

        # Should receive at least one diagnostic
        assert_that(len(actual), is_(greater_than(0)))

        done.clear()

        ls_session.notify_did_close(
            {
                "textDocument": {
                    "uri": TEST_FILE_URI,
                    "languageId": "python",
                    "version": 1,
                }
            }
        )

        # wait for some time to receive all notifications
        done.wait(TIMEOUT)

    expected = {
        "uri": TEST_FILE_URI,
        "diagnostics": [],
    }

    assert_that(actual, is_(expected))


def test_publish_diagnostics_on_change():
    """test that linting is done on file change."""
    contents = TEST_FILE2_PATH.read_text(encoding="utf-8")
    actual = []
    with session.LspSession() as ls_session:
        ls_session.initialize(defaults.VSCODE_DEFAULT_INITIALIZE)

        done = Event()

        def _handler(params):
            nonlocal actual
            actual = params
            done.set()

        ls_session.set_notification_callback(session.PUBLISH_DIAGNOSTICS, _handler)

        ls_session.notify_did_open(
            {
                "textDocument": {
                    "uri": TEST_FILE2_URI,
                    "languageId": "python",
                    "version": 1,
                    "text": contents,
                }
            }
        )

        done.wait(TIMEOUT)

        assert_that(actual, is_({"uri": TEST_FILE2_URI, "diagnostics": []}))

        done.clear()

        # Simulate a change in the file
        ls_session.notify_did_change(
            {
                "textDocument": {
                    "uri": TEST_FILE2_URI,
                    "version": 1,
                },
                "contentChanges": [
                    {
                        # "range": {
                        #     "start": {"line": 1, "character": 0},
                        #     "end": {"line": 1, "character": 0},
                        # },
                        "text": "x:int = 1\nx:int = 2",
                    }
                ],
            }
        )

        # wait for some time to receive all notifications
        done.wait(TIMEOUT)

        expected = {
            "uri": TEST_FILE2_URI,
            "diagnostics": [
                {
                    "range": {
                        "start": {"line": 1, "character": 0},
                        "end": {"line": 1, "character": 9},
                    },
                    "severity": Severity.WARNING,
                    "code": "TYG903:redefine-variable-warning",
                    "message": "Variable 'x' already defined",
                    "source": LINTER["name"],
                }
            ],
        }

        assert_that(actual, is_(expected))

        done.clear()

    