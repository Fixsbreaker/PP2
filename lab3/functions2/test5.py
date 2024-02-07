import json
from test4 import average_imdb_score
from test3 import movies_by_category

with open("movies.json", "r", encoding="UTF-8") as file:
    data = json.load(file)

def average_imdb_score_by_category(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb_score(category_movies)

print(average_imdb_score_by_category(data, 'Suspense'))
