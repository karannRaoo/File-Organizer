import os 
import shutil

# folder path you want to organize
FOLDER_PATH = os.getcwd() # current working directory

# file type mapping
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.md'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],                     
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.js', '.html', '.css'], 
    'Others': []  # for files that don't fit into any category
}

# create folders if they don't exist
for folder in FILE_TYPES.keys(): # iterate through the keys of the FILE_TYPES dictionary
    folder_path = os.path.join(FOLDER_PATH, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# organize files
for filename in os.listdir(FOLDER_PATH): 
    file_path = os.path.join(FOLDER_PATH, filename) # create the full path to the file

    #skip folders
    if os.path.isdir(file_path):
        continue

    # get file extension
    file_ext = os.path.splitext(filename)[1].lower() # get the file extension and convert it to lowercase

    for folder, extensions in FILE_TYPES.items(): # iterate through the FILE_TYPES dictionary
        if file_ext in extensions: # check if the file extension is in the list of extensions for the current folder
            shutil.move(file_path, os.path.join(FOLDER_PATH, folder, filename)) # move the file to the corresponding folder
            
print("file organized successfully✅:") 
    