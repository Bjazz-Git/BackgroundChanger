from backgroundchanger import Background_Changer
import random
import appexceptions
import tkinter
from tkinter import Tk
from tkinter import filedialog

class Background_Helper():
    def __init__(self, directory=""):
        self.background_changer = Background_Changer(directory= directory)


    def set_background_folder(self):
        root = Tk()
        root.withdraw()
        folder = filedialog.askdirectory()
        self.background_changer.set_background_folder(folder)
        root.destroy()


    def get_background_folder(self):
        return self.background_changer.get_folder()
        

    # Allows the user to pick their desktop's background
    def pick_background(self, background):
        self.background_changer.change_background(background)


    # Chooses a random background from the background folder
    def choose_random_background(self):
        images = self.get_all_images()
        ran_image = random.choice(images)
        self.background_changer.change_background(ran_image)


    # Gets the user's current background, and returns it as bytes
    def current_background(self):
        background = self.background_changer.get_background()

        return background


    # Get the file name of all the images within the background folder
    def get_background_names(self):
        return self.background_changer.get_image_names()


    # Get the directory paths to all the images within the background folder
    def get_background_paths(self):
        return self.background_changer.get_images()


    # Takes an image as bytes and returns the name of the image
    def get_image_name(self, image):
        # Converts the bytes into a string and then gets each section of the image's directory
        directory_sections = image.decode("utf-8").split("\\")

        # Returns the last part of the directory, which is the image's given name
        # The image's extension is also removed before return
        return directory_sections[-1].split(".")[0]


    # Gets the folders within the background directory
    def get_folders(self):
        return self.background_changer.get_folders()
    

    # Get all images in the directory, including those in sub folders
    def get_all_images(self):
        images = []
        folders = []
        
        # Get all files from the base directory to the last folder
        directory = ""
        current_folder = 0
        while True:
            directory_files = self.get_files(directory=directory)
            images.extend(directory_files["images"])
            folders.extend(directory_files["folders"])

            # If there is a folder that hasn't been checked set the new directory to it
            if (current_folder < len(folders)):
                directory = folders[current_folder]
                current_folder += 1
            
            # If there are no more folders to check, break 
            else:
                break

        # Return all found images
        return images
    

    # Gets the files and images at the base directory or a specified one
    def get_files(self, directory=""):
        return self.background_changer.get_valid_files(directory=directory)

