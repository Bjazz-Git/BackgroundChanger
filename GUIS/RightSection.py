import tkinter as tk
from tkinter import PhotoImage
from PIL import ImageTk, Image


class MainMenuRight(tk.Frame):
    def __init__(self, parent, helper, width, height):
        self.helper = helper
        self.width = width
        self.height = height
        border_color = "black"
        image_size = (int(self.width/2), int(self.height/2))
        super().__init__(parent, width=self.width/2, height=self.height/2, highlightthickness=10, highlightbackground=border_color)
        self.pack_propagate(False)

        # Frame to contain current background
        image_frame = tk.Frame(self, highlightbackground=border_color, highlightthickness=10)
        
        # Current Background
        current_bg = self.helper.current_background()
        # Current Background Name
        current_bg_text = self.helper.get_file_name(current_bg, image_size[0])

        # Background name Label
        self.background_name_label = tk.Label(image_frame, text=f"Current Background is: {current_bg_text}", anchor="w", justify="left")
        
        # Background Label
        self.background_img = Image.open(current_bg).resize(image_size)
        self.background_img = ImageTk.PhotoImage(self.background_img)
        self.image_label = tk.Label(image_frame, image=self.background_img, background=border_color) 

        # Formatting
        image_frame.pack(side="top", expand=True, padx=50, pady=50)
        self.background_name_label.pack(side="top", fill="both")
        self.image_label.pack(side="top", fill="both", expand=True)

        