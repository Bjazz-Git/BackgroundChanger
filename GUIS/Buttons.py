import ttkbootstrap as ttkb

class Buttons(ttkb.Frame):
        def __init__(self, parent, controller, helper):
            self.parent = parent
            self.controller = controller
            self.helper = helper
            # options = self.get_options()
            # options_text = list(options.keys())
            self.option_buttons = []
            
            # Initialize Button Frame
            super().__init__(parent)
                 

        # Creates a button that allows the user to change their background
        def create_change_bg_button(self):
            bg_button = self.create_button("Set Background", self.change_background)
            self.format_buttons()
            self.option_buttons.append(bg_button)
            self.option_buttons[len(self.option_buttons) - 1].pack(side = "top", fill= "both", expand = True)
            return bg_button
        
        
        # Changes the frame to show a collection of scrollable images (all backgrounds name frame)
        def change_background(self):
            self.controller.show_frame("All_Backgrounds", "MainMenuLeft")


        # Creates a button that allows the user to change their background folder
        def create_change_bg_folder_button(self):
            folder_button = self.create_button("Set Background Folder", self.change_background_folder)
            self.format_buttons()
            self.option_buttons.append(folder_button)
            self.option_buttons[len(self.option_buttons) - 1].pack(side = "top", fill= "both", expand = True)
            return folder_button
        
        # Allows the user to change their backgrounds folder
        def change_background_folder(self):
            self.helper.set_background_folder()
            print(type(self.parent).__name__)

            # If Missing Directory Frame, change the frame to the main menu frame
            if type(self.parent).__name__ == "Missing_Directory_Frame":
                pass

            # If Main menu frame, update screen to show directory change
            elif type(self.parent).__name__ == "MainMenuLeft":
                self.controller.refresh_screen(self.controller.top_bar, helper=self.helper)
                self.controller.refresh_screen(self.controller.left_frames["All_Backgrounds"], helper=self.helper)


        # Creates a button that allows the user to change their background to a random background
        def create_set_random_bg_button(self):
            random_bg_button = self.create_button("Set Random Background", self.set_random_background)
            self.format_buttons()
            self.option_buttons.append(random_bg_button)
            self.option_buttons[len(self.option_buttons) - 1].pack(side = "top", fill= "both", expand = True)
            return random_bg_button


        def set_random_background(self):
            self.helper.choose_random_background()
            self.controller.refresh_screen(self.controller.right_bar, helper=self.helper)


        # Creates a button with the specified name and command attached to a frame
        def create_button(self, buttonName, buttonCommand):
            button_frame = ttkb.Frame(self)
            button_frame.pack_propagate(False)

            button = ttkb.Button(button_frame, text=buttonName, command=lambda : buttonCommand())
            button.pack(side="top", fill="both", expand=True)
            return button_frame


        # Formats the buttons within the frame
        def format_buttons(self):
            buttons = self.winfo_children()
            number_of_buttons = len(buttons)

            for button in buttons:
                padding = 10
                button_width = int(self.parent.width / number_of_buttons) - padding * 2
                button_height = int(self.parent.height / number_of_buttons) - padding * 2

                button.config(width=button_width)
                button.config(height=button_height)
                button.config(padding=padding)