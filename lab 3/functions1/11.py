def palindrome(string):
    s = []
    b = []
    for x in range(len(string)//2):
        s.append(string[x])
    for x in range(len(string//2), len(string)):
        b.append(string[x])
    if s == b[::-1]:
        return print("It is palindrome!")
    else:
        return print("It isnt palindrome")
    
string = input()
palindrome(string)