#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

import string

for letter in string.ascii_uppercase:
    file_name = f"{letter}.txt"
    with open(file_name, "w") as f:
        f.write(file_name)