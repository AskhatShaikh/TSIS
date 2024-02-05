def average_imdb(movies):
    cnt = 0
    for x in movies:
        cnt += x['imdb']
    cnt = cnt / len(movies)
    return round(cnt,2)
movies = 1
print("Average IMDB:",average_imdb(movies))