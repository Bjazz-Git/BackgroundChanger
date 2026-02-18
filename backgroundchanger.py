import ctypes
import os
import appexceptions
import access_c
from validate_files import valid_files
from validate_files import valid_folder
import copy


class Background_Changer():
    def __init__(self, directory):
        # Provides a way to call the functions in accessbackground.c
        self.background_changer = access_c.get_functions()
        self.directory = directory

    # Changes the Desktop background to a specific image in the background folder
    def change_background(self, background):
        return_num = self.background_changer.changeBackground(background)

        # If the background change operation was unsuccessful, raise the exception
        if return_num < 1:
            raise appexceptions.InvalidImage


    # Takes a folder path and stores it into a text file, if the path leads to a real directory
    def set_background_folder(self, folder):
        if valid_folder(folder):
            with open("background_folder_directory.txt", "w") as f:
                f.write(self.format_directory(str(folder)))


    # Formats the directory to prevent problems with c's window.h library
    def format_directory(self, directory):
        formatted_directory = directory
        # Replaces the directory's forward slashes with backslashes
        formatted_directory = formatted_directory.replace("/", "\\")
        return formatted_directory


    # Returns the backgrounds folder, if there is one
    def get_folder(self): 
        # If no directory was provided use the default directory
        if self.directory == "":
            with open("background_folder_directory.txt", "r") as f:
                    return f.read()
            
        # If a directory was provided then use that one isntead of the base directory
        else:
            return self.directory


    # Returns a list of files in the background folder, if there are any
    def files_in_folder(self, directory=""):
        # If no directory was provided get the default directory
        if directory == "":
            directory = self.get_folder()

        if directory is not None:
            return os.listdir(directory)


    # Gets all of the valid files from a directory (images and folders)
    def get_valid_files(self, directory=""):
        # If no directory was provided use the base background directory
        if directory == "":
            directory = self.get_folder()

        return valid_files(directory, self.files_in_folder(directory))


    # Gets the images in the background folder directory
    def get_images(self, directory=""):
        return self.get_valid_files(directory)["images"]


    # Gets the folders in the background folder directory
    def get_folders(self, directory=""):
        return self.get_valid_files(directory)["folders"]

    # Gets all image names in the backgrounds folder
    def get_image_names(self):
        # Gets all valid images
        images = self.get_images()
        # Stores all image names
        image_names = []

        for image in images:
            # Gets all the folder names that the image is stored in
            image_directories = image.split("\\")
            # Gets the image name
            image_name = image_directories[len(image_directories) - 1]
            image_names.append(image_name)
        
        return image_names


    # Gets the user's current background
    def get_background(self):
        # Gets the pointer to the user's background
        background_pointer = self.background_changer.getBackground()

        # Makes a copy of the background contents
        # background = ctypes.c_char_p(background_pointer.value)
        # background = background.decode('utf-8')

        # Returns the copy of the background
        return background_pointer


    # Frees the memory used by background
    def free_memory(self, background):
        self.background_changer.freeMemory(background) 
            