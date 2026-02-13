import tkinter as tk

class MainMenuTop(tk.Frame):
    def __init__(self, parent, helper):
        super().__init__(parent, highlightbackground="black", highlightthickness=10)
        self.parent = parent
        self.helper = helper

        # Frame centered in top bar
        self.top_bar_frame2 = tk.Frame(self)
        self.top_bar_frame2.pack(side="top")

        # Labels
        self.directory_label = tk.Label(self.top_bar_frame2,  text="Backgrounds Directory:")
        self.directory_location_label = tk.Label(self.top_bar_frame2,  text=f"{self.helper.get_background_folder()}")
        
        # Position labels 
        self.directory_label.grid(row=0, column=0)
        self.directory_location_label.grid(row=0, column=1)

    def refresh_directory_name(self):
        self.directory_location_label.configure(text=self.helper.get_background_folder())