import tkinter as tk
class MainMenuTop(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # Frame centered in top bar
        self.top_bar_frame2 = tk.Frame(self)
        self.top_bar_frame2.pack(side="top")

        # Labels
        self.Label1 = tk.Label(self.top_bar_frame2,  text="Backgrounds Directory:")
        self.Label2 = tk.Label(self.top_bar_frame2,  text="C:\\Users\\Braxt\\OneDrive\\Pictures\\Backgrounds")
        
        # Position labels 
        self.Label1.grid(row=0, column=0)
        self.Label2.grid(row=0, column=1)    