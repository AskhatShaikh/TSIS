#Write a Python program to insert spaces between words starting with capital letters
import re
def space(x):
    return ' '.join(re.findall('[A-Z][a-z]*', x))

x = "INDINidsmaoidmisdiaimJMos"
y = space(x)
print(y)  