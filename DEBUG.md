# DEBUG

## Launch json and Tasks json

```bash
mkdir -p .vscode
echo '{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Debug",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/src/main.py",
            "console": "integratedTerminal",
            "justMyCode": true,
            "env": {
                "PYTHON_KEYRING_BACKEND": "keyrings.cryptfile.cryptfile.CryptFileKeyring",
                "PYTHONPATH": "${workspaceFolder}/src/pb"
            },
            "envFile": "${workspaceFolder}/.env",
            "python": "${command:python.interpreterPath}",
            "pythonArgs": [
                "-BO"
            ],
            "preLaunchTask": "Check venv and generate config",
            "internalConsoleOptions": "neverOpen"
        }
    ]
}' > .vscode/launch.json

echo '{
    "version": "2.0.0",
    "cwd": "${workspaceFolder}",
    "type": "shell",
    "presentation": {
        "close": true
    },
    "tasks": [
        {
            "label": "Check venv and generate config",
            "command": "",
            "args": [
                "source",
                "venv/bin/activate;",
                "make",
                "config;"
            ],
        },
    ]
}' > .vscode/tasks.json
```
