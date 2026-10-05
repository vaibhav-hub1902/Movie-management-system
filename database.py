movies = []

def insert_movie(name,director,year,genre,rateing):

    movie = {'name' : name,'director' : director,'year' :year ,'genre' :genre,'rateing':rateing}
    movies.append(movie)

    print("Movie added successfully")

def show_all_movies():
    return movies

def search_movies(name):

    for movie in movies:

        if movie['name'] == name:
            return movie

    return None

def delete_movie(name):

    for movie in movies:

        if movie["name"] == name:
            movies.remove(movie)
        else:
            print("movie not found")

def update_movie_rateing(name,new_rateing):

    movie = search_movies(name)

    if movie:
        movie["rateing"] = new_rateing
        print("movie rateing updated")
    else:
        print("movie not found")