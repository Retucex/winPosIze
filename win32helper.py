import win32gui as gui

class Win32WindowPlacement:
    def __init__(self, placement = None):
        if placement != None:
            (self.flags, self.showCmd,
            (self.minPosX, self.minPosY),
            (self.maxPosX, self.maxPosY),
            (self.posXTopLeft, self.posYTopLeft, self.posXBottomRight, self.posYBottomRight)) = placement

    def minPos(self):
        return (self.minPosX, self.minPosY)

    def maxPos(self):
        return (self.maxPosX, self.maxPosY)

    def windowedPos(self):
        return (self.posXTopLeft, self.posYTopLeft, self.posXBottomRight, self.posYBottomRight)


class Win32Window:
    def __init__(self, hwnd):
        self.hwnd = hwnd
        self.title = gui.GetWindowText(hwnd)
        self.isVisible = gui.IsWindowVisible(hwnd)
        self.placement = Win32WindowPlacement(gui.GetWindowPlacement(hwnd))

    def getPosition(self):
        return self.placement.windowedPos()

    # def flash(self, count = 0, timeout = 0):
    #     if count == 0 and timeout == 0:
    #         gui.FlashWindow(self.hwnd, 0)
    #     else:
    #         gui.FlashWindowEx(self.hwnd, 0, count, timeout)

    def __str__(self):
        return f"[{self.hwnd}] - {self.title}"

def currentWindow():
    return Win32Window(gui.GetForegroundWindow())

def enumWindows():

    def callback(hwnd, listwin):
        win = Win32Window(hwnd)
        if win.isVisible and len(win.title) > 0:
            listwin.append(Win32Window(hwnd))

    windows = []
    gui.EnumWindows(callback, windows)

    return windows

def getCursorPos():
    (_, _, (x, y)) = gui.GetCursorInfo()
    return (x, y)