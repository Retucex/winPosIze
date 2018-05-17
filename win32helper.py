import win32gui as gui

class Win32WindowPlacement:
    def __init__(self, placement=None):
        if placement != None:
            (self.flags, self.showCmd,
            (self.minPosX, self.minPosY),
            (self.maxPosX, self.maxPosY),
            (self.posXTopLeft, self.posYTopLeft, self.posXBottomRight, self.posYBottomRight)) = placement


class Win32Window:
    def __init__(self, hwnd):
        self.hwnd = hwnd
        self.title = gui.GetWindowText(hwnd)
        self.isVisible = gui.IsWindowVisible(hwnd)
        self.placement = Win32WindowPlacement(gui.GetWindowPlacement(hwnd))

    def __str__(self):
        return f"[{self.hwnd}] - {self.title}" 