import backgroundchanger

def main():
    pick_background()

# TODO: If the user adds an image to the folder after all images have been displayed to the user, 
# choosing an image through numbers could cause the incorrect background to be set.
# Prompts the user to pick a background from the background folder
def pick_background():
    show_images()
    # Asks the user to pick a background from the backgrounds folder
    while True:
        try:
            user_input = int(input("Type a number to pick your background: "))
            images = backgroundchanger.valid_files()
            backgroundchanger.change_background(images[user_input - 1])
            break
        except:
            print("Invalid Choice")


# Displays the user's background images 
def show_images():
    image_names = backgroundchanger.get_image_names()
    img_num = 1
    for name in image_names:
        print(f"{img_num}: {name}")
        img_num += 1

main()