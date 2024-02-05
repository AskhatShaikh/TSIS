movie = {
    "name": "Usual Suspects", 
    "imdb": 7.0,
    "category": "Thriller"
}
def above55(movie):
    if movie['imdb'] > 5.5:
        return True
print(above55(movie))