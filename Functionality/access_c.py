import os
import ctypes

# Gets C functions and makes them compatible with Python
# Converts Python arguments and return types to C types
def get_functions():
    path = os.path.dirname(__file__)
    background_changer = ctypes.CDLL(path+"\\clibrary.so")
    access_change_image(background_changer)
    access_get_background(background_changer)
    access_free_memory(background_changer)
   
    return background_changer

def access_change_image(background_changer):
    # Gets the changeImage c function
    change_image = background_changer.changeBackground

    # Sets the arguments and return types of change_image
    change_image.argtypes = [ctypes.c_wchar_p]
    change_image.restype = ctypes.c_int

    return background_changer

def access_get_background(background_changer):
    # Gets the getBackground c function
    get_background = background_changer.getBackground

    # Sets getBackground's return type
    get_background.restype = ctypes.c_char_p

    return background_changer

def access_free_memory(background_changer):
    # Gets the freeMemory c function
    free_memory = background_changer.freeMemory

    # Sets free memory's argument
    free_memory.argtypes = [ctypes.c_void_p]

    return background_changer