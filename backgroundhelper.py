import backgroundchanger
import random
import appexceptions
import tkinter
from tkinter import Tk
from tkinter import filedialog


def set_background_folder():
    root = Tk()
    root.withdraw()
    folder = filedialog.askdirectory()
    backgroundchanger.set_background_folder(folder)
    root.destroy()


def get_background_folder():
    return backgroundchanger.get_folder()
    

# Allows the user to pick their desktop's background
def pick_background(background):
    backgroundchanger.change_background(background)


# Chooses a random background from the background folder
def choose_random_background():
    images = backgroundchanger.get_images()
    ran_image = random.choice(images)
    backgroundchanger.change_background(ran_image)


# Gets the user's current background, and returns it as bytes
def current_background():
    background = backgroundchanger.get_background()

    return background


def get_all_background_names():
    return backgroundchanger.get_image_names()


def get_all_background_paths():
    return backgroundchanger.get_images()


# Takes an image as bytes and returns the name of the image
def get_image_name(image):
    # Converts the bytes into a string and then gets each section of the image's directory
    directory_sections = image.decode("utf-8").split("\\")

    # Returns the last part of the directory, which is the image's given name
    # The image's extension is also removed before return
    return directory_sections[-1].split(".")[0]

