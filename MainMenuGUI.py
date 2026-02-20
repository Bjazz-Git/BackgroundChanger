import ttkbootstrap as ttkb
from GUIS.TopSection import MainMenuTop
from GUIS.LeftSection import LeftFrame
from GUIS.LeftSection import MainMenuLeft
from GUIS.RightSection import MainMenuRight
from GUIS.Backgrounds import All_Backgrounds
from backgroundhelper import Background_Helper


### TODO: Improve formatting of Screens
### TODO: Create a refresh Button, to improve performance (prevent get_valid_files from being called over and over again)
### The location of files should be stored on file and this refresh button should be in the tool bar
### TODO: Add a feature that makes it so random images are choosen automatically at certain times, days, weeks, months
### TODO: Add the ability for users to ignore backgrounds (backgrounds that won't show up in the selection and random pool)


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

        # # Top Frame
        self.top_bar = self.createDirectoryFrame(self.background_helper)

        # Left Frame
        self.left_frames = {}
        self.left_frame = LeftFrame(self.window, controller=self, width=self.width, height=self.height)
        self.left_frame.pack(side="left", fill="both", expand=True)
        #Creates the left screens and adds them to a dictionary
        self.createButtonsFrame(self.background_helper)
        self.createBackgroundsFrame(self.background_helper)

        # Show the MainMenuLeft Frame
        self.show_frame(MainMenuLeft.__name__)
        
        # Right Frame
        self.right_bar = self.createCurrentBackgroundFrame(self.background_helper)

    # Places the applications window in the center of the screen
    def center_window(self):
        x = (self.window.winfo_screenwidth() - self.width) / 2
        y = (self.window.winfo_screenheight() - self.height) / 2
        self.window.geometry(f"{self.width}x{self.height}+{int(x)}+{int(y)}")


    # Creates the top frame that displays the user's current background directory
    def createDirectoryFrame(self, background_helper):
        top_bar = MainMenuTop(self.window, controller=self, helper = background_helper)
        top_bar.pack(side="top", fill="both")
        return top_bar


    # Creates the screen/frame that displays buttons for the user to make choices with
    def createButtonsFrame(self, background_helper):
        page_name = MainMenuLeft.__name__
        frame = MainMenuLeft(self.left_frame, controller=self, helper=background_helper, width=self.width, height=self.height)
        self.left_frames[page_name] = frame

    
    # Creates the screen/frame that displays clickable backgrounds for the user to select
    def createBackgroundsFrame(self, background_helper):
        page_name = All_Backgrounds.__name__
        frame = All_Backgrounds(self.left_frame, controller=self, helper = background_helper, width=self.width, height=self.height)
        self.left_frames[page_name] = frame


    # Creates the screen/frame that displays the user's current background
    def createCurrentBackgroundFrame(self, background_helper):
        right_bar = MainMenuRight(self.window, helper = background_helper, width=self.width, height=self.height)
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
    def refresh_screen(self, frame, helper):
        # Gets the name of the frame
        frame_name = type(frame).__name__

        # Change the directory name in the directory frame
        if (frame_name == MainMenuTop.__name__):
            # Refreshes the directory name
            self.top_bar.refresh_directory_name(helper)

        # Replaces current background frame with a new one
        elif (frame_name == MainMenuRight.__name__):
            # Destroys the current frame
            frame.destroy()
            # Creates a new current background frame
            self.right_bar = self.createCurrentBackgroundFrame(helper)
        
        # Replaces the backgrounds frame with a new one
        elif (frame_name == All_Backgrounds.__name__):
            # Destroys the current frame
            frame.destroy()
            # Creates a new backgrounds frame
            self.createBackgroundsFrame(helper)

    
if __name__ == "__main__":
    app = MainMenuGUI()
    app.window.mainloop()