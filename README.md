# :camera:Auto Curated Movie Lists 
## In this project we will attempt to instegrate various movie sources and connect them to the **TMDB** api via a frontend web and mobile app using the **Flutter** framework :cd:

### Our Aim
- Identify Movie Websites: Determine the websites that provide the movie titles. These websites should have a consistent structure and accessibility that allows for web scraping. Ensure that you comply with the websites' terms of service and usage policies.
 
- Implement Web Scraping: Develop web scraping scripts or utilize web scraping libraries in a programming language like Python (e.g., Beautiful Soup, Scrapy) to extract movie titles from the identified websites. Retrieve the movie titles by navigating the website's HTML structure and capturing relevant elements.
 
- Define API Integration: Identify a movie information API that provides the additional movie details you require. Ensure that the API offers the necessary endpoints and data fields to retrieve the desired movie information. Review the API documentation and obtain any required access credentials.
 
- Design API Requests: Define the API requests needed to retrieve movie information based on the extracted movie titles. Construct the appropriate API endpoints and include any required parameters or headers. Use the extracted movie titles as inputs in the API requests.
 
- Extract Movie Information from API: Implement the logic to send API requests with the extracted movie titles and retrieve the corresponding movie information in response. Parse and extract the required movie details from the API responses, such as synopsis, release date, genre, director, and other relevant information.
 
- Apply Filters and Parameters: Design and implement the filter and parameter functionality in your web app's user interface. Allow users to input their desired filters, such as genre, release year, rating, etc. Capture the user inputs and incorporate them into the search query for further processing.
 
- On-the-Fly Integration and Processing: Combine the extracted movie titles from web scraping with the retrieved movie information from the API on the fly. Match the movie titles between the scraped data and API responses to associate the relevant movie details with each title. Perform any necessary data transformations or filtering based on the user's input filters.
 
- Generate Search Results: Apply the user's selected filters and parameters to the integrated and processed data. Sort and rank the movies based on relevance or other criteria. Generate the search results, including the movie titles and associated information, such as synopsis, release date, and other details.
 
- Present Results to Users: Display the search results to the users through a user-friendly interface. This can be in the form of a list, grid, or any other suitable format. Consider including pagination or infinite scrolling if there are many search results to display.
 
- Continual Improvement: Regularly monitor the movie websites for changes in structure or accessibility, and adjust the web scraping scripts accordingly. Stay updated with the movie information API's documentation and ensure compatibility with any changes they introduce. Gather user feedback to improve the search functionality and refine the integration process.

### Our Project Structure
1. Scraping
2. API Integration
3. On-the-Fly Integration and Processing
4. Applying Filters and Parameters
5. Using **Flutter** for web integration
   
