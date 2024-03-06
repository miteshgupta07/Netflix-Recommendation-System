# Required Libraries
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import bs4 as bs
import urllib.request
import pickle
import requests
import json

# Load the nlp model and tfidf vectorizer from disk
nlp_model = pickle.load(open("nlp_model.pkl", 'rb'))
vectorizer = pickle.load(open("transform.pkl", 'rb'))

def create_similarity():
    data = pd.read_csv('Netflix Recommendation System\\Processed Datasets\\main_data.csv')
    # Creating a count matrix
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data['comb'])
    # Creating a similarity score matrix
    similarity = cosine_similarity(count_matrix)
    return data, similarity

def rcmd(title, data, similarity):
    title = title.lower()
    try:
        data.head()
        similarity.shape
    except NameError:
        data, similarity = create_similarity()

    titles=pd.Series(data['movie_title'])


    if title not in data['movie_title'].unique():
        return 'Sorry! try another movie name'
    else:
        recommend_movies=[]
    recommend=[]
    title=title.lower()
    idx=titles[titles==title].index[0] # getting the index of movie that matches the title
    score_series=pd.Series(similarity[idx]).sort_values(ascending=False) # creating a series with the similarity scores in descending order
    top_10_indexes=list(score_series.iloc[1:11].index) # getting the indexes of the 10 most similar movies
    for i in top_10_indexes:
      recommend_movies.append(list(data['movie_title'])[i])

    return recommend_movies

# Converting list of string to list (e.g., "["abc","def"]" to ["abc","def"])
def convert_to_list(my_list):
    return json.loads(my_list)

# To get suggestions of movies
def get_suggestions():
    data = pd.read_csv('Netflix Recommendation System\\Processed Datasets\\main_data.csv')
    return list(data['movie_title'].str.capitalize())

# Flask API
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    suggestions = get_suggestions()
    return render_template('home.html', suggestions=suggestions)

@app.route("/similarity", methods=["POST"])
def similarity():
    movie = request.form['name']
    data, similarity = create_similarity()
    rc = rcmd(movie, data, similarity)
    return rc if isinstance(rc, str) else '---'.join(rc)

@app.route("/recommend", methods=["POST"])
def recommend():
    # Getting data from AJAX request
    title = request.form['title']
    cast_ids = convert_to_list(request.form['cast_ids'])
    cast_names = convert_to_list(request.form['cast_names'])
    cast_chars = convert_to_list(request.form['cast_chars'])
    cast_bdays = convert_to_list(request.form['cast_bdays'])
    cast_bios = convert_to_list(request.form['cast_bios'])
    cast_places = convert_to_list(request.form['cast_places'])
    cast_profiles = convert_to_list(request.form['cast_profiles'])
    imdb_id = request.form['imdb_id']
    poster = request.form['poster']
    genres = request.form['genres']
    overview = request.form['overview']
    vote_average = request.form['rating']
    vote_count = request.form['vote_count']
    release_date = request.form['release_date']
    runtime = request.form['runtime']
    status = request.form['status']
    rec_movies = convert_to_list(request.form['rec_movies'])
    rec_posters = convert_to_list(request.form['rec_posters'])

    # Get movie suggestions for autocomplete
    suggestions = get_suggestions()

    # Rendering the string to Python string
    for i in range(len(cast_bios)):
        cast_bios[i] = cast_bios[i].replace(r'\\n', '\\n').replace(r'\\"', '\\"')

    # Combining multiple lists as a dictionary
    movie_cards = {rec_posters[i]: rec_movies[i] for i in range(len(rec_posters))}
    casts = {cast_names[i]: [cast_ids[i], cast_chars[i], cast_profiles[i]] for i in range(len(cast_profiles))}
    cast_details = {cast_names[i]: [cast_ids[i], cast_profiles[i], cast_bdays[i], cast_places[i], cast_bios[i]] for i in range(len(cast_places))}

    # Web scraping to get user reviews from IMDB site
    sauce = urllib.request.urlopen('https://www.imdb.com/title/{}/reviews?ref_=tt_ov_rt'.format(imdb_id)).read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    soup_result = soup.find_all("div", {"class": "text show-more__control"})

    reviews_list = []  # List of reviews
    reviews_status = []  # List of comments (good or bad)
    for reviews in soup_result:
        if reviews.string:
            reviews_list.append(reviews.string)
            # Passing the review to our model
            movie_review_list = np.array([reviews.string])
            movie_vector = vectorizer.transform(movie_review_list)
            pred = nlp_model.predict(movie_vector)
            reviews_status.append('Good' if pred else 'Bad')

    # Combining reviews and comments into a dictionary
    movie_reviews = {reviews_list[i]: reviews_status[i] for i in range(len(reviews_list))}

    # Passing all the data to the HTML file
    return render_template('recommend.html', title=title, poster=poster, overview=overview, vote_average=vote_average,
                           vote_count=vote_count, release_date=release_date, runtime=runtime, status=status, genres=genres,
                           movie_cards=movie_cards, reviews=movie_reviews, casts=casts, cast_details=cast_details)

if __name__ == '__main__':
    app.run(debug=True)
