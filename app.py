from flask import Flask, request, render_template
import pickle
import pandas as pd
import requests
import json

app = Flask(__name__)

# TMDb API Key
TMDB_API_KEY = "0544145f300ef6e02b4dff2213c2eaff"

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movie_titles = movies['title'].tolist()

# 🔍 Fetch details from TMDb
def fetch_movie_details(title):
    try:
        search_url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={title}"
        response = requests.get(search_url)
        data = response.json()

        if data['results']:
            movie = data['results'][0]
            movie_id = movie.get('id')

            detail_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
            detail_resp = requests.get(detail_url).json()

            genres = [g['name'] for g in detail_resp.get('genres', [])]

            return {
                'title': movie.get('title'),
                'poster': f"https://image.tmdb.org/t/p/w500{movie.get('poster_path')}" if movie.get('poster_path') else None,
                'overview': movie.get('overview'),
                'rating': movie.get('vote_average'),
                'votes': movie.get('vote_count'),
                'release_year': movie.get('release_date', '')[:4] if movie.get('release_date') else 'N/A',
                'tmdb_url': f"https://www.themoviedb.org/movie/{movie_id}",
                'genres': ", ".join(genres) if genres else "N/A"
            }
        return None
    except:
        return None

# 🏠 Home Route
@app.route('/')
def index():
    with open('top_movies.json') as f:
        top_movies = json.load(f)

    results = []
    for movie in top_movies:
        details = fetch_movie_details(movie['title'])
        if details:
            results.append(details)

    return render_template('index.html', movie_titles=movie_titles, movies=results)

# 🔥 Top 100 route
@app.route('/top')
def top_movies():
    with open('top_movies.json') as f:
        top_movies = json.load(f)

    results = []
    for movie in top_movies:
        details = fetch_movie_details(movie['title'])
        if details:
            results.append(details)

    return render_template('top.html', movies=results)

# 🔁 Recommend Route
@app.route('/recommend', methods=['POST'])
def recommend():
    movie = request.form['movie']

    if movie not in movies['title'].values:
        return f"<h3>Movie '{movie}' not found.</h3><a href='/'>Try again</a>"

    index = movies[movies['title'] == movie].index[0]
    distances = list(enumerate(similarity[index]))
    sorted_movies = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]

    rec_data = []
    for i in sorted_movies:
        details = fetch_movie_details(movies.iloc[i[0]].title)
        if details:
            rec_data.append(details)

    return render_template('recommend.html', movie=movie, recs=rec_data)

# 🚀 Run
if __name__ == '__main__':
    app.run(debug=True)
