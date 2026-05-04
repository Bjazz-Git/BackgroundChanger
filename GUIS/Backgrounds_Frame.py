import ttkbootstrap as ttkb
from PIL import Image, ImageTk
from Functionality.backgroundhelper import Background_Helper

class Backgrounds_frame(ttkb.Frame):
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
        # Gets the space the scrollbar takes and uses it as padding
        scrollbar = parent._scrollbar
        scrollbar_padding = scrollbar.cget("minimum_pixel_length") + 10
        # The size of all images stored in a tuple
        self.image_size = (int(self.main_frame.width / self.column_count - scrollbar_padding), int(self.main_frame.height/ self.column_count))
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
            # Trys to create a folder button, and if one was created adds it to the buttons list
            self.buttons.append(self.create_folder_button(self.folder_paths[i]))

        # Creates Background buttons, that when clicked, change the user's background to the clicked background
        for i in range(len(self.backgrounds_paths)):
            self.buttons.append(self.create_background_button(self.backgrounds_paths[i]))

        # Adds the background buttons/frames to the screen in a grid format
        for i in range(len(self.buttons)):
            # Adds a button to the screen
            self.place_file_button(i)


    # Gets the text that will be displayed on the background button's label
    def get_label(self, file):
        label_width = self.image_size[0]
        image_name = self.helper.get_file_name(file, label_width)
        return image_name


    # Sets the user's background using the provided background image
    def set_background(self, background_num):
        self.helper.pick_background(self.backgrounds_paths[background_num])
        main_frame = self.controller.controller
        main_frame.refresh_screen(main_frame.right_bar, helper=self.helper)


    # Adds a button to the screen/backgrounds frame
    def place_file_button(self, file_number):
        row=int(file_number / self.column_count), 
        column=int(file_number % self.column_count)

        self.buttons[file_number].grid(row=row, column=column)

    
    # Creates a folder button
    def create_folder_button(self, folder):
        new_helper = Background_Helper(folder)

        # Creates a new frame that will store the folder's images and folders
        folder_frame = Backgrounds_frame(self.parent, self.controller, helper=new_helper, main_frame=self.main_frame, 
            parent_frame=self)

        # Used to store all other folder obejcts
        self.folder_frames.append(folder_frame)

        # The frame that is used to store the folder button
        selection_frame = ttkb.Frame(self)

        # Gets a string that is used to display the folder's name
        label = self.get_label(file=folder)

        # Creates a folder button that when clicked will display the images in the folder
        folder_button = ttkb.Button(selection_frame, image = self.folder_img, text=label,
            compound="bottom", bootstyle="light, outline",
            command = lambda folder_num = len(self.folder_frames) - 1: self.main_frame.open_folder(self.folder_frames[folder_num])
        )
        folder_button.pack(side="top")

        # Returns the frame storing the folder button
        return selection_frame
    

    # Create a Background button
    def create_background_button(self, background):
        # Gets Image
        image = Image.open(background).resize(self.image_size)
        # Create Photo Image
        image = ImageTk.PhotoImage(image)
        # Stores all background images
        self.backgrounds.append(image)

        # A frame to store the background button in
        selection_frame = ttkb.Frame(self)

        # Gets a string that is used to display the background's name
        label = self.get_label(file=background)

        # Creates a background button
        background_button = ttkb.Button(selection_frame, text= label, image = image, 
            compound="bottom", bootstyle="light, outline", 
            command= lambda image_num = len(self.backgrounds) - 1: self.set_background(image_num)
        )
        background_button.pack(side="top")

        # Returns the frame containing the background button
        return selection_frame


    ## Started implementation of a way to refresh individual frames without deleting all frames
    # Refreshes the backgrounds in the current frame
    ## Note: get_label is called additional times to check if files are similar, this might cause performance issues and is a flawed way of checking if files are the same
    def refresh_backgrounds(self):
        # Gets the paths to all folders within the backgrounds directory
        new_folder_paths = self.helper.get_folders()
        # Gets the paths to all the user's backgrounds
        new_backgrounds_paths = self.helper.get_background_paths()

        background_frames = self.winfo_children()

        # Go through all of the folders and backgrounds in the frame 
        for i in range(len(background_frames)):
            current_file_name = background_frames[i].winfo_children()[0].cget("text")
            # Idx used to get the current background frame
            background_idx = abs(i - len(new_folder_paths))

            # Check if there are any new folders to add to the frame
            if i < len(new_folder_paths):
                # If the new folder is not equal to the folder on the frame, replace the previous folder with the new one
                if (self.get_label(new_folder_paths[i]) != current_file_name):
                    # print(f"{new_folder_paths[i]} != {current_file_name}")
                    # Destroys the previous folder button
                    background_frames[i].destroy()
                    # Creates a new folder button and stores it in an array
                    self.buttons[i] = self.create_folder_button(new_folder_paths[i])
                    # Places the folder button onto the screen
                    self.place_file_button(i)

            # Check if there are any new backgrounds to add to the frame
            elif background_idx < len(new_backgrounds_paths):
                # If the new background is not equal to the background on the frame, replace the current background with the new one
                if (self.get_label(new_backgrounds_paths[background_idx]) != current_file_name):
                    # print(f"{new_backgrounds_paths[background_idx]} != {current_file_name}")
                    # Destroys the previous background button
                    background_frames[i].destroy()
                    # Creates a new background button and stores it in an array
                    self.buttons[i] = self.create_background_button(new_backgrounds_paths[background_idx])
                    # Places the folder button onto the screen
                    self.place_file_button(i)

            # If this line is reached than there are no more folders or backgrounds to add to the screen
            else:
               # Destroys the leftover frame from before the refresh
               background_frames[i].destroy()
               # Removes the old frame from the buttons array
               self.buttons.pop(i)


        # Total new files added to the directory
        total_new_files = len(new_folder_paths) + len(new_backgrounds_paths)
        
        # Adds any new files not added to the screen to the screen
        for i in range(len(background_frames), total_new_files):
            # If there are folders buttons that haven't been added, add them to the screen
            if i < len(new_folder_paths):
                # Creates a new folder button and stores it in an array
                self.buttons.append(self.create_folder_button(new_folder_paths[i]))
                # Places the folder button onto the screen
                self.place_file_button(i)
            
            # If there are new background buttons that haven't been added, add them to the screen
            else:
                background_idx = abs(i - len(new_folder_paths))
                # Creates a new background button and stores it in an array
                self.buttons.append(self.create_background_button(new_backgrounds_paths[background_idx]))
                # Places the folder button onto the screen
                self.place_file_button(i)
        
