import os
import shutil
import zipfile
from pathlib import Path

#For Searching Files
def search_file(filename):

    for root, dirs, files in os.walk("C:\\"):

        if filename.lower() in [file.lower() for file in files]:

            print("File Found :", os.path.join(root, filename))
            return

    print("File Not Found")

#For Searching Folders

def search_folder(folder_name):

    for root, dirs, files in os.walk("C:\\"):

        if folder_name.lower() in [folder.lower() for folder in dirs]:

            print("Folder Found :", os.path.join(root, folder_name))
            return

    print("Folder Not Found")

#For Creating Files
def create_file(file_name):

    with open(file_name, "w") as file:
        pass

    print("File Created Successfully")  

#For Creating Folders
def create_folder(folder_name):

    os.makedirs(folder_name, exist_ok=True)

    print("Folder Created Successfully")

#For Deleting Files
def delete_file(file_name):

    if os.path.exists(file_name):

        os.remove(file_name)

        print("File Deleted Successfully")

    else:

        print("File Not Found")

#For Deleting Folders        
def delete_folder(folder_name):

    if os.path.exists(folder_name):

        shutil.rmtree(folder_name)

        print("Folder Deleted Successfully")

    else:

        print("Folder Not Found")

#For Renaming Files 
def rename_file(old_name, new_name):

    if os.path.exists(old_name):

        os.rename(old_name, new_name)

        print("Renamed Successfully")

    else:

        print("File Not Found")

#For Renaming Folders
def rename_folder(old_name, new_name):
    if os.path.exists(old_name):

        os.rename(old_name, new_name)

        print("Renamed Successfully")

    else:

        print("Folder Not Found")

#For Copying Files
def copy_file(source, destination):

    shutil.copy(source, destination)

    print("File Copied Successfully")                     

#For Moving Files
def move_file(source, destination):

    shutil.move(source, destination)

    print("File Moved Successfully")  

#For Listing Files in a Directory
def list_files(path):

    if os.path.exists(path):

        for file in os.listdir(path):

            print(file)

    else:

        print("Folder Not Found")

#For Opening Files
def open_file(file_path):

    if os.path.exists(file_path):

        os.startfile(file_path)

    else:

        print("File Not Found")  


def open_folder(folder_path):

    if os.path.exists(folder_path):

        os.startfile(folder_path)

    else:

        print("Folder Not Found")


#For Zipping the Folder
def zip_folder(folder_path, zip_name):

    shutil.make_archive(zip_name, "zip", folder_path)

    print("ZIP Created Successfully")


#For Unzipping the Folder
def unzip_folder(zip_file, destination):

    with zipfile.ZipFile(zip_file, "r") as zip_ref:

        zip_ref.extractall(destination)

    print("ZIP Extracted Successfully")

    