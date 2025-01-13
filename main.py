# Automated File Sorting

import os
import shutil

# Define paths for Downloads and subfolders
downloads_path = os.path.expanduser('~/Downloads')
folder_mapping = {
    'pdf': 'PDF Files',
    'pptx': 'Powerpoints',
    'py': 'Python',
    'txt': 'TextFiles',
    'docx': 'Documents'
}

# Create subfolders if they don't exist
for folder in folder_mapping.values():
    folder_path = os.path.join(downloads_path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


# Move files to the appropriate folder
def organize_files():
    for file_name in os.listdir(downloads_path):
        file_path = os.path.join(downloads_path, file_name)
        # Skip directories
        if os.path.isdir(file_path):
            continue
        # Get file extension and check if it's in the mapping
        file_extension = file_name.split('.')[-1].lower()
        if file_extension in folder_mapping:
            folder_name = folder_mapping[file_extension]
            destination_folder = os.path.join(downloads_path, folder_name)
            destination_path = os.path.join(destination_folder, file_name)
            # Move file to the corresponding folder
            shutil.move(file_path, destination_path)
            print(f"Moved {file_name} to {folder_name}")


organize_files()
