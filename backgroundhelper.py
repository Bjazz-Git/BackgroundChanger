import backgroundchanger
import random
import appexceptions
import tkinter
from tkinter import Tk
from tkinter import filedialog



# def main():
#     try:
#         # user_input = int(input("Enter a number: "))
#         userchoiceGUI.submit()
#         text_interface(2)
#         # set_background_folder()
            
#     # Handles what happens if an image that couldn't be found in the backgrounds folder
#     except (appexceptions.MissingImage) as e:
#         print(e)
    
#     # Handles what happens if an image couldn't be set as a background
#     except (appexceptions.InvalidImage) as e:
#         print(e)
    
#     # Handles what happens if an unexpected error occurs in the program
#     except Exception as e:
#         print(e)


def text_interface(user_input):

    # Call function based on user choice
    if user_input == 1:
        set_background_folder()

    elif user_input == 2:
        # backgroundchanger.free_memory(background_pointer)
        background_pointer = current_background()
        print(background_pointer)
        backgroundchanger.free_memory(background_pointer)
        
    # Set Background
    elif user_input == 3:
        pick_background()

    # Set Random Background
    elif user_input == 4:
        choose_random_background()

    # End Program
    elif user_input == 5:
        # Frees the memory assigned to background
        # backgroundchanger.free_memory(background_pointer)
        return False
    
    return True


def set_background_folder():
    root = Tk()
    root.withdraw()
    folder = filedialog.askdirectory()
    backgroundchanger.set_background_folder(folder)
    root.destroy()
    

# Allows the user to pick their desktop's background
def pick_background(background):
    backgroundchanger.change_background(background)


# Displays the user's background images 
def show_images():
    image_names = backgroundchanger.get_image_names()
    img_num = 1
    for name in image_names:
        print(f"{img_num}: {name}")
        img_num += 1

# Chooses a random background from the background folder
def choose_random_background():
    images = backgroundchanger.get_images()
    ran_image = random.choice(images)
    backgroundchanger.change_background(ran_image)


# Gets the user's current background
def current_background():
    background = backgroundchanger.get_background()

    return background


def get_all_background_names():
    return backgroundchanger.get_image_names()

def get_all_background_paths():
    return backgroundchanger.get_images()


# if __name__ == "__main__":
#     main()