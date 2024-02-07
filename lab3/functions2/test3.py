import json

with open("movies.json", "r", encoding="UTF-8") as file:
    data = json.load(file)

def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

if __name__ == "__main__":
    print(movies_by_category(data, "Romance"))  