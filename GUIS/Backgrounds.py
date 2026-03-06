import ttkbootstrap as ttkb

from PIL import Image, ImageTk
import customtkinter
from GUIS.Backgrounds_Frame import Backgrounds_frame

class All_Backgrounds(ttkb.Frame):
    def __init__(self, parent, helper, controller, width, height):
        self.parent = parent
        self.controller = controller
        self.helper = helper
        self.width = width/2
        self.height = height/2

        # The default theme color of objects
        default_color = self.controller.style.colors.primary

        super().__init__(self.parent, width=self.width, height=self.height)
        self.pack_propagate(False)

        # Frame that contains all of the buttons
        self.button_tool_bar = ttkb.Frame(self)

        # Back Button Frame
        self.back_button_frame = ttkb.Frame(self.button_tool_bar)
        # Back Button
        self.back_button = ttkb.Button(self.back_button_frame, text="Back", command= lambda: self.back())

        # Refresh Button Frame
        self.refresh_button_frame = ttkb.Frame(self.button_tool_bar)
        # Create Refresh Button
        self.refresh_button = ttkb.Button(self.refresh_button_frame, text="⟳", command= lambda: self.refresh_backgrounds())

        # Scrollable Frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(
            self, orientation="vertical", label_text="Select a background",
            corner_radius=0,
            fg_color="transparent", 
            label_fg_color=default_color, label_text_color="white",
            scrollbar_fg_color=default_color
        )

        # Creates a frame that contains all user backgrounds
        self.backgrounds_frame = Backgrounds_frame(self.scrollable_frame, controller=parent, helper=helper, main_frame=self)
        # Represents the current location/folder the user is in
        self.current_location = self.backgrounds_frame 

        # Position frames
        self.button_tool_bar.pack(side="top", fill="both", pady=5)
        self.back_button_frame.grid(row=0, column=0, padx=5)
        self.back_button.pack(side="left")
        self.refresh_button_frame.grid(row=0, column=1, padx=5)
        self.refresh_button.pack(side="left")
        self.scrollable_frame.pack(side="top", fill="both", expand=True, padx=0)
        self.backgrounds_frame.pack(side="top", fill="both", expand=True, padx=0)

    
    # Goes back to the previous screen
    def back(self):
        # If not at the default folder location, go back to the current folder's parent folder
        if self.current_location != self.backgrounds_frame:
            self.open_folder(self.current_location.parent_frame)
            # Updates the directory location
            self.update_directory(self.current_location)


        # If at the default folder location, go back to the main menu
        else:
            self.controller.show_frame("MainMenuLeft", "All_Backgrounds")

 
    # Hides all children in the scrollable frame and displays the given frame to the screen
    def open_folder(self, frame):
        self.current_location = frame
       
        for background_frame in self.scrollable_frame.winfo_children():
            background_frame.pack_forget()
        
        frame.pack(side="left", fill="both", expand=True)
        # Updates the directory location
        self.update_directory(self.current_location)


    # Refreshes the directory location to be accurate to where the user is located
    def update_directory(self, frame):
        self.controller.refresh_screen(self.controller.top_bar, frame.helper)

    
    # Refreshes the backgrounds frame to show any new backgrounds
    def refresh_backgrounds(self):
        # Gets the current frame being shown on the scrollable frame
        for background_frame in self.scrollable_frame.winfo_children():
            print("Frame: ")
            print(background_frame)

        self.controller.refresh_screen(self, self.helper)
        self.controller.show_frame("All_Backgrounds")

       


