#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.

import os

def check(path):
    if os.path.exists(path):
        print(f"{path} is exist")
        if os.path.isfile(path):
            print(f"Filename: {os.path.basename(path)}")
            print(f"Directory portion: {os.path.dirname(path)}")
        elif os.path.isdir(path):
            print(f"Directory: {os.path.basename(path)}")
            print(f"Directory portion: {os.path.dirname(path)}")
    else:
        print(f"{path} I don't know , where is it")
    
if __name__ == "__main__":
    pp=input()
    check(pp)
