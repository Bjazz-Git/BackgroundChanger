import tkinter as tk
from PIL import Image, ImageTk
import customtkinter
from GUIS.Backgrounds_Frame import Backgrounds_frame

class All_Backgrounds(tk.Frame):
    def __init__(self, parent, helper, controller, width, height):
        self.parent = parent
        self.controller = controller
        self.helper = helper
        self.width = width/2
        self.height = height/2
        super().__init__(self.parent, width=self.width, height=self.height, highlightthickness=1, highlightbackground="blue")
        self.pack_propagate(False)

        # Back Button Frame
        self.back_button_frame = tk.Frame(self)
        # Back Button
        self.back_button = tk.Button(self.back_button_frame, text="Back", command= lambda: self.back())

        # Scrollable Frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(
            self, orientation="vertical", label_text="Select a background",
            border_color="red", fg_color="transparent"
        )

        # Creates a frame that contains all user backgrounds
        self.backgrounds_frame = Backgrounds_frame(self.scrollable_frame, controller=parent, helper=helper)

        # Position frames
        self.back_button_frame.pack(side="top", fill="both")
        self.back_button.pack(side="left")
        self.scrollable_frame.pack(side="left", fill="both", expand=True)
        self.backgrounds_frame.pack(side="left", fill="both", expand=True)

    
    # Goes back to the button page
    def back(self):
        self.controller.show_frame("MainMenuLeft", "All_Backgrounds")

