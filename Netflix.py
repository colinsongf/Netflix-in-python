# Netflix.py
import math
import json

average_users = {}
average_movies = {}
actual_ratings = {}

prediction_list = []
rating_list = []

average_movies = json.load( open('/u/prat0318/netflix-tests/savant-cacheMovies.txt','r') )
average_users = json.load( open('/u/prat0318/netflix-tests/savant-cacheUsers.txt', 'r'))
actual_ratings = json.load( open('/u/prat0318/netflix-tests/savant-cacheActual.txt', 'r'))

def netflix_solve(r, w):
    s = r.readline().rstrip("\n")
    movie = s
    while (s != ""):
        if s[-1] != ':':
            user = s
            actual_rating(user, movie)
        else:
            movie = s.rstrip(':')
            print(s)
        s = r.readline().rstrip("\n")
    rmse(prediction_list, rating_list)

def actual_rating(user, movie):
    rating = actual_ratings[movie + " " + user]
    rating_list.append(rating)
    predict(average_users[user], average_movies[movie]) 

def predict(user_rating, movie_rating):
    user_rating=float(user_rating)
    movie_rating=float(movie_rating)
    prediction = float((user_rating + movie_rating) / 2)
    prediction = round(prediction, 1)
    prediction_list.append(prediction)
    print(prediction)

def rmse(prediction_list, rating_list):
    assert (len(prediction_list) == len(rating_list))
    print("RMSE: " , round((math.sqrt(sum(map(lambda x, y : (x - y) ** 2, prediction_list, rating_list)) / len(prediction_list))), 2))
