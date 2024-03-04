'''
Write a Python program that invoke square root function after specific milliseconds.
Sample Input:
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858
'''

import time
import math

def square(number, milliseconds):
    time.sleep(milliseconds/1000)
    square_root= math.sqrt(number)
    return square_root

number= 25100
milliseconds = 2123
result = square(number, milliseconds)
print(f"Square root of {number} after {milliseconds} miliseconds is {result}")