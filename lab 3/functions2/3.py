def category_selector(movies, a):
    category_list = []
    for x in movies:
        if a == x['category']:
            category_list.append(x['name'])
    return category_list
category = category_selector(movies, input("Select category:"))
for x in category:
    print(x)
    