import json

with open("movies.json", "r", encoding="UTF-8") as file:
    data = json.load(file)

def filter_above_5_5(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

print(filter_above_5_5(data))  
