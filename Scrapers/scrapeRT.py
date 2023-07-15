import csv
import requests
from bs4 import BeautifulSoup

URL = "https://editorial.rottentomatoes.com/guide/best-netflix-movies-to-watch-right-now/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.select("h2")

with open("movies.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Score"])

    for idx, movie in enumerate(all_movies):
        title = movie.select_one("a")
        score = movie.select_one(".tMeterScore")
        if title and score:
            writer.writerow([title.getText(), score.getText()])