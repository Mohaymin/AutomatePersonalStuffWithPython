from PIL import Image
import os

folder_path = 'D:\DSLR\Testing\\'
target_extension = '.CR2'

def get_files_by_extension(folder_path, extension):
    try:
        # Get a list of all files in the folder
        all_files = os.listdir(folder_path)

        # Filter files based on the provided extension
        selected_files = [file for file in all_files if file.endswith(extension)]

        return selected_files

    except Exception as e:
        print(f"Error: {e}")
        return []


def convert_cr2_file_to_jpg(file_name):
    im = Image.open(folder_path + file_name)
    rgb_im = im.convert('RGB')
    rgb_im.save(folder_path + file_name + ".jpg")


#clear the junks in the console
os.system('cls' if os.name=='nt' else 'clear')

files_with_extension = get_files_by_extension(folder_path, target_extension)

if files_with_extension:
    print(f"Files with extension '{target_extension}' in {folder_path}:")
    for file in files_with_extension:
        convert_cr2_file_to_jpg(file)
