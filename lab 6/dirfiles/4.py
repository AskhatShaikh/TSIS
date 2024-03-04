#Write a Python program to count the number of lines in a text file.

file = open('demofile.txt', 'r')

lines =0
for line in file:
    lines+=1

print(lines)