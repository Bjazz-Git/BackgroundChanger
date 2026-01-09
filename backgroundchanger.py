import ctypes
import os
import tkinter
from tkinter import filedialog

# Gets C functions and makes them compatible with Python
# Converts Python arguments and return types to C types
def access_c():
    path = os.path.dirname(__file__)
    background_changer = ctypes.CDLL(path+"\\clibrary.so")
    
    # Gets the change_image c function
    change_image = background_changer.changeImage

    # Sets the arguments and return types of change_image
    change_image.argtypes = [ctypes.c_wchar_p]
    change_image.restype = ctypes.c_int
    return background_changer


# Changes the Desktop background to a specific image in the background folder
def change_background(image):
    background_changer = access_c()
    background_changer.changeImage(image)


# Pulls up the users file explorer, allowing them to choose their backgrounds folder
# Then sets the users background folder to the selected folder
def set_background_folder():
    # The background folder's directory
    folder = tkinter.filedialog.askdirectory()
    with open("background_folder_directory.txt", "w") as f:
        f.write(format_directory(str(folder)))


# Formats the directory to prevent problems with c's window.h library
def format_directory(directory):
    formatted_directory = directory
    # Replaces forward slashes with backslashes
    formatted_directory = formatted_directory.replace("/", "\\")
    return formatted_directory


# Returns the backgrounds folder, if there is one
def get_folder(): 
    with open("background_folder_directory.txt", "r") as f:
            return f.read()


# Checks if there is a background folder 
def valid_folder():
    # Checks if the background folder contains text
    try: 
        directory = get_folder()
        # Checks if the directory store in file is valid
        if os.path.exists(directory):
            return True
            
        else:
            return False

    # There is no background folder      
    except:
        return None


# Returns a list of files in the background folder, if there are any
def files_in_folder():
    directory = get_folder()
    if directory is not None:
        return os.listdir(directory)


# Returns a list of all files that are images
def valid_files():
    files = files_in_folder()
    folder = get_folder()
    images = []

    # If the folder contains files
    if files:
        for file in files:
            if is_image(file):
                images.append(os.path.join(folder, file))
        
        return images
    
    # No valid images in folder
    else:
        return None


# Checks if a file can be used as a background image
def is_image(file):
    # List of valid extensions
    types = ["jpg", "jpeg", "png", "bmp"]

    # Check if file's extension is valid
    try:
        extension = file.split(".")[1]
        # Valid Image
        if extension in types:
            return True
        
        # Invalid Image
        else:
            return False
        
    # File doesn't have extension type    
    except:
        return False


# Gets all image names in the backgrounds folder
def get_image_names():
    # Gets all valid images
    images = valid_files()
    # Stores all image names
    image_names = []

    for image in images:
        # Gets all the folder names that the image is stored in
        image_directories = image.split("\\")
        # Gets the image name
        image_name = image_directories[len(image_directories) - 1]
        image_names.append(image_name)
    
    return image_names
        