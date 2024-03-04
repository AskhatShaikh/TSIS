#Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path

import os

def access(path):
    if os.path.exists(path):
        print(f"{path} is exist")
    else:
        print(f"{path} is gone")
    if os.access(path, os.R_OK):
        print(f"{path} is readability")
    else:
        print(f"{path} is not readability")
    if os.access(path, os.W_OK):
        print(f"{path} is writability")
    else:
        print(f"{path} is not writability")
    if os.access(path, os.X_OK):
        print(f"{path} is executability")
    else:
        print(f"{path} is not executability")

pp=os.path.join(os.getcwd(), "lab6")
pp1=os.path.join(os.getcwd(), r"C:\Users\user\Desktop\PP2s\lab6\DirFiles")
access(pp)
access(pp1)