import ttkbootstrap as ttkb
from GUIS.TopSection import MainMenuTop
from GUIS.LeftSection import LeftFrame
from GUIS.LeftSection import MainMenuLeft
from GUIS.RightSection import MainMenuRight
from GUIS.Backgrounds import All_Backgrounds
from GUIS.Missing_Directory_Frame import Missing_Directory_Frame
from GUIS.Main_Frame import Main_Frame
from Functionality.backgroundhelper import Background_Helper

### TODO: If the main directory is empty the user should be shown a screen indicating they need to add a directory
### TODO: See what to do about the refresh method for the directory button change in Buttons class
### TODO: Dealing with all background folders and images being deleted (redirect user to main menu)
    ### Issues relates to Backgrounds refresh method.

### TODO: Add a feature that makes it so random images are choosen automatically at certain times, days, weeks, months
### TODO: Add the ability for users to ignore backgrounds (backgrounds that won't show up in the selection and random pool)
### TODO: self.width and self.height could possibly be improved to not require it as an argument


class MainMenuGUI:
    def __init__(self):
        self.window = ttkb.Tk()
        # Sets the window's theme/style
        self.style = ttkb.Style("darkly")
        # Sets the main window's width and height
        self.width = int(self.window.winfo_screenwidth() /1.5)
        self.height = int(self.window.winfo_screenheight() / 1.5)
        # centers the window in the middle of the screen
        self.center_window()
        # Sets window title
        self.window.title("Background Changer")
        # Prevents the window from being resized
        self.window.resizable(False, False)

        self.background_helper = Background_Helper()

        # If a background directory was provided then display the main frames
        if self.background_helper.get_background_folder() is not None:
            self.get_main_frame()

        # Display a frame asking the user to provide a background directory
        else:
            self.get_empty_frame()

    
    # This is the frame that will be displayed to the screen if the user has provided a backgrounds directory
    def get_main_frame(self):
        Main_Frame(window=self.window, parent=self, helper=self.background_helper)

    
    # This is the frame that will be displayed to the screen if the user has not provided a backgrounds directory
    def get_empty_frame(self):
        missing_directory_frame = Missing_Directory_Frame(parent=self.window, controller=self, helper=self.background_helper, width=self.width, height=self.height)
        missing_directory_frame.pack(side="top", fill="both")


    # Places the applications window in the center of the screen
    def center_window(self):
        x = (self.window.winfo_screenwidth() - self.width) / 2
        y = (self.window.winfo_screenheight() - self.height) / 2
        self.window.geometry(f"{self.width}x{self.height}+{int(x)}+{int(y)}")

    
if __name__ == "__main__":
    app = MainMenuGUI()
    app.window.mainloop()