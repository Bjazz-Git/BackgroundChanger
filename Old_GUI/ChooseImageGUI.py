import tkinter as tk
from PIL import ImageTk, Image
import os
import backgroundhelper

class ChooseImageGUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Gets the paths to all the user's backgrounds
        self.backgrounds = backgroundhelper.get_background_paths()

        # Used to store background image objects
        self.background_objects = []

        # Used to track how many rows before backgrounds are displayed 
        header_rows = 1

        back_button = tk.Button(self, text="←", command= lambda: self.controller.show_frame("UserChoiceGUI"))
        back_button.grid(row = 0, column=0)

        # Creates an Image object for all images in the user's background directory and stores them into an array
        for background in self.backgrounds:
            # Gets Image
            image = Image.open(background).resize((400, 300))
            # Create Photo Image
            image = ImageTk.PhotoImage(image)
            self.background_objects.append(image)

        # Accesses the backgrounds array and creates buttons using the backgrounds as images
        for i in range(len(self.background_objects)):
            row = int(header_rows + i/2)
            column = 0 if i % 2 == 0 else 1

            # Creates a button, which when clicked, will set the user's background to the button's image
            background_button = tk.Button(self, image = self.background_objects[i], 
                command= lambda image_num = i: self.set_background(image_num)
            )
            background_button.grid(row=row, column=column)
    
    # Sets the user's background using the provided background image
    def set_background(self, background_num):
        backgroundhelper.pick_background(self.backgrounds[background_num])