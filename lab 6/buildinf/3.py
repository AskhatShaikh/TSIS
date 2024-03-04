#Write a Python program with built in function that checks whether a passed string is palindrome or not.

def check(a):
    for i in range(len(a)//2):
        if a[i]!=a[-i-1]:
            return False
    return True

r = input()
print(check(r))