import os
import shutil
import logging

# Logging Configuration
logging.basicConfig(filename='file_organizer.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# User should update these paths according to their system
documents_path = "<Path to your Documents folder>"
downloads_path = "<Path to your Downloads folder>"

# User should define their own destination directories here
destinations = {
    'Business': "<Path to Business folder>",
    'Personal': "<Path to Personal folder>",
    'School': "<Path to School folder>",
    'Play': "<Path to Play folder>",
}

# File type or keyword mapping for categories
# User can customize these keywords and file types
file_type_keywords = {
    'Business': ['.docx', '.xlsx', '.pptx', 'report', 'invoice'],
    'Personal': ['.jpg', '.jpeg', '.png', 'letter', 'diary'],
    'School': ['.pdf', 'homework', 'assignment', 'lecture'],
    'Play': ['.mp3', '.mp4', '.avi', 'game', 'movie'],
}

def determine_category(file_name):
    file_name_lower = file_name.lower()
    file_extension = os.path.splitext(file_name_lower)[1]
    for category, identifiers in file_type_keywords.items():
        if any(identifier in file_name_lower or file_extension == identifier for identifier in identifiers):
            return category
    return 'Other'

def rename_if_exists(dest_path, item):
    base, extension = os.path.splitext(item)
    counter = 1
    new_name = item
    while os.path.exists(os.path.join(dest_path, new_name)):
        new_name = f"{base}_{counter}{extension}"
        counter += 1
    return new_name

def organize_files(path):
    logging.info(f"Organizing files in {path}")
    for item in os.listdir(path):
        try:
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                category = determine_category(item)
                dest_path = destinations.get(category, "<Path to Other folder>")
                if not os.path.exists(dest_path):
                    os.makedirs(dest_path)
                new_item_name = rename_if_exists(dest_path, item)
                new_item_path = os.path.join(dest_path, new_item_name)
                shutil.move(item_path, new_item_path)
                logging.info(f"Moved {item} to {new_item_path}")
        except Exception as e:
            logging.error(f"Error moving {item}: {e}")

organize_files(documents_path)
organize_files(downloads_path)

logging.info("File organization completed.")
