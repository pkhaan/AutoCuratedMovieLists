import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_bfi():
    url = 'https://www.bfi.org.uk/sight-and-sound/greatest-films-all-time'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    div = soup.find('div', class_='ResultsPage__ResultGrid-sc-of10co-0 igHJEb')
    titles = div.find_all('h1')

    df = pd.DataFrame(titles, columns=['title'])
    df['year'] = ""
    return df
