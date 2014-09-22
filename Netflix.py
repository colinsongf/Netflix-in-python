# Netflix.py
import math

dictionary = {}
prediction_list = []
rating_list = []

# Create dictionary with users' average ratings
infile = open("u/prat0318/netflix-tests/savant-cacheUsers.txt", "r")
line = infile.readline().rstrip("\n")
while (line != ""):
    a,b = line.split(" ")
    dictionary[a] = b
    line = infile.readline().rstrip("\n")
infile.close()

# Also add average movie ratings to dictionary
infile = open("u/prat0318/netflix-tests/savant-cacheMovies.txt", "r")
line = infile.readline().rstrip("\n")
while (line != ""):
    a,b = line.split(" ")
    dictionary[a] = b
    line = infile.readline().rstrip("\n")
infile.close()

def predict(user_rating, movie_rating):
    user_rating=float(user_rating)
    movie_rating=float(movie_rating)
    prediction = float((user_rating + movie_rating) / 2)
    prediction = round(prediction, 1)
    prediction_list.append(prediction)

# this is the function that is not working, if you draw out what the loops do, it does not
# really make sense, i think the loops need to be re-organized
def actual_rating(user, movie):
    dic1 = {}
    predict(dictionary[user], dictionary[movie])
    infile = open("u/prat0318/netflix-tests/cct667-ProbeCacheAnswers.txt", "r")
    for line in infile:
        a,b,c = line.split(" ")
        movie_id = a
        customer_id = b
        rating = c     # After changing c to rating, i have changed the rest of the code so it uses the variable rating and not c
        if movie_id in dic1.keys():
            dic1[movie_id][customer_id] = rating
        else:
            dic1[movie_id] = {customer_id:rating}
        if a == movie and b == user:
            rating_list.append(rating)
            return rating
    print()

# original rmse formula
def rmse(prediction_list, rating_list):
    assert (len(prediction_list) == len(rating_list))
    sum = 0
    for i in range(len(prediction_list))
        sum += (prediction_list[i] - rating_list[i]) ** 2
    rmse = math.sqrt(sum / len(prediction_list))
    print(rmse)

#the rmse formula if we implement a linked list, but we need to make sure the lists are accumulating together 
def rmse(prediction_list, rating_list):
    assert (len(prediction_list) == len(rating_list))
    sum = 0
    linked = zip(prediction_list, rating_list)
    for v in linked:
        sum += (v[0] - v[1]) ** 2
    rmse = math.sqrt(sum / len(prediction_list))
    print(rmse)
