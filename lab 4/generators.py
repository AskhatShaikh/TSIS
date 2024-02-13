"""
#1
Create a generator that generates the squares of numbers up to some number N.
"""

class Square:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.n:
            result = self.current **2
            self.current +=1
            return result
        else:
            raise StopIteration
        
N = int(input())
squares = Square(N)
for x in squares:
    print(x)

"""
#2
Write a program using generator to print the even numbers between 0 and n 
in comma separated form where n is input from console.
"""  

class Even:
    def __init__(self, n):
        self.n = n 
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.n:
            result = self.current
            self.current +=2
            return result
        else:
            raise StopIteration
        
N=int(input())
Evennumbers=Even(N)
Even_nustr=(str(x) for x in Evennumbers)
result_str= ", ".join(Even_nustr)
print(result_str)

"""
#3
Define a function with a generator which can iterate the numbers, 
which are divisible by 3 and 4, between a given range 0 and n.
"""

def Div(n):
    current =0
    while current <=n:
        if current %3 == 0 and current %4 ==0:
            yield current
        current +=1

N=int(input())
numbers=Div(N)
numbers_str=(str(x) for x in numbers)
result_str=", ".join(numbers_str)
print(result_str)
        
"""
#4
Implement a generator called squares to yield the square of all numbers from (a) to (b). 
Test it with a "for" loop and print each of the yielded values.
"""

def squares(a, b):
    current =a
    while  current <=b :
        yield current**2
        current +=1

a = int(input())
b = int(input())
numbers=squares(a, b)
for x in numbers:
    print(x)
        
"""
#5
Implement a generator that returns all numbers from (n) down to 0.
"""

def zero(n):
    current = n
    while current >=0:
        yield current 
        current-=1

N = int(input())
numbers=zero(N)
for x in numbers:
    print(x)