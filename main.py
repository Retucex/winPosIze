import win32process as process
import win32gui as gui
from win32helper import getCursorPos, enumWindows, Win32Window
import timer

windows = enumWindows()

print(getCursorPos())

for w in windows:
    print(f"{w} | {w.placement} | {process.GetWindowThreadProcessId(w.hwnd)}")