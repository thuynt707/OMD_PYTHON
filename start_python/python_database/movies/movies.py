import sys
from db import get_movies, get_actors, find_movie


def print_all_movies():
    movies = get_movies()
    for movie in movies:
        print(movie('id'), movie('title'), movie('year'))

    file = open('movies.txt', 'w', encoding='utf-8')
    for movie in movies:
        file.write(f"{movie['id']}")

def print_all_actors():
    actors = get_movies()
    for actor in actors:
        print(actor('id'), actor('name'))


def print_movie_info():
    print("Nhập movie id: ")
    movie_id = input("> ")
    movie, actors = find_movie(movie_id)

    if not movie:
        print("movie not found")
    else
        print("Movie info: ")
        print(movie('title'), movie('year'))

        print("Actor info: ")
        print(actors('name'))

def add_movie():
    print ("Nhap ten phim")
    title = input()
    print ("Nhap nam phat hanh")
    year = input()

    add_movie(title, year)

def quit():
    print("Have fun")
    sys.exit()
