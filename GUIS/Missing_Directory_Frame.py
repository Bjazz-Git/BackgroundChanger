import ttkbootstrap as ttkb
from GUIS.Buttons import Buttons

class Missing_Directory_Frame(ttkb.Frame):
    def __init__(self, parent, controller, helper, width, height):
        self.parent = parent
        self.controller = controller
        self.helper = helper
        self.width = width/2
        self.height = height/2
        self.font_size = 40
        super().__init__(self.parent, width=self.width, height=self.height, borderwidth=2, relief="groove")

        # # # Label used to ask user to set background
        self.label = ttkb.Label(self, text="Select a folder that contains your backgrounds", font=(self.font_size), anchor="center", justify="center")

        # Creates a buttons frame
        self.change_directory_button = Buttons(self, self.controller, self.helper, width=self.width, height=self.height)
        print(self.label.winfo_reqwidth())
        print(self.winfo_reqheight())
        self.change_directory_button.create_change_bg_folder_button(width = self.label.winfo_reqwidth()/1.75, height=self.winfo_reqheight()/4)
        
        # Pack Objects
        self.label.pack(side="left")
        self.change_directory_button.pack(side="left", fill="both", expand=True)


    def change_screen(self, new_frame_name, old_frame):
        self.controller.change_screen(new_frame_name, old_frame)


