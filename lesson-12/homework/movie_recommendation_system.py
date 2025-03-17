import requests
import random

# Replace with your The Movie Database API key
api_key = "YOUR_API_KEY"

# Base URL for The Movie Database API
base_url = "https://api.themoviedb.org/3"

# Function to get a list of genres
def get_genres():
    url = f"{base_url}/genre/movie/list?api_key={api_key}&language=en-US"
    response = requests.get(url)
    genres = response.json()['genres']
    
    genre_dict = {genre['id']: genre['name'] for genre in genres}
    return genre_dict

# Function to get movies by genre
def get_movies_by_genre(genre_id):
    url = f"{base_url}/discover/movie?api_key={api_key}&with_genres={genre_id}"
    response = requests.get(url)
    movies = response.json()['results']
    
    return movies

# Function to recommend a random movie from a selected genre
def recommend_movie():
    genres = get_genres()
    
    # Display genres to the user
    print("Available genres:")
    for genre_id, genre_name in genres.items():
        print(f"{genre_id}: {genre_name}")
    
    # Get user input for genre
    genre_choice = int(input("Enter the genre ID you are interested in: "))
    
    # Fetch movies from the selected genre
    movies = get_movies_by_genre(genre_choice)
    
    if movies:
        random_movie = random.choice(movies)
        title = random_movie['title']
        overview = random_movie['overview']
        release_date = random_movie['release_date']
        
        # Print movie recommendation
        print(f"\nRecommended Movie:\nTitle: {title}\nRelease Date: {release_date}\nOverview: {overview}")
    else:
        print("No movies found for this genre.")

# Run the recommendation system
recommend_movie()