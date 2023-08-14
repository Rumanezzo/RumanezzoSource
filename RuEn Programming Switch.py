from win32api import SendMessage
from win32gui import GetForegroundWindow


def set_layout(flag):
    code = 0x04190419 if flag else 0x04090409
    window_handle = GetForegroundWindow()
    result = SendMessage(window_handle, 0x0050, 0, code)
    return result
# 0 - английский, 1 - русский
set_layout(0)
