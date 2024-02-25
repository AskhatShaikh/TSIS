#Write a python program to convert snake case string to camel case string.
import re
def snake_camel(s):
    res = ''
    res += (s.group(1)).upper()
    return res

str = input()
camel = re.sub(r'(_[a-z])', snake_camel, str)
camel = camel.replace('_', '')
print(camel)