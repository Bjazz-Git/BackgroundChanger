from tkinter import *
from PIL import ImageTk, Image
import os
import backgroundhelper

# Create the Image window
root = Tk()
root.geometry("800x600")

backgrounds = backgroundhelper.get_all_background_paths()

background_objects = []

for background in backgrounds:
    # Gets Image
    image = Image.open(background).resize((400, 300))
    # Create Photo Image
    image = ImageTk.PhotoImage(image)
    background_objects.append(image)


for i in range(len(background_objects)):
    row = int(i/2)
    column = 0 if i % 2 == 0 else 1
    background_object = Label(root, image=background_objects[i])
    background_object.grid(row=row, column=column)

root.mainloop()