import os
import shutil

downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

# Categories and their file extensions
file_types = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi"],
}

# Create category folders 
for folder in file_types.keys():
    folder_path = os.path.join(downloads_folder, folder)
    os.makedirs(folder_path, exist_ok=True)

# Organize files
for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Get file extension
    _, extension = os.path.splitext(filename)
    extension = extension.lower()

    moved = False

    for folder, extensions in file_types.items():
        if extension in extensions:
            destination = os.path.join(downloads_folder, folder, filename)
            shutil.move(file_path, destination)
            print(f"Moved: {filename} → {folder}")
            moved = True
            break

    # Handle unknown file types
    if not moved:
        other_folder = os.path.join(downloads_folder, "Others")
        os.makedirs(other_folder, exist_ok=True)

        destination = os.path.join(other_folder, filename)
        shutil.move(file_path, destination)
        print(f"Moved: {filename} → Others")

print("Downloads folder organized successfully!")