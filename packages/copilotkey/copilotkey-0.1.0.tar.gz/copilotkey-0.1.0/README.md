# copilotkey

Tiny Python package to send **Shift+Win+F23** (the Copilot Key) when called.

## Install locally
```bash
pip install -e .
```

## Usage
```python
from copilotkey import CopilotKey

CopilotKey()        # sends Shift+Win+F23
CopilotKey.press()  # same thing
```

## CLI
```
copilotkey   # runs the command-line entrypoint (sends the key once)
python -m copilotkey
```

## Notes
- Primary target: **Windows**. The package tries `keyboard.send("shift+windows+f23")` first (if `keyboard` installed). If not present, it falls back to a Windows API call using `ctypes`.
- The simulated keypress goes to the currently focused window.
