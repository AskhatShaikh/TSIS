#Write a Python program with built in function to multiply all the numbers in a list

def multiply(num):
    result = 1
    for x in num:
        result *=x
    return result

a = [1, 2, 3, 4, 5]  
b=multiply(a)
print(b)