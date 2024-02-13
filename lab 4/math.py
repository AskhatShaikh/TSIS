"""
#1
Write a Python program to convert degree to radian.
Input degree: 15
Output radian: 0.261904
"""
import math
def convert_to_radian(x):
    radian= x*(3.142848/180)
    print("Output radian:", "{:.6f}".format(radian))

degree=float(input("Input degree: "))
convert_to_radian(degree)

"""
#2
Write a Python program to calculate the area of a trapezoid.
Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5
"""

import math
def area1(h, f, s):
    Area=float((f+s)/2)*h
    print("Expected Output:", Area)

H=int(input("Height: "))
F=int(input("Base, first value: "))
S=int(input("Base, second value: "))
area1(H, F, S)

"""
#3
Write a Python program to calculate the area of regular polygon.
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
"""

import math
def area2(n, l):
    Area=(n*l**2)/(4*math.tan(math.pi/n))
    print("The area of the polygon is:", int(Area))

N = int(input("Input number of sides: "))
L = int(input("Input the length of a side: "))
area2(N, L)

"""
#4
Write a Python program to calculate the area of a parallelogram.
Length of base: 5
Height of parallelogram: 6
Expected Output: 30.0
"""

import math
def area3(b, h):
    Area = b*h
    print("Expected Output:", float(Area))

B = int(input("Length of base: "))
H = int(input("Height of parallelogram: "))
area3(B, H)