import tkinter as tk
from backgroundhelper import choose_random_background
from backgroundhelper import set_background_folder
from tkinter import OptionMenu

class UserChoiceGUI(tk.Frame):   
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        options = self.get_options()
        options_text = list(options.keys())
        option_buttons = []

        # Sets the default background to the first background in the directory
        try:
            selected_option = tk.StringVar()
            selected_option.set(options_text[0])

        except IndexError as e:
            print(e)

        # Create the option buttons and add them into the option_buttons array
        for option_text in options_text:
            option_buttons.append(
                tk.Button(self, text=option_text, command=lambda option=options[option_text]: self.submit(option))
            )

        # Add the option buttons to the screen
        for i in range(len(option_buttons)):
            option_buttons[i].pack(side = "top", fill= "both", expand = True)

    # Takes the user's choice and activates the command that corresponds with that choice
    def submit(self, selected_option):
        # Call the option selected by the user
        selected_option()

    def get_options(self):
        options = {"Set Background Folder" : set_background_folder,
                "Set Background": lambda: self.controller.show_frame("All_Backgrounds"), 
                "Set Random Background": choose_random_background}
        
        return options