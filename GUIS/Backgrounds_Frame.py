import tkinter as tk
from PIL import Image, ImageTk
from backgroundhelper import Background_Helper

class Backgrounds_frame(tk.Frame):
    def __init__(self, parent, controller, helper, main_frame, parent_frame = None, frame_num = 0):
        self.parent = parent
        self.controller = controller
        self.helper = helper
        self.main_frame = main_frame
        # Stores the location of the frame
        self.parent_frame = parent_frame
        self.frame_num = frame_num
        # The size of all images stored in a tuple
        image_size = (320, 180)
        super().__init__(parent)
        
        # Gets the paths to all folders within the backgrounds directory
        self.folder_paths = self.helper.get_folders()
        # Gets the paths to all the user's backgrounds
        self.backgrounds_paths = self.helper.get_all_background_paths()

        # Stores all folder frames
        self.folder_frames = []
        # Stores the background images by the frame
        self.backgrounds = []
        # Stores all buttons
        self.buttons = []

        # Number backgrounds per row
        column_count = 2

        # Get the Folder placholder image
        self.folder_img = Image.open("Images/folder.png").resize(image_size)
        # Creates a folder image object
        self.folder_img = ImageTk.PhotoImage(self.folder_img)

        # Create a folder object for all folders in the user's background directory and store them into an array
        for i in range(len(self.folder_paths)):
            new_helper = Background_Helper(self.folder_paths[i])

            # Creates a new frame that will store the folder's images and folders
            folder_frame = Backgrounds_frame(self.parent, self.controller, helper=new_helper, main_frame=self.main_frame, 
                parent_frame=self, frame_num= self.frame_num + i + 1)

            self.folder_frames.append(folder_frame)

            # Creates a folder button that when clicked will display the images in the folder
            folder_button = tk.Button(self, image = self.folder_img,
                command = lambda folder_num = i: self.main_frame.open_folder(self.folder_frames[folder_num])
            )

            # Stores the button in a list
            self.buttons.append(folder_button)

        # Creates Background buttons, that when clicked, change the user's background to the clicked background
        for i in range(len(self.backgrounds_paths)):
            # Gets Image
            image = Image.open(self.backgrounds_paths[i]).resize(image_size)
            # Create Photo Image
            image = ImageTk.PhotoImage(image)
            # Stores all background images
            self.backgrounds.append(image)

            # Creates a background button
            background_button = tk.Button(self, image = image, 
                command= lambda image_num = i: self.set_background(image_num)
            )

            # Stores the created buttons
            self.buttons.append(background_button)
        

        # Accesses the backgrounds array and creates buttons using the backgrounds as images
        for i in range(len(self.buttons)):
            row=int(i / column_count), 
            column=int(i % column_count)

            self.buttons[i].grid(row=row, column=column)

    
    # Sets the user's background using the provided background image
    def set_background(self, background_num):
        self.helper.pick_background(self.backgrounds_paths[background_num])
        main_frame = self.controller.controller
        main_frame.refresh_screen(main_frame.right_bar, helper=self.helper)
        