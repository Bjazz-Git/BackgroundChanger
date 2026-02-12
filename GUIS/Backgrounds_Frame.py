import tkinter as tk
import backgroundhelper
from PIL import Image, ImageTk

class Backgrounds_frame(tk.Frame):
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        super().__init__(parent)

        # Gets the paths to all the user's backgrounds
        self.backgrounds_paths = backgroundhelper.get_all_background_paths()

        # Stores the background images by the frame
        self.backgrounds = []

        # Number backgrounds per row
        column_count = 2

        # Creates an Image object for all images in the user's background directory and stores them into an array
        for background in self.backgrounds_paths:
            # Gets Image
            image = Image.open(background).resize((320, 180))
            # Create Photo Image
            image = ImageTk.PhotoImage(image)
            self.backgrounds.append(image)

        # Accesses the backgrounds array and creates buttons using the backgrounds as images
        for i in range(len(self.backgrounds)):
            row=int(i / column_count), 
            column=int(i % column_count)

            # Creates a button, which when clicked, will set the user's background to the button's image
            background_button = tk.Button(self, image = self.backgrounds[i], 
                command= lambda image_num = i: self.set_background(image_num)
            )
            background_button.grid(row=row, column=column)

    
    # Sets the user's background using the provided background image
    def set_background(self, background_num):
        backgroundhelper.pick_background(self.backgrounds_paths[background_num])
        main_frame = self.controller.controller
        main_frame.refresh_screen(main_frame.right_bar)
        