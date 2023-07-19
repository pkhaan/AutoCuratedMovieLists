import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


def scrape_tspdt():
    url = 'https://www.theyshootpictures.com/gf1000_all1000films.htm'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    movies = soup.find('div', id='stacks_in_1784')

    movie_list = movies.find_all('span')[1:2][0]

    for br in movie_list.find_all("br"):
        br.replace_with("\n")

    movie_list_list = list(filter(None, movie_list.text.split("\n")))

    details = []
    for movie in movie_list_list:
        movie_name = re.search(r'(.*)\)(.*)\((.*),\s([0-9]+)', movie)
        details.append(
            {'title:': movie_name.group(2),
             'year:': movie_name.group(4)
             }
        )

    df = pd.DataFrame(details)
    return df
