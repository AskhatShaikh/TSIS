#Write a Python program to split a string at uppercase letters.
import re

text = "FkjffJHGghghgGvGhvjggH"

x = re.split('[A-Z]', text)
print(x)
