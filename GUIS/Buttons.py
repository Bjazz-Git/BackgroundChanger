import ttkbootstrap as ttkb

class Buttons(ttkb.Frame):
        def __init__(self, parent, controller, helper):
            self.parent = parent
            self.controller = controller
            self.helper = helper
            options = self.get_options()
            options_text = list(options.keys())
            option_buttons = []

            # Button Formatting
            number_of_buttons = 3
            padding = 10
            button_width = int(self.parent.width / number_of_buttons) - padding * 2
            button_height = int(self.parent.height / number_of_buttons) - padding * 2
            
            # Initialize Button Frame
            super().__init__(parent)

            # Buttons
            # Create the option buttons and add them into the option_buttons array
            for option_text in options_text:
                # A frame to contain an option button
                option_frame = ttkb.Frame(self, width=button_width, height=button_height, padding=padding)
                option_frame.pack_propagate(False)
                ttkb.Button(
                    option_frame, text=option_text, 
                    command=lambda option=options[option_text]: option()
                ).pack(side="top", fill="both", expand=True)

                option_buttons.append(
                    option_frame
                )
            
            # Add the option buttons to the screen
            for i in range(len(option_buttons)):
                option_buttons[i].pack(side = "top", fill= "both", expand = True)
                 
        
        def get_options(self):
            options = {"Set Background Folder" :self.change_background_folder,
                    "Set Background": self.change_background, 
                    "Set Random Background": self.set_random_background}
            
            return options

        
        # Changes the frame to show a collection of scrollable images (all backgrounds name frame)
        def change_background(self):
            self.controller.show_frame("All_Backgrounds", "MainMenuLeft")
        

        def change_background_folder(self):
            self.helper.set_background_folder()
            self.controller.refresh_screen(self.controller.top_bar, helper=self.helper)
            self.controller.refresh_screen(self.controller.left_frames["All_Backgrounds"], helper=self.helper)

        def set_random_background(self):
            self.helper.choose_random_background()
            self.controller.refresh_screen(self.controller.right_bar, helper=self.helper)