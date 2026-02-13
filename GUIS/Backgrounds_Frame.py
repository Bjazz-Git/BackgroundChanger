import tkinter as tk
from PIL import Image, ImageTk

class Backgrounds_frame(tk.Frame):
    def __init__(self, parent, helper, controller):
        self.parent = parent
        self.controller = controller
        self.helper = helper
        # The size of all images stored in a tuple
        image_size = (320, 180)
        super().__init__(parent)
        
        # Gets the paths to all folders within the backgrounds directory
        self.folder_paths = self.helper.get_folders()
        # Gets the paths to all the user's backgrounds
        self.backgrounds_paths = self.helper.get_all_background_paths()

        # Stores all folders
        self.folders = []
        # Stores the background images by the frame
        self.backgrounds = []
        # Stores all buttons
        self.buttons = []

        # Number backgrounds per row
        column_count = 2

        # Create a folder object for all folders in the user's background directory and store them into an array
        for _ in range(len(self.folder_paths)):
            # Get the Folder placholder image
            folder = Image.open("Images/folder.png")
            # Creates a folder image object
            folder = ImageTk.PhotoImage(folder)
            # Stores the folder image object
            self.folders.append(folder)

        # Creates an Image object for all images in the user's background directory and store them into an array
        for i in range(len(self.backgrounds_paths)):
            # Gets Image
            image = Image.open(self.backgrounds_paths[i]).resize(image_size)
            # Create Photo Image
            image = ImageTk.PhotoImage(image)
            # Stores all background images
            self.backgrounds.append(image)

            # Creates a button, which when clicked, will set the user's background to the button's image
            background_button = tk.Button(self, image = image, 
                command= lambda image_num = i: self.set_background(image_num)
            )

            # Stores the created buttons
            self.buttons.append(background_button)
        

        # Create folder buttons that display all files within that folder
        for i in range(len(self.folders)):
            pass
        

        # Accesses the backgrounds array and creates buttons using the backgrounds as images
        for i in range(len(self.buttons)):
            row=int(i / column_count), 
            column=int(i % column_count)

            self.buttons[i].grid(row=row, column=column)

            # Creates a button, which when clicked, will set the user's background to the button's image
            # background_button = tk.Button(self, image = self.backgrounds[i], 
            #     command= lambda image_num = i: self.set_background(image_num)
            # )
            # background_button.grid(row=row, column=column)

    
    # Sets the user's background using the provided background image
    def set_background(self, background_num):
        self.helper.pick_background(self.backgrounds_paths[background_num])
        main_frame = self.controller.controller
        main_frame.refresh_screen(main_frame.right_bar, helper=self.helper)
        