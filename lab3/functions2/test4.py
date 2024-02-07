import json

with open("movies.json", "r", encoding="UTF-8") as file:
    data = json.load(file)

def average_imdb_score(movies):
    if not movies:
        return 0
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)

if __name__ == "__main__":
    print(average_imdb_score(data)) 