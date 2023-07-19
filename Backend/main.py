import requests
import pandas as pd
import os

from dotenv import load_dotenv
from matching import match


def main():
    all_movies = match()

    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + os.getenv('TMDB_API_ACCESS_TOKEN'),
    }

    details = []

    for movie_name in all_movies['title']:

        # For each movie in the list we perform a search on TMDB
        query = movie_name
        search_url = f"https://api.themoviedb.org/3/search/movie?query={query}"
        response = requests.get(search_url, headers=headers)
        search_results = response.json()

        # We assume that the movie we are looking for is the first result
        if len(search_results['results']) == 0:
            continue
        else:
            tmdb_id = search_results['results'][0]['id']

        # We then use the TMDB ID to get the movie details
        movie_url = f"https://api.themoviedb.org/3/movie/{tmdb_id}"
        response = requests.get(movie_url, headers=headers)

        if response.status_code != 200:
            continue
        if response.json()['title'] is None:
            continue

        tmdb_id = response.json()['id']
        title = response.json()['title']
        year = response.json()['release_date'][:4]
        genres = response.json()['genres']

        # We then append the details of each movie to a list
        details.append(
            {
                'tmdb_id': tmdb_id,
                'title': title,
                'year': year,
                'genres': genres
            }
        )

    # And finally we split all the genres into a list and save all info in a dataframe
    for title in details:
        genre_list = []
        for genre in title['genres']:
            genre_list.append(genre['name'])
        title['genres'] = genre_list

    df = pd.DataFrame(details)


if __name__ == '__main__':
    main()
