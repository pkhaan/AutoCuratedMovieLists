import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


def scrape_afi():
    url = 'https://www.afi.com/afis-100-years-100-movies-10th-anniversary-edition/'
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML%2C like Gecko) '
                            'Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.62'}
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.text, 'lxml')

    movies = soup.find_all('h6', {'class': 'q_title'})
    movies = [title.text for title in movies]

    detailes = []
    for movie in movies:
        extracted = re.search(r'[0-9]+\.\s(.*)\(([0-9]+)\)', movie)
        detailes.append({
            'title': extracted.group(1),
            'year': extracted.group(2)
        })

    df = pd.DataFrame(detailes)
    return df
