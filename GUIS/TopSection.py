import ttkbootstrap as ttkb

class MainMenuTop(ttkb.Frame):
    def __init__(self, parent, controller, helper):
        super().__init__(parent, borderwidth=2, relief="groove")
        self.parent = parent
        self.helper = helper
        self.controller = controller

        # Frame centered in top bar
        self.top_bar_frame2 = ttkb.Frame(self)
        self.top_bar_frame2.pack(side="top")

        # Labels
        self.directory_label = ttkb.Label(self.top_bar_frame2,  text="Backgrounds Directory:")
        self.directory_location_label = ttkb.Label(self.top_bar_frame2,  text="")
        # The total length the directory_location_label can take up (Accounts for the directory_label and adds padding of 10)
        self.label_length = controller.width - (self.directory_label.winfo_reqwidth() + 10)
        self.refresh_directory_name(self.helper)
        
        # Position labels 
        self.directory_label.grid(row=0, column=0)
        self.directory_location_label.grid(row=0, column=1)


    # Changes the directory's name to the one contained by the helper object
    def refresh_directory_name(self, helper):
        # Formats the directory text to prevent it from running of the screen
        directory_text = helper.format_directory_text(label_text=helper.get_background_folder(), label_width=self.label_length)
        self.directory_location_label.configure(text=directory_text)