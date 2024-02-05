

def above_5_5_movies(movie):
    above55_list = []
    for x in movie:
        if x['imdb'] > 5.5:
            above55_list.append(x['name'])
    return above55_list
above5_5 = above_5_5_movies(movie)
for x in above5_5:
    print(x)

