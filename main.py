import ctypes
import os
import tkinter
from tkinter import filedialog

def main():
    change_background()

def change_background():
    path = os.path.dirname(__file__)
    background_changer = ctypes.CDLL(path+"\\clibrary.so")
    background_changer.changeImage()


# Pulls up the users file explorer, allowing them to choose their backgrounds folder
# Then sets the users background folder to the folder they selected
def set_background_folder():
    # The background folder's directory
    folder_direct = tkinter.filedialog.askdirectory()
    with open("background_folder_directory.txt", "w") as f:
        f.write(folder_direct)


# Checks if there is a background folder 
def valid_folder():
    # Checks if the background folder contains text
    try: 
        with open("background_folder_directory.txt", "r") as f:
            directory = f.read()
            # Checks if the directory store in file is valid
            if os.path.exists(directory):
                return True
            
            else:
                return False

    # There is no background folder      
    except:
        return None

# Returns the backgrounds folder, if there is one
def get_folder():
    if valid_folder():
        with open("background_folder_directory.txt", "r") as f:
            return f.read()
    
    else:
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
        

main()