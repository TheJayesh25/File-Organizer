import os
import shutil

# Define the folder to be organized
folder_to_organize = r'folder_path_needed_to_organize'  # Change this to your folder path

# Define categories and their corresponding file extensions
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Applications': ['.exe', '.msi', '.dmg', '.apk'],
    'Others': []
}

def get_file_type(extension):
    for category, extensions in file_types.items():
        if extension in extensions:
            return category
    return 'Others'

if __name__ == '__main__':
    print('Files have been organized!')
  
