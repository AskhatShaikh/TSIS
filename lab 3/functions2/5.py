def category_imdb(movies, a):
    cnt = 0
    lencnt = 0
    for x in movies:
        if a == x['category']:
            cnt += x['imdb']
            lencnt += 1
    cnt = cnt / lencnt
    return round(cnt,2)
a = input("Select category")
print("Average IMDB:",category_imdb(movies, a) )
        