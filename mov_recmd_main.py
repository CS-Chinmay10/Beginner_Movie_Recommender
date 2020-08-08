# Movie recommender system
"""This recommender system uses Tastedive API and OMDB API to arrange the movie details and their info.
Tastedive API provides a JSON response which consists the related movies' titles.
Using the OMDB API, it provides a response also in JSON consisting info about a movie and its ratings"""

import requests , json

# Get data from Tastedive API
def get_movie_data(movie_name , movies_limit = "5"):
    baseurl = "https://tastedive.com/api/similar"
    param_diction = {}
    """Initiate the query params for the url"""
    param_diction["q"] = movie_name
    param_diction["type"] = "movies"
    param_diction["k"] = "yourkeyhere"      # If you have Tastedive API key, then insert here
    param_diction["limit"] = movies_limit
    response = requests.get(baseurl , params = param_diction)
    return json.loads(response.text)

# Extract movie titles from the dict
def extract_movie_titles(movie_dict):
    """The dictionary consists of JSON data"""
    results = movie_dict["Similar"]["Results"]  # A list containing all related movie details
    return [result["Name"] for result in results]

# Get JSON data from OMDB API
def get_movie_info(movie_name):
    baseurl = "http://www.omdbapi.com/"
    param_diction = {}
    param_diction["t"] = movie_name
    param_diction["type"] = "movie"
    param_diction["r"] = "json"
    param_diction["plot"] = "short"
    param_diction["apikey"] = "yourkeyhere"     # An OMDB API key is required! Put your key here
    response = requests.get(baseurl , params = param_diction)
    return json.loads(response.text)

# Extract Rotten Tomatoes score from the OMDB data
def get_rotten_score(movie_dict):
    ratings = movie_dict["Ratings"]     # Returns a list containing ratings from different websites
    for rating in ratings:
        if "Rotten Tomatoes" != rating["Source"]:
            continue
        score = int(rating["Value"].strip("%"))
        return score

# Sort the recommended movies list based on their score
def sort_movie_list(movie_list):
    sorted_lst = sorted(movie_list , key = lambda x: get_rotten_score(get_movie_info(x)) , reverse = True)
    return sorted_lst


# Show the results to the user
def main():
    get_movie_name = input("Enter a movie name: ")
    num_of_movies = input("How many movies do you want? (default : 5 , max = 20): ")
    print("\n")
    movie_lst = sort_movie_list(extract_movie_titles(get_movie_data(get_movie_name , num_of_movies)))
    print("You requested for the movie," , get_movie_name , "\n")
    print(" ** ** " * 10 , "\n")
    print("Here are the recommended movies related to your search:" , "\n")
    for i in range(len(movie_lst)):
        print(str(i + 1) + ")  " + movie_lst[i] + "\n")

main()