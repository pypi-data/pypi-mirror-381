import ctypes
import time

__all__ = ["CopilotKey", "__version__"]
__version__ = "0.2.0"

class _CopilotKey:
    def __call__(self):
        _send_windows_ctypes()


    def __repr__(self):
        return "<CopilotKey - call to send Shift+Win+F23>"

CopilotKey = _CopilotKey()

# -------- helpers --------
def _send_windows_ctypes() -> None:
    user32 = ctypes.windll.user32

    VK_LSHIFT = 0xA0
    VK_LWIN   = 0x5B
    VK_F23    = 0x86  # F23 (0x86)

    KEYEVENTF_EXTENDEDKEY = 0x0001
    KEYEVENTF_KEYUP = 0x0002

    # press
    user32.keybd_event(VK_LSHIFT, 0, 0, 0)
    time.sleep(0.0001)
    user32.keybd_event(VK_LWIN,   0, KEYEVENTF_EXTENDEDKEY, 0)
    time.sleep(0.0001)
    user32.keybd_event(VK_F23,    0, 0, 0)
    time.sleep(0.0001)
    # release
    user32.keybd_event(VK_F23,    0, KEYEVENTF_KEYUP, 0)
    time.sleep(0.0001)
    user32.keybd_event(VK_LWIN,   0, KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP, 0)
    time.sleep(0.0001)
    user32.keybd_event(VK_LSHIFT, 0, KEYEVENTF_KEYUP, 0)