import win32process as process
import win32gui as gui
from win32helper import Win32Window, Win32WindowPlacement

def cb(hwnd, listwin):
    win = Win32Window(hwnd)
    if win.isVisible and len(win.title) > 0:
        listwin.append(Win32Window(hwnd))

windows = []
gui.EnumWindows(cb, windows)
print(gui.GetCursorInfo())

for w in windows:
    print(w)