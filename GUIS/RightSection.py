import tkinter as tk
from tkinter import PhotoImage
from PIL import ImageTk, Image
from backgroundhelper import current_background

class MainMenuRight(tk.Frame):
    def __init__(self, parent, width, height):
        self.width = width
        self.height = height
        super().__init__(parent, width=self.width/2, height=self.height/2, highlightthickness=1, highlightbackground="purple")
        self.pack_propagate(False)

        # Frame to contain current background
        image_frame = tk.Frame(self, highlightbackground="orange", highlightthickness=10)

        # Background name
        self.background_name_label = tk.Label(image_frame, text="Current Background is: vow image", anchor="w", justify="left")
        
        # Background Label
        self.background_img = Image.open(current_background()).resize((int(self.width/2), int(self.height/2)))
        self.background_img = ImageTk.PhotoImage(self.background_img)
        print(type(self.background_img))
        self.image_label = tk.Label(image_frame, image=self.background_img) 

        # Formatting
        image_frame.pack(side="top", expand=True, padx=50, pady=50)
        self.background_name_label.pack(side="top", fill="both")
        self.image_label.pack(side="top", expand=True)
    
    def updateImage(self):
        self.background_img = current_background()

        