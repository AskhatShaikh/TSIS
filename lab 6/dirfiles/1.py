#Write a Python program to list only directories, files and all directories, files in a specified path.

import os

def list(x):
    print("Directories:")
    for item in os.listdir(x):
        if os.path.isdir(os.path.join(x, item)):
            print(item)

    print("\nFiles:")
    for item in os.listdir(x):
        if os.path.isfile(os.path.join(x, item)):
            print(item)
    
pp=os.path.join(os.getcwd(), "lab6")
list(pp)