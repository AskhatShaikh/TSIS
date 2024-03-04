#Write a Python program to copy the contents of a file to another file

import shutil
import os

def copy(file, new_file):
    if os.path.isfile(file):
        shutil.copyfile(file, new_file)
        print("The file has been copied successfully!")
    else:
        print("The source file could not be found.")

file = "C:/Users/user/Desktop/PP2s/lab6/DirFiles/7file.txt"
new_file ="C:/Users/user/Desktop/PP2s/lab6/DirFiles/7new_file.txt"
copy(file, new_file)