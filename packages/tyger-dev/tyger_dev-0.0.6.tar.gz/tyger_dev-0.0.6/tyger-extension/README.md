# Tyger Extension for VS Code

This extension provides static type checking for Python files in VS Code using the Tyger type checker. It provides real-time feedback on type errors, helping you catch type-related issues early in your development process.

## About Tyger

Tyger is a static type checker for Python that helps identify type errors in your code. It analyzes your Python code without running it and reports potential type errors, helping you catch bugs before they occur at runtime.

The extension integrates Tyger with VS Code's editor interface to provide real-time feedback as you write code. It highlights type errors directly in your editor with explanatory messages, making it easier to understand and fix type-related issues.

## For Users

### Installation

You can install the Tyger extension directly from the Visual Studio Code Marketplace:

1. Open VS Code
2. Go to Extensions view (Ctrl+Shift+X)
3. Search for "Tyger"
4. Click "Install"

### Requirements

-   VS Code 1.78.0 or greater
-   Python 3.9 or greater
-   Python extension for VS Code

### Features

-   Real-time type checking of Python code
-   Error highlighting directly in your editor
-   Detailed error messages to help understand and fix type issues
-   Support for standard Python type annotations

### Configuration

The extension provides several settings to customize its behavior:

-   `tyger.args`: Additional command-line arguments to pass to Tyger
-   `tyger.path`: Custom path to the Tyger executable
-   `tyger.importStrategy`: Strategy for importing Tyger (useBundled, fromEnvironment)
-   `tyger.interpreter`: Path to Python interpreter to use for Tyger
-   `tyger.showNotifications`: Control when notifications are shown

You can access these settings through VS Code's Settings UI or by editing the settings.json file.

### Commands

The extension contributes the following commands:

-   `Tyger: Restart Server`: Restarts the Tyger language server

## For Developers

This section is intended for developers who want to contribute to the Tyger extension or modify it for their own needs.

### Development Requirements

1. VS Code 1.78.0 or greater
2. Python 3.9 or greater
3. Node.js 18.17.0 or greater
4. npm 8.19.0 or greater
5. Python extension for VS Code

### Setting Up the Development Environment

1. Clone the repository: `git clone https://github.com/pleiad/tyger-extension.git`
2. Navigate to the project directory: `cd tyger-extension`
3. Create and activate a Python virtual environment
4. Install `nox` in the activated environment: `python -m pip install nox`
5. Run `nox --session setup` to set up the development environment
6. Install test dependencies (optional): `python -m pip install -r src/test/python_tests/requirements.txt`
7. Install Node.js dependencies: `npm install`

### Building and Running the Extension

Run the `Debug Extension and Python` configuration from VS Code. That will build and debug the extension in a host window.

If you just want to build without debugging, you can run the build task in VS Code (`Ctrl+Shift+B`).

### Project Structure

-   `src/`: Contains the TypeScript code for the VS Code integration
    -   `common/`: Common utilities and constants
    -   `test/`: Test files
-   `bundled/`: Contains the Python code for the language server
    -   `tool/`: The language server implementation
    -   `libs/`: Dependencies for the language server

### Debugging

-   To debug both TypeScript and Python code: Use the `Debug Extension and Python` debug config
-   To debug only TypeScript code: Use the `Debug Extension` debug config
-   To debug an already running server: Use `Python Attach` and select the process running `lsp_server.py`

When stopping, be sure to stop both the TypeScript and Python debug sessions to avoid reconnection issues.

### Logging

The extension creates a logging Output channel that can be found under `Output` > `Tyger`.

You can control the log level by running the `Developer: Set Log Level...` command from the Command Palette and selecting the Tyger extension.

For logs between the Language Client and Language Server, set `"tyger.server.trace": "verbose"` in your settings.

### Testing

Tests are in `src/test/python_tests/test_server.py`.

You can run all tests using `nox --session tests` command or through the VS Code Test Explorer if you have installed the test dependencies.

### Linting

Run `nox --session lint` to run linting on both Python and TypeScript code.

### Packaging and Publishing

1. Update various fields in `package.json` as needed
2. Update the CHANGELOG.md for the new release
3. Build the package using `nox --session build_package`
4. Upload the generated `.vsix` file to the Visual Studio Code Marketplace

## Troubleshooting

### Module not found errors

If you encounter module not found errors (such as for `pygls`), this might occur if `bundled/libs` is empty. Make sure to follow the build steps for creating and bundling the required libraries.
