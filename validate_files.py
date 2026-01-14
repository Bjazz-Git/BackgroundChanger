import os

# Checks if there is a background folder 
def valid_folder(folder):
    # Checks if the background folder contains text
    try: 
        # Checks if the folder is on the user's computer
        if os.path.exists(folder):
            return True
            
        else:
            return False

    # There is no background folder      
    except:
        return False

# Returns a list of all files that are images
def valid_files(folder, files):
    images = []

    # If the folder contains files
    if files:
        for file in files:
            if is_image(file):
                images.append(os.path.join(folder, file))
        
        return images


# Checks if a file can be used as a background image
def is_image(file):
    # List of valid extensions
    types = ["jpg", "jpeg", "png", "bmp"]

    # Check if file's extension is valid
    try:
        extension = file.split(".")[1]
        # Valid Image
        if extension in types:
            return True
        
        # Invalid Image
        else:
            return False
        
    # File doesn't have extension type    
    except:
        return False