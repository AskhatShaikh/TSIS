"""
Write a Python program with builtin function that
accepts a string and calculate the number of upper case letters and lower case letters
"""

def counter(string):
    upper = sum(1 for char in string if char.isupper())
    lower = sum(1 for char in string if char.islower())
    return upper, lower

string = str(input())
upper , lower = counter(string)
print(f"number of Upper case letter: {upper}")
print(f"number of lower case letter: {lower}")