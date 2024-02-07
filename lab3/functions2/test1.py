import json

with open("movies.json", "r", encoding="UTF-8") as file:
    data = json.load(file)

def above_5_5(movie):
    return movie["imdb"] > 5.5




print(above_5_5(data[0]))  
# for movie in data:
#     if movie["name"] == "We Two":
#         print(above_5_5(movie))
#         break

