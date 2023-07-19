import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_criterion():
    url = 'https://www.criterion.com/shop/browse/list'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    titles = soup.find_all('td', {'class': 'g-title'})
    years = soup.find_all('td', {'class': 'g-year'})
    movies = []
    for title, year in zip(titles, years):
        movies.append(
            {
                'title': title.text.strip(),
                'year': year.text.strip()
            })

    df = pd.DataFrame(movies)
    return df
