import ttkbootstrap as ttkb
from GUIS.Buttons import Buttons

class LeftFrame(ttkb.Frame):
    def __init__(self, parent, controller, width, height):
        self.width = width/2
        self.height = height/2
        self.parent = parent
        self.controller = controller
        super().__init__(self.parent, height=self.height, width=self.width)
        self.pack_propagate(False)


class MainMenuLeft(ttkb.Frame):
    def __init__(self, parent, controller, helper, height, width):
        self.parent = parent
        self.controller = controller
        self.helper = helper
        self.height = height/2
        self.width = width/2

        super().__init__(self.parent, height=self.height, width=self.width)

        buttons_frame = Buttons(self, self.controller, self.helper)
        buttons_frame.pack(side="top", fill="both", expand=True)