import ttkbootstrap as ttkb
from GUIS.Buttons import Buttons

class Missing_Directory_Frame(ttkb.Frame):
    def __init__(self, parent, controller, helper, width, height):
        self.parent = parent
        self.controller = controller
        self.helper = helper
        self.width = width
        self.height = height
        super().__init__(self.parent)

        # Creates a buttons frame
        self.change_directory_button = Buttons(self, self.controller, self.helper)
        self.change_directory_button.create_change_bg_folder_button()
        self.change_directory_button.pack(side="top", fill="both", expand=True)


