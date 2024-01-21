import os

def delete_files_by_extension(folder_path, extension):
    try:
        # Get a list of all files in the folder
        all_files = os.listdir(folder_path)

        # Filter files based on the provided extension
        selected_files = [file for file in all_files if file.endswith(extension)]

        # Delete each selected file
        for file in selected_files:
            file_path = os.path.join(folder_path, file)
            os.remove(file_path)
            print(f"Deleted: {file_path}")

        print(f"Deletion of files with extension '{extension}' completed.")

    except Exception as e:
        print(f"Error: {e}")


# DEFINE FOLDER PATH AND EXTENSION HERE
folder_path = "D:\DSLR\Testing"
target_extension = '.CR2'
#EXECUTE THE DELETE OPERATION
delete_files_by_extension(folder_path, target_extension)
