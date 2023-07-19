import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


def scrape_loc():
    url = 'https://www.loc.gov/programs/national-film-preservation-board/film-registry/complete-national-film-registry-listing/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    titles = soup.find_all('th', scope='row')

    movies = []

    for title in titles:
        movie_title = title.text.strip()
        movie_year = title.find_next_sibling('td').text.strip()

        if re.match(r'^\d{4}$', movie_year):
            continue

        movies.append({
            'title': movie_title,
            'year': movie_year
        })

        df = pd.DataFrame(movies)
        return df
