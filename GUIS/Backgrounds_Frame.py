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
        # Number backgrounds per row
        self.column_count = 2
        # The size of all images stored in a tuple
        # Subtracted by 20 to account for scrollbar size
        self.image_size = (int(self.main_frame.width / self.column_count) - 20, int(self.main_frame.height/ self.column_count))
        super().__init__(parent)
        
        # Gets the paths to all folders within the backgrounds directory
        self.folder_paths = self.helper.get_folders()
        # Gets the paths to all the user's backgrounds
        self.backgrounds_paths = self.helper.get_background_paths()

        # Stores all folder frames
        self.folder_frames = []
        # Stores the background images by the frame
        self.backgrounds = []
        # Stores all buttons
        self.buttons = []


        # Get the Folder placholder image
        self.folder_img = Image.open("Images/folder.png").resize(self.image_size)
        # Creates a folder image object
        self.folder_img = ImageTk.PhotoImage(self.folder_img)

        # Create a folder object for all folders in the user's background directory and store them into an array
        for i in range(len(self.folder_paths)):
            folder = self.folder_paths[i]
            new_helper = Background_Helper(folder)

            # Creates a new frame that will store the folder's images and folders
            folder_frame = Backgrounds_frame(self.parent, self.controller, helper=new_helper, main_frame=self.main_frame, 
                parent_frame=self, frame_num= self.frame_num + i + 1)

            self.folder_frames.append(folder_frame)

            selection_frame = tk.Frame(self)
            # Creates a folder button that when clicked will display the images in the folder
            folder_button = tk.Button(selection_frame, image = self.folder_img,
                command = lambda folder_num = i: self.main_frame.open_folder(self.folder_frames[folder_num])
            )
            folder_button.pack(side="top")
            # Adds a label displaying the background's name
            self.add_label(parent=selection_frame, file=folder)

            # Stores the button in a list
            self.buttons.append(selection_frame)

        # Creates Background buttons, that when clicked, change the user's background to the clicked background
        for i in range(len(self.backgrounds_paths)):
            # Gets Image
            image = Image.open(self.backgrounds_paths[i]).resize(self.image_size)
            # Create Photo Image
            image = ImageTk.PhotoImage(image)
            # Stores all background images
            self.backgrounds.append(image)

            selection_frame = tk.Frame(self)
            # Creates a background button
            background_button = tk.Button(selection_frame, image = image, 
                command= lambda image_num = i: self.set_background(image_num)
            )
            background_button.pack(side="top")
            # Adds a label displaying the background's name
            self.add_label(parent=selection_frame, file=self.backgrounds_paths[i])

            # Stores the created buttons
            self.buttons.append(selection_frame)
        

        # Accesses the backgrounds array and creates buttons using the backgrounds as images
        for i in range(len(self.buttons)):
            row=int(i / self.column_count), 
            column=int(i % self.column_count)

            self.buttons[i].grid(row=row, column=column)

    # Adds a label to a frame that display's that frame's file's name
    def add_label(self, parent, file):
        label_width = self.image_size[0]
        image_name = self.helper.get_file_name(file, label_width)
        tk.Label(parent, text=image_name, bg="grey").pack(side="top", fill="both")



    # Sets the user's background using the provided background image
    def set_background(self, background_num):
        self.helper.pick_background(self.backgrounds_paths[background_num])
        main_frame = self.controller.controller
        main_frame.refresh_screen(main_frame.right_bar, helper=self.helper)