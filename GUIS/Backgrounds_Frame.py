import ttkbootstrap as ttkb
from PIL import Image, ImageTk
from backgroundhelper import Background_Helper

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
            folder = self.folder_paths[i]
            new_helper = Background_Helper(folder)

            # Creates a new frame that will store the folder's images and folders
            folder_frame = Backgrounds_frame(self.parent, self.controller, helper=new_helper, main_frame=self.main_frame, 
                parent_frame=self, frame_num= self.frame_num + i + 1)

            # Used to store all other folder obejcts
            self.folder_frames.append(folder_frame)

            # The frame that is used to store the folder button
            selection_frame = ttkb.Frame(self)

            # Gets a string that is used to display the folder's name
            label = self.get_label(file=self.backgrounds_paths[i])

            # Creates a folder button that when clicked will display the images in the folder
            folder_button = ttkb.Button(selection_frame, image = self.folder_img, text=label,
                compound="bottom", bootstyle="light, outline",
                command = lambda folder_num = i: self.main_frame.open_folder(self.folder_frames[folder_num])
            )
            folder_button.pack(side="top")

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

            # A frame to store the background button in
            selection_frame = ttkb.Frame(self)

            # Gets a string that is used to display the background's name
            label = self.get_label(file=self.backgrounds_paths[i])

            # Creates a background button
            background_button = ttkb.Button(selection_frame, text= label, image = image, 
                compound="bottom", bootstyle="light, outline", 
                command= lambda image_num = i: self.set_background(image_num)
            )
            background_button.pack(side="top")

            # Stores the created buttons
            self.buttons.append(selection_frame)
        

        # Adds the background buttons/frames to the screen in a grid format
        for i in range(len(self.buttons)):
            row=int(i / self.column_count), 
            column=int(i % self.column_count)

            self.buttons[i].grid(row=row, column=column)


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