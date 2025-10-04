__all__ = ["CopilotKey", "press", "__version__"]
__version__ = "0.1.1"

import sys
import warnings

def press():
    """Send Shift + Win + F23 (best-effort)."""
    if _try_keyboard_send():
        return
    if sys.platform.startswith("win"):
        _send_windows_ctypes()
        return
    raise NotImplementedError(
        "copilotkey: automatic key injection is implemented for Windows. "
        "On other OSes install 'keyboard' or request a port."
    )

# alias
send = press

class _CopilotKey:
    def __call__(self):
        press()
    def press(self):
        press()
    def __repr__(self):
        return "<CopilotKey - call to send Shift+Win+F23>"

CopilotKey = _CopilotKey()

# -------- helpers --------
def _try_keyboard_send() -> bool:
    try:
        import keyboard  # optional dependency
    except Exception:
        return False
    try:
        keyboard.send("shift+windows+f23")
        return True
    except Exception as e:
        warnings.warn(f"copilotkey: keyboard.send failed: {e}; falling back.")
        return False

def _send_windows_ctypes() -> None:
    import ctypes
    user32 = ctypes.windll.user32

    VK_LSHIFT = 0xA0
    VK_LWIN   = 0x5B
    VK_F23    = 0x86  # F23 (0x86)

    KEYEVENTF_EXTENDEDKEY = 0x0001
    KEYEVENTF_KEYUP = 0x0002

    # press
    user32.keybd_event(VK_LSHIFT, 0, 0, 0)
    user32.keybd_event(VK_LWIN,   0, 0, 0)
    user32.keybd_event(VK_F23,    0, 0, 0)
    # release
    user32.keybd_event(VK_F23,    0, KEYEVENTF_KEYUP, 0)
    user32.keybd_event(VK_LWIN,   0, KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP, 0)
    user32.keybd_event(VK_LSHIFT, 0, KEYEVENTF_KEYUP, 0)
