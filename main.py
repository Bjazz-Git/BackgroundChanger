import backgroundchanger
import random
import appexceptions

def main():
    try:
        # pick_background()
        background = current_background()
        print(background)

    # Handles what happens if an image that couldn't be found in the backgrounds folder
    except (appexceptions.MissingImage) as e:
        print(e)
    
    # Handles what happens if an image couldn't be set as a background
    except (appexceptions.InvalidImage) as e:
        print(e)
    
    # Handles what happens if an unexpected error occurs in the program
    except Exception as e:
        print(e)


# Allows the user to pick their desktop's background
def pick_background():
    # Asks the user to pick a background from the backgrounds folder
    while True:
        # Get the images in the folder
        images = backgroundchanger.get_images()
        show_images()

        # Ask the user to pick a background image
        try:
            # If there are images in the folder, let the user select a background
            if len(images) > 0:
                user_input = int(input("Type a number to pick your background: "))
                backgroundchanger.change_background(images[user_input - 1])
                break
            else:
                print("No Background Images")
                break

        # User chose invalid number/image
        except Exception as e:
            raise e


# Displays the user's background images 
def show_images():
    image_names = backgroundchanger.get_image_names()
    img_num = 1
    for name in image_names:
        print(f"{img_num}: {name}")
        img_num += 1

# Chooses a random background from the background folder
def choose_random_background():
    images = backgroundchanger.valid_files()
    ran_image = random.choice(images)
    backgroundchanger.change_background(ran_image)

# Gets the user's current background
def current_background():
    print("function called")
    return backgroundchanger.get_background()

main()