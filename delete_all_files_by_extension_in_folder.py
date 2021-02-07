import os
from pathlib import Path

print("Delete all files in folder by the extension")

basePath = input("Enter directory path: ")
isNotFound = True # if any file is deleted or not

if os.path.isdir(basePath) == False:
    print("Path is not correct! Quiting ...")
    quit()

extensionToDelete = input("What's the extension: ")
extensionToDelete = f".{extensionToDelete}"

for root, dirs, files in os.walk(basePath, topdown=False):
    for name in files:
        ext = Path(name).suffix
        if ext == extensionToDelete:
            isNotFound = False
            absolutePath = os.path.join(root, name) # absolute path for file deleting
            relativePath = os.path.relpath(absolutePath, basePath) # relative path for printing
            print("Deleteing:", relativePath)
            try:
                os.remove(absolutePath)
            except:
                print("Error deleting file: ", relativePath)

if isNotFound:
    print(f"No {extensionToDelete} file found")
