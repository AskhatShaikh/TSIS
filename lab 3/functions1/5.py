from itertools import permutations as perm_func

def permutations(string):
    perms = [''.join(p) for p in perm_func(string)]
    return perms

input_string = input("Enter a string: ")
print("Permutations of the string:", permutations(input_string))

