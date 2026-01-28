from tkinter import *
from PIL import ImageTk, Image
import os
import backgroundhelper

# Create the Image window
root = Tk()
root.geometry("800x600")

# Gets the paths to all the user's backgrounds
backgrounds = backgroundhelper.get_all_background_paths()

# Used to store background image objects
background_objects = []

# Sets the user's background using a provided background number 
# (This number corresponds to the images position in the backgrounds array)
def set_background(background_num):
    backgroundhelper.pick_background(backgrounds[background_num])

# Creates an Image object for all images in the user's background directory and stores them into an array
for background in backgrounds:
    # Gets Image
    image = Image.open(background).resize((400, 300))
    # Create Photo Image
    image = ImageTk.PhotoImage(image)
    background_objects.append(image)

# Accesses the backgrounds array and creates buttons using the backgrounds as images
for i in range(len(background_objects)):
    row = int(i/2)
    column = 0 if i % 2 == 0 else 1
    # Creates a button, which when clicked, will set the user's background to the button's image
    background_button = Button(root, image= background_objects[i], 
        command= lambda i=i: set_background(i)
    )
    background_button.grid(row=row, column=column)

root.mainloop()