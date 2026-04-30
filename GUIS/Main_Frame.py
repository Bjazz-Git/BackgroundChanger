import ttkbootstrap as ttkb
from GUIS.TopSection import MainMenuTop
from GUIS.LeftSection import LeftFrame
from GUIS.LeftSection import MainMenuLeft
from GUIS.RightSection import MainMenuRight
from GUIS.Backgrounds import All_Backgrounds

class Main_Frame(ttkb.Frame):
    def __init__(self, window, parent, helper):
        self.window = window
        self.parent = parent
        self.width = self.parent.width
        self.height = self.parent.height
        self.style = self.parent.style
        self.background_helper = helper
        super().__init__(self.window)

        # Top Frame
        self.top_bar = self.createDirectoryFrame(self.background_helper)

        # Left Frame
        self.left_frames = {}
        self.left_frame = LeftFrame(self, controller=self, width=self.width, height=self.height)
        self.left_frame.pack(side="left", fill="both", expand=True)
        #Creates the left screens and adds them to a dictionary
        self.createButtonsFrame(self.background_helper)
        self.createBackgroundsFrame(self.background_helper)

        # Show the MainMenuLeft Frame
        self.show_frame(MainMenuLeft.__name__)
        
        # Right Frame
        self.right_bar = self.createCurrentBackgroundFrame(self.background_helper)


    # Creates the top frame that displays the user's current background directory
    def createDirectoryFrame(self, background_helper):
        top_bar = MainMenuTop(self, controller=self, helper = background_helper)
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
        right_bar = MainMenuRight(self, helper = background_helper, width=self.width, height=self.height)
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