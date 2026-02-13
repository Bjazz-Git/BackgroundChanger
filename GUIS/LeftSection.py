import tkinter as tk
from GUIS.Buttons import Buttons

class LeftFrame(tk.Frame):
    def __init__(self, parent, controller, width, height):
        self.width = width
        self.height = height
        self.parent = parent
        self.controller = controller
        super().__init__(self.parent, height=self.height/2, width=self.width/2, highlightthickness=10, highlightbackground="black")
        self.pack_propagate(False)


class MainMenuLeft(tk.Frame):
    def __init__(self, parent, controller, helper, height, width):
        self.parent = parent
        self.controller = controller
        self.helper = helper
        self.height = height
        self.width = width

        super().__init__(self.parent, height=self.height/2, width=self.width/2)

        buttons_frame = Buttons(self, self.controller, self.helper)
        buttons_frame.pack(side="top", fill="both", expand=True)