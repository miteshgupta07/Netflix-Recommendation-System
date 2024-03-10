
# Netflix Recommendation System

Content Based Recommender System recommends movies similar to the movie user likes and analyses the sentiments on the reviews given by the user for that movie.

The details of the movies(title, genre, runtime, rating, poster, etc) are fetched using an API by TMDB, https://www.themoviedb.org/documentation/api, and using the IMDB id of the movie in the API.

I use web scraping to get the reviews given by the user in the IMDB site using beautifulsoup4 and performed sentiment analysis on those reviews.

## Features

- **Content-Based Filtering:** Utilizes content-based filtering techniques to recommend content based on the user's past interactions and content features.
  
- **Personalized Recommendations:** Delivers tailored movie and TV show suggestions by considering the user's historical preferences.
- **User-Friendly Interface:** Incorporates a simple and intuitive interface for users to explore and discover new content.
- **Scalable Architecture:** Designed to scale efficiently with a growing user base and content library.

# Demo

![Screenshot (63)](https://github.com/miteshgupta07/Netflix-Recommendation-System/assets/111682782/a4f7bda0-297e-4de7-bae4-94d4658ae06d)
![Screenshot (64) (2)](https://github.com/miteshgupta07/Netflix-Recommendation-System/assets/111682782/b557c6c4-2793-4ae6-a7b8-db4eaf4afc48)


## Prerequisites
- Python 3.8
- Dependencies List:
  - **Scikit Learn:** A machine learning library in Python.
    - Install: `pip install scikit-learn`
    - Purpose: Utilized for implementing machine learning models and data preprocessing in the project.

  - **Pandas:** A powerful data manipulation and analysis library.
    - Install: `pip install pandas`
    - Purpose: Used for handling and processing structured data.

  - **NumPy:** A fundamental package for scientific computing with Python.
    - Install: `pip install numpy`
    - Purpose: Provides support for large, multi-dimensional arrays and matrices, along with mathematical functions to operate on these arrays.

  - **Matplotlib:** A comprehensive library for creating static, interactive, and animated plots.
    - Install: `pip install matplotlib`
    - Purpose: Essential for generating various types of plots and charts.

  - **tmbdv3api:** An API for interacting with TMDb (The Movie Database) version 3.
    - Install: `pip install tmbdv3api`
    - Purpose: Used for accessing movie-related data and information.

  - **NLTK (Natural Language Toolkit):** A library for working with human language data.
    - Install: `pip install nltk`
    - Purpose: Used for natural language processing tasks such as text tokenization and stemming.

  - **Flask:** A lightweight web application framework.
    - Install: `pip install Flask`
    - Purpose: Used for building web applications and serving the application in a server environment.

  - **Pickle:** A module for serializing and deserializing Python objects.
    - Comes with Python standard library, no separate installation required.
    - Purpose: Used for saving and loading machine learning models or other Python objects.


## Running Flask Tests

```bash
  python app.py
```
    
## Acknowledgements

- **The Movie Database (TMDb):** Gratitude to TMDb for providing a rich source of movie and TV show metadata, enhancing the content-based recommendation system.

- **Scikit-learn:** Gratitude to the Scikit-learn community for creating a powerful machine learning library.
- **Pandas:** Essential for data manipulation and analysis, providing versatile data structures crucial for handling structured data.

- **NumPy:** A fundamental library for scientific computing, enabling efficient operations on large, multi-dimensional arrays and matrices.

- **Matplotlib:** Integral for creating static, animated, and interactive visualizations, making it a cornerstone for data visualization.

- **tmdbsimple (TMDb v3 API):** Simplifies interactions with the TMDb v3 API, facilitating seamless integration of movie-related data into applications.

- **NLTK (Natural Language Toolkit):** Essential for natural language processing tasks, providing easy-to-use interfaces for various language-related operations.

- **Flask:** A lightweight web application framework used for developing web applications and APIs, simplifying HTTP request handling and template rendering.

## Contact
Email : miteshgupta2711@gmail.com

Linkedin : https://www.linkedin.com/in/mitesh-gupta/

Twitter : https://twitter.com/mg_mitesh
