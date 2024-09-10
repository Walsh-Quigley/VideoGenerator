import os
import shutil

def cleanup(dir_path):

    # Check if the directory exists
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        # Iterate over all the files in the directory
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            try:
                # Check if it's a file and delete it
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                # If it's a directory, delete it and its contents
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
    else:
        print(f'The directory {dir_path} does not exist.')

def cleanAll():
    # Call the function
    cleanup('./text')
    cleanup('./narration')
    cleanup('./images')

cleanAll()