# 🎬 Movie Recommender System

Welcome to the **Movie Recommender System** — an intelligent web app that helps users discover movies they might love based on their input, using content-based filtering. Built with Python, Flask, and JavaScript, this project integrates machine learning and a live movie API to deliver a seamless recommendation experience.

---

## 🚀 Features

- 🔍 **Search and Get Recommendations** — Enter a movie title and get similar movie suggestions.
- 🧠 **Content-Based Filtering** — Uses cosine similarity on feature-engineered movie metadata.
- 🖼️ **Posters, Ratings, and Info** — Movie data is fetched live from **The Movie Database (TMDb) API**.
- 🌐 **Single Page Experience** — Smooth scrolling and movie loading with JavaScript lazy loading.
- 📦 **Top 100 Movies JSON** — Precomputed list of top-rated movies with genre, year, rating, and vote info.
- 🔧 **Modular Design** — Clean separation of backend logic (`Flask`) and frontend rendering (`HTML/CSS/JS`).

---

## 🧠 ML Logic Behind Recommendations

We used a **content-based filtering** technique where each movie is represented by a set of textual features (title, genres, keywords, overview, cast, director). The key steps include:

1. **Data Cleaning & Feature Engineering**:
   - Combined `genres`, `keywords`, `cast`, `crew`, and `overview` into a unified "tag" column.
   - Removed duplicates, handled missing values, and standardized text.

2. **Vectorization**:
   - Used **CountVectorizer** to convert text tags into numerical vectors.

3. **Similarity Calculation**:
   - Applied **Cosine Similarity** to compute distances between movie vectors.

4. **Model Enhancement**:
   - Initial version used only `overview`. Later improvements included `cast`, `crew`, `keywords`, and `genres` — increasing the recommendation quality.
   - Stored `movies.pkl` and `similarity.pkl` for quick runtime performance.

---

## 🔗 TMDb API Integration

To enhance the UI with real movie posters, metadata, and descriptions, we integrated:

📡 **The Movie Database API (TMDb)**  
- Used to fetch:
  - 🎞️ Poster images  
  - 🌟 Ratings and vote counts  
  - 📅 Release years  
  - 📖 Overviews

Each recommended movie fetches live details via a dedicated API call using the TMDb movie ID.

---

## 📂 Project Structure

```
recommendation/
│
├── app.py                  # Flask backend
├── templates/
│   └── index.html          # Main page template
├── static/
│   └── styles.css          # Custom styles
├── movies.pkl              # Serialized movie DataFrame
├── similarity.pkl          # Cosine similarity matrix
├── top_movies.json         # Top 100 movies for lazy loading
├── .gitignore              # Ignoring heavy files and virtual env
└── requirements.txt        # Python dependencies
```

---

## 🧪 How to Run Locally

1. 📦 Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. 🏃‍♂️ Run the app:
   ```bash
   python app.py
   ```

3. 🌐 Visit:
   ```
   http://localhost:5000/
   ```

---

## 💡 Future Improvements

- 🔍 Add collaborative filtering with user-based behavior (using MovieLens dataset).
- 🗣️ Add NLP-based description embedding (TF-IDF or BERT).
- 📱 Make the app responsive for mobile.
- 🧾 Add user login & save favorites.

---

## 🙌 Final Note

This project is built with real-world practices — clean UI, lazy loading, pre-processed data, and API integration — making it **interview-ready** and showcasing proficiency in:
- Python 🐍
- Flask 🌶️
- Machine Learning 🤖
- JavaScript 💻
- API Integration 🔗

If you like the project or want to suggest improvements, feel free to fork and star ⭐ the repo!

---

### 🧠 Powered By:
- [TMDb API](https://www.themoviedb.org/)
- [scikit-learn](https://scikit-learn.org/)
- [Pandas](https://pandas.pydata.org/)
