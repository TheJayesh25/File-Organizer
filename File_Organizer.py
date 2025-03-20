import os
import shutil

# Define the folder to be organized
folder_to_organize = r'folder_path_needed_to_organize' 

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

def organize_files():
    # Get all file names in the folder
    for file_name in os.listdir(folder_to_organize):
        file_path = os.path.join(folder_to_organize, file_name)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file_name)[1].lower()
            category = get_file_type(file_extension)
            category_folder = os.path.join(folder_to_organize, category)
            
            # Create category folders if they don't exist
            os.makedirs(category_folder, exist_ok=True)

            # Move files to their respective category's folders
            shutil.move(file_path, os.path.join(category_folder, file_name))
            print(f'Moved {file_name} to {category}/')

if __name__ == '__main__':
    organize_files()
    print('Files have been organized!')