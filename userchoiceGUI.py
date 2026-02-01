import tkinter as tk
from backgroundhelper import choose_random_background
from backgroundhelper import set_background_folder
from tkinter import OptionMenu
from ChooseImageGUI import ChooseImageGUI 

class UserChoiceGUI(tk.Frame):   
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        options = self.get_options()
        options_text = list(options.keys())

        # Sets the default background to the first background in the directory
        try:
            selected_option = tk.StringVar()
            selected_option.set(options_text[0])

        except IndexError as e:
            print(e)


        options_dropdown = OptionMenu(self, selected_option, *options_text)
        submit_button = tk.Button(self, text = "Submit", command=lambda option=selected_option: self.submit(option))

        options_dropdown.grid(row=0, column=0)
        submit_button.grid(row=0, column=1)

    # Takes the user's choice and activates the command that corresponds with that choice
    def submit(self, selected_option):
        options = self.get_options()
        option = selected_option.get()
        options[option]()

    def get_options(self):
        options = {"Set Background Folder" : set_background_folder,
                "Set Background": lambda: self.controller.show_frame(ChooseImageGUI.__name__), 
                "Set Random Background": choose_random_background}
        
        return options