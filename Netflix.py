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

# ------------
# netflix_solve
# ------------

def netflix_solve(r, w):
    """
    r a reader
    w a writer
    Read a string
    Print that string if it ends in ':', indicating it's a movie ID. 
    Call actual_rating with two strings until reading another movie
    Call netflix_rmse with two lists after reading file
    """
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
    assert s == ""
    netflix_rmse(prediction_list, rating_list)

# ------------
# actual_rating
# ------------

def actual_rating(user, movie):
    """
    user is a string containing a user ID
    movie is a string containing a movie ID
    Add the user's actual rating to a list
    Call netflix_predict with two dictionary values
    """
    assert movie != ""
    assert user != ""
    rating = actual_ratings[movie + " " + user]
    assert rating >= 1 and rating <= 5
    rating_list.append(rating)
    netflix_predict(average_users[user], average_movies[movie]) 

# ------------
# netflix_predict
# ------------

def netflix_predict(user_rating, movie_rating):
    """
    user_rating is a dictionary value containing the average rating for a user
    movie_rating is a dictionary value containing the average rating of a movie
    Augment the extreme values, and average the two values to get a prediction
    Add the prediction to a list
    Print the prediction, a float number
    """
    assert user_rating != ""
    assert movie_rating != ""
    user_rating=float(user_rating)
    movie_rating=float(movie_rating)
    if user_rating < 2.1:
        user_rating -= user_rating * .75
    if user_rating > 3.9:
        user_rating += user_rating / 11
    if movie_rating < 2.1:
        movie_rating -= movie_rating * .75
    if movie_rating > 3.9 :
        movie_rating += movie_rating / 11
    prediction = float((user_rating + movie_rating) / 2)
    prediction = round(prediction, 1)
    prediction_list.append(prediction)
    print(prediction)

# ------------
# netflix_rmse
# ------------

def netflix_rmse(prediction_list, rating_list):
    """
    prediction_list is a list of predicted ratings 
    rating_list is a list of the corresponding actual ratings 
    Print a string and the calculated RMSE, a float value
    """
    assert (len(prediction_list) == len(rating_list))
    print("RMSE:" , format((math.sqrt(sum(map(lambda x, y : (x - y) ** 2, prediction_list, rating_list)) / len(prediction_list))), ".2f"))
