import tkinter as tk
from tkinter import ttk
from GUIS.TopSection import MainMenuTop
from GUIS.LeftSection import LeftFrame
from GUIS.LeftSection import MainMenuLeft
from GUIS.RightSection import MainMenuRight
from GUIS.Backgrounds import All_Backgrounds
### TODO: Folders should show up and allow the selection of images
### TODO: Improve formatting of Screens
### TODO: Make it so that long strings of text are cut off (using ...) instead of running off screen


class MainMenuGUI:
    def __init__(self):
        self.window = tk.Tk()
        # Sets the main window's width and height
        self.width = int(self.window.winfo_screenwidth() /1.5)
        self.height = int(self.window.winfo_screenheight() / 1.5)
        # centers the window in the middle of the screen
        self.center_window()
        # Sets window title
        self.window.title("Background Changer")
        # Prevents the window from being resized
        self.window.resizable(False, False)

        # # Top Frame
        self.top_bar = self.createDirectoryFrame()

        # Left Frame
        self.left_frames = {}
        self.left_frame = LeftFrame(self.window, controller=self, width=self.width, height=self.height)
        self.left_frame.pack(side="left", fill="both", expand=True)
        #Creates the left screens and adds them to a dictionary
        self.createButtonsFrame()
        self.createBackgroundsFrame()

        # Show the MainMenuLeft Frame
        self.show_frame(MainMenuLeft.__name__)
        
        # Right Frame
        self.right_bar = self.createCurrentBackgroundFrame()

    # Places the applications window in the center of the screen
    def center_window(self):
        x = (self.window.winfo_screenwidth() - self.width) / 2
        y = (self.window.winfo_screenheight() - self.height) / 2
        self.window.geometry(f"{self.width}x{self.height}+{int(x)}+{int(y)}")


    # Creates the top frame that displays the user's current background directory
    def createDirectoryFrame(self):
        top_bar = MainMenuTop(self.window)
        top_bar.pack(side="top", fill="both")
        return top_bar


    # Creates the screen/frame that displays buttons for the user to make choices with
    def createButtonsFrame(self):
        page_name = MainMenuLeft.__name__
        frame = MainMenuLeft(self.left_frame, controller=self, width=self.width, height=self.height)
        self.left_frames[page_name] = frame

    
    # Creates the screen/frame that displays clickable backgrounds for the user to select
    def createBackgroundsFrame(self):
        page_name = All_Backgrounds.__name__
        frame = All_Backgrounds(self.left_frame, controller=self, width=self.width, height=self.height)
        self.left_frames[page_name] = frame


    # Creates the screen/frame that displays the user's current background
    def createCurrentBackgroundFrame(self):
        right_bar = MainMenuRight(self.window, width=self.width, height=self.height)
        right_bar.pack(side="right", fill="both")
        return right_bar

    # Displays a hidden frame to the screen  
    def show_frame(self, page_name, previous_frame=""):
        if previous_frame != "":
            self.left_frames[previous_frame].pack_forget()

        '''Show a frame for the given page name'''
        frame = self.left_frames[page_name]
        frame.pack(side="top", fill="both", expand="True")
    
    # Refreshes a given frame. This is done to ensure up to date information is shown
    def refresh_screen(self, frame):
        # Gets the name of the frame
        frame_name = type(frame).__name__

        # Change the directory name in the directory frame
        if (frame_name == MainMenuTop.__name__):
            print("Reached")
            # Refreshes the directory name
            self.top_bar.refresh_directory_name()

        # Replaces current background frame with a new one
        elif (frame_name == MainMenuRight.__name__):
            # Destroys the current frame
            frame.destroy()
            # Creates a new current background frame
            self.right_bar = self.createCurrentBackgroundFrame()
        
        # Replaces the backgrounds frame with a new one
        elif (frame_name == All_Backgrounds.__name__):
            # Destroys the current frame
            frame.destroy()
            # Creates a new backgrounds frame
            self.createBackgroundsFrame()

    
if __name__ == "__main__":
    app = MainMenuGUI()
    app.window.mainloop()