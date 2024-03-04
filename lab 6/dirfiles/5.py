#Write a Python program to write a list to a file.

list = ['Joel', 'Sara', 'Tommy', 'Ellie', 'Dina', 'Tess']

file_name=input("Enter your file name:")

with open(file_name, "w") as f:
    for x in list:
        f.write(x + "\n")

print("List has been written to", file_name)