# Movie Recommender System
A movie recommender system which is beginner friendly.
NOTE: Only for non-commercial use!

This project is part of my online MOOC Coursera course - py3 Specialization: Data Collection and Processing with Python , offered by University of Michigan.
This is similar to the one I did in the course.

What this program is about?

This application uses two APIs, Tastedive and OMDB, to gather info about a particular movie and suggest related movies.
The main function takes in one required parameter (movie_name) and an optional parameter (num_of_movies).

API used:

1) Tastedive API
This API returns a JSON response for a particular movie name. The response consists of list of related movies.
This API needs a key in order to fetch the data. So in the script, a valid API key must be entered.

2) OMDB API
This API also returns a JSON response for a partiicular name. However, the response consists of the movie info and its ratings.
This API is used only for getting the rating scores for each movie in the list of related movies acquired from the Tastedive API.
Like Tastedive API, this API also requires a valid key which must be entered in the script.
After getting all the scores and the list of related movies, the list is sorted on the basis of Rotten Tomatoes score in the reverse order.
The sorted list is shown to the user.

Also, this is my first time writing a documentation for a real software project!
Sure enough, this project will have lots of new features to be added as I progress in my software development skills.
Any edits/changes, are always welcome. :)
