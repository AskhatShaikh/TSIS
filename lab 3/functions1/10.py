def unique(lst1):
    lst2 = []
    for item in lst1:
        if item not in lst2:
            lst2.append(item)
    return lst2

lst1 = [1, 2, 2, 3, 4, 5, 5, 7, 7, 8]
print(unique(lst1))