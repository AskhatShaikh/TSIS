import re

x = "AShgbdgvdhShgvwhdcfHGdfghjGfghj"

h = re.findall("[A-Z][a-z]+" ,x)
print(h)