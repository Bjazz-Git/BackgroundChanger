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


# Returns a list of all files that are images and folders within the current directory
def valid_files(folder, files):
    directory_files = {}
    directory_files["images"] = []
    directory_files["folders"] = []

    print("new call")

    # If the folder contains files
    if files:
        for file in files:
            # Gets the full path to the image
            file_directory = os.path.join(folder, file)

            # If file is an image, add it to the images dictionary
            if is_image(file):
                directory_files["images"].append(file_directory)

            # If the file is a folder, add it to the folders directory
            elif is_folder(file_directory):
                print(file)
                directory_files["folders"].append(file_directory)
        
        # Returns all valid files (images and folders)
        return directory_files


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
    

# Checks if a file is a folder
def is_folder(file):
    return os.path.isdir(file)