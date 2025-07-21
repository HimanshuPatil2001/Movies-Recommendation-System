import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast
import pickle

# Load TMDB dataset
df = pd.read_csv('tmdb_5000_movies.csv')

# Keep only necessary columns
df = df[['id', 'title', 'overview', 'genres', 'keywords']]

# Fill missing values
df['overview'] = df['overview'].fillna('')
df['genres'] = df['genres'].fillna('[]')
df['keywords'] = df['keywords'].fillna('[]')

# Function to parse the JSON-like string from genres/keywords column
def extract_names(text):
    try:
        return [item['name'].replace(" ", "") for item in ast.literal_eval(text)]
    except:
        return []

df['genre_tags'] = df['genres'].apply(extract_names)
df['keyword_tags'] = df['keywords'].apply(extract_names)

# Combine all tags and overview into a single text feature
df['tags'] = df['overview'] + ' ' + df['genre_tags'].apply(lambda x: ' '.join(x)) + ' ' + df['keyword_tags'].apply(lambda x: ' '.join(x))

# Vectorization
vectorizer = CountVectorizer(max_features=5000, stop_words='english')
vectors = vectorizer.fit_transform(df['tags'])

# Similarity calculation
similarity = cosine_similarity(vectors)

# Keep only necessary columns for UI
movie_df = df[['id', 'title', 'overview', 'genre_tags', 'keyword_tags']]
movie_df.rename(columns={'genre_tags': 'genres', 'keyword_tags': 'keywords'}, inplace=True)

# Save
pickle.dump(movie_df, open('movies.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

print("✅ Updated movies.pkl and similarity.pkl generated.")