##### For our scraping sources we used the following cinephile(or not) sites:
- [Library of Congress](https://www.loc.gov/)
- [IMDB](https://www.imdb.com/)
- [Criterion Collection](https://www.criterion.com/)
- [BFI](https://www.bfi.org.uk/)
- [Rotten Tomatoes](https://www.rottentomatoes.com/)    

Using basic `BeautifoulSoup` structure
```python
def scrape_movie_titles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract movie titles from the HTML structure
    titles = soup.find_all('h2', cdlass_='movie-title')
    movie_titles = [title.text for title in titles]
    return movie_titles
```

#### Matching Parameters
Using *Jaccard's* similarity via fuzzy's word token ratio we attempt to eradicate any unwanted duplicate values from our dataset

- Jaccard Similarity for 2 sets:
  $$J(A, B) = \frac {|A \cap B|}{|A \cup B|}$$

and now for three
$$d(i,j) = \frac {b+c}{a+b+c} \implies 1- sim(i,j)$$

we exctract the ratio needed to insinuate that the said value is prevalent against the other one.

```python
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

csv_file1 = 'ScrapedCSVs/top_100_movies.csv'
csv_file2 = 'ScrapeLOC/movies.csv'
csv_file3 = 'ScrapeRottenTomatoes/moviesRT.csv'

# Read each CSV into separate DataFrames
df1 = pd.read_csv(csv_file1)
df2 = pd.read_csv(csv_file2)
df3 = pd.read_csv(csv_file3)

# Function to find fuzzy matches using Jaccard similarity
def fuzzy_match_jaccard(movie_title, titles_list):
    return process.extractOne(movie_title, titles_list, scorer=fuzz.token_sort_ratio)[0]

# Get a list of all movie titles in all three DataFrames
all_movie_titles = df1['Title'].tolist() + df2['Title'].tolist() + df3['Title'].tolist()

# Find fuzzy matches for each DataFrame
df1['Matched_Title'] = df1['Title'].apply(fuzzy_match_jaccard, args=(all_movie_titles,))
df2['Matched_Title'] = df2['Title'].apply(fuzzy_match_jaccard, args=(all_movie_titles,))
df3['Matched_Title'] = df3['Title'].apply(fuzzy_match_jaccard, args=(all_movie_titles,))

# Concatenate the DataFrames based on fuzzy matches
combined_df = pd.concat([df1, df2, df3], ignore_index=True)

# Write the combined DataFrame to a new CSV file
output_csv = 'combined_movies_jaccard.csv'
combined_df.to_csv(output_csv, index=False)

print(f"Jaccard similarity matching completed. The combined data is saved to {output_csv}.")
```

## Flutter Application

### Operating Principle

 The app sends requests and receives responses from the themoviedb API. <br> To learn more about `APIs` and the `Multitier architecture` click <a target="_blank" href="https://en.wikipedia.org/wiki/Multitier_architecture#Web_development_usage">here</a>.
 
<a target="_blank" href="https://volansys.com/wp-content/uploads/2019/07/VOLANSYS_Tiers-of-Architecture-new.jpg"> <img width="350" alt="multitier_architecture" src="https://user-images.githubusercontent.com/61885011/132905821-d68d4792-3f8f-4660-a648-968f353dcb1c.jpg"> </a>

....in this phase we integrate via api calls our .  csv and we try to macth our movie titles with the TMDB database in order to extract our list.

## Dependencies
- `Sizer`: <a target="_blank" href="https://pub.dev/packages/sizer">https://pub.dev/packages/sizer</a>
- `Flutter Spinkit`: <a target="_blank" href="https://pub.dev/packages/flutter_spinkit">https://pub.dev/packages/flutter_spinkit</a>
- `Cached Network Image`: <a target="_blank" href="https://pub.dev/packages/cached_network_image">https://pub.dev/packages/cached_network_image</a>
- `Fluttertoast`: <a target="_blank" href="https://pub.dev/packages/fluttertoast">https://pub.dev/packages/fluttertoast</a>
- `Http`: <a target="_blank" href="https://pub.dev/packages/http">https://pub.dev/packages/http</a>
- `Path Provider`: <a target="_blank" href="https://pub.dev/packages/path_provider">https://pub.dev/packages/path_provider</a>
 
## Getting Started
This application is using api of <a target="_blank" href="https://www.themoviedb.org/">themoviedb</a>, so before using it you have to create an api from <a  target="_blank" href="https://www.themoviedb.org/">themoviedb</a> and generate an API and apply it to this application, follow the below step to connect api with this app.

First go to <a target="_blank" href="https://www.themoviedb.org/documentation/api">https://www.themoviedb.org/documentation/api</a>, and follow the API Documentation, you will get the API Code.

- go to `secret/the_moviedb_api.dart`
- you will see the code like this

```dart
const String themoviedbApi = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX';
```
- replace the all `xx..` to your API, like this

```dart
const String themoviedbApi = 'your_api_token_here';
```



#### Known Bugs`(TODO)`
- Android Emulator doesn't work due to `jvm` error
- Web view needs to be fixed as the project renders mainly to android and iOS devices
- Correct connection with our API and the predisposed API that **flutter** provided.
