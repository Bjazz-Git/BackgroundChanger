import tkinter as tk
from backgroundhelper import choose_random_background
from backgroundhelper import set_background_folder

class Buttons(tk.Frame):
        def __init__(self, parent, controller):
            self.controller = controller
            options = self.get_options()
            options_text = list(options.keys())
            option_buttons = []
            
            # Initialize Button Frame
            super().__init__(parent)

            # Buttons
            # Create the option buttons and add them into the option_buttons array
            for option_text in options_text:
                option_buttons.append(
                    tk.Button(self, text=option_text, command=lambda option=options[option_text]: option())
                )
            
            # Add the option buttons to the screen
            for i in range(len(option_buttons)):
                option_buttons[i].pack(side = "top", fill= "both", expand = True)
                 
        
        def get_options(self):
            options = {"Set Background Folder" :self.change_background_folder,
                    "Set Background": self.change_background, 
                    "Set Random Background": self.set_random_background}
            
            return options

        
        # Changes the frame to show a collection of scrollable images (all backgrounds name frame)
        def change_background(self):
            self.controller.show_frame("All_Backgrounds", "MainMenuLeft")
        

        def change_background_folder(self):
            set_background_folder()
            self.controller.refresh_screen(self.controller.top_bar)
            self.controller.refresh_screen(self.controller.left_frames["All_Backgrounds"])

        def set_random_background(self):
            choose_random_background()
            self.controller.refresh_screen(self.controller.right_bar)