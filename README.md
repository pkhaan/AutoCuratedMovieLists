# :camera:Auto Curated Movie Lists 
## In this project we will attempt to instegrate various movie sources and connect them to the **TMDB** api via a fronted web and mobile app using the **Flutter** framework :cd:

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




