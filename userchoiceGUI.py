import tkinter
from tkinter import Tk
from backgroundhelper import choose_random_background
from backgroundhelper import set_background_folder
from backgroundhelper import current_background
from backgroundhelper import pick_background
from tkinter import OptionMenu

# def get_user_input():
# Print User options
entryWindow = Tk()
# user_input = tkinter.StringVar()
options = {"Set Background Folder" : set_background_folder, 
           "Get Background Folder": current_background, 
           "Set Background": pick_background, 
           "Set Random Background": choose_random_background}

options_text = list(options.keys())

# Sets the default background to the first background in the directory
try:
    selected_option = tkinter.StringVar()
    selected_option.set(options_text[0])

except IndexError as e:
    print(e)


options_dropdown = OptionMenu(entryWindow, selected_option, *options_text)
options_dropdown.pack()

def submit():
    option = selected_option.get()
    options[option]()
    # match options.get(option):
    #     case 1:
    #         set_background_folder()
    #     case 2:
    #         current_background()
    #     case 3:
    #         pick_background()
    #     case 4:
    #         choose_random_background()

# input_field = tkinter.Entry(entryWindow, textvariable=user_input)
submit_button = tkinter.Button(entryWindow, text = "Submit", command=submit)

options_dropdown.grid(row=0, column=0)
submit_button.grid(row=0, column=1)
entryWindow.mainloop()





    