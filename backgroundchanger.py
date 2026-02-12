import ctypes
import os
import appexceptions
import access_c
from validate_files import valid_files
from validate_files import valid_folder
import copy

# Provides a way to call the functions in accessbackground.c
background_changer = access_c.get_functions()

# Changes the Desktop background to a specific image in the background folder
def change_background(background):
    backgrounds = get_images()

    # Checks if the background specified is in the background folder
    if background in backgrounds:
        # background_changer = access_change_image()
        return_num = background_changer.changeBackground(background)

        # If the background change operation was unsuccessful, raise the exception
        if return_num < 1:
            raise appexceptions.InvalidImage

    # If the background couldn't be located in the background folder directory, raise the exception
    else:
        raise appexceptions.MissingImage


# Takes a folder path and stores it into a text file, if the path leads to a real directory
def set_background_folder(folder):
    if valid_folder(folder):
        with open("background_folder_directory.txt", "w") as f:
            f.write(format_directory(str(folder)))


# Formats the directory to prevent problems with c's window.h library
def format_directory(directory):
    formatted_directory = directory
    # Replaces the directory's forward slashes with backslashes
    formatted_directory = formatted_directory.replace("/", "\\")
    return formatted_directory


# Returns the backgrounds folder, if there is one
def get_folder(): 
    with open("background_folder_directory.txt", "r") as f:
            return f.read()


# Returns a list of files in the background folder, if there are any
def files_in_folder():
    directory = get_folder()
    if directory is not None:
        return os.listdir(directory)

# Gets the images in the background folder directory
def get_images():
    return valid_files(get_folder(), files_in_folder())

# Gets all image names in the backgrounds folder
def get_image_names():
    # Gets all valid images
    images = get_images()
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
def get_background():
    # Gets the pointer to the user's background
    background_pointer = background_changer.getBackground()

    # Makes a copy of the background contents
    # background = ctypes.c_char_p(background_pointer.value)
    # background = background.decode('utf-8')

    # Returns the copy of the background
    return background_pointer


# Frees the memory used by background
def free_memory(background):
   background_changer.freeMemory(background) 
        