# 📚 Book Recommender System

An intelligent **Content-Based Book Recommendation System** built using **Python, Pandas, Scikit-Learn, Streamlit, and TMDb API**. The application recommends books similar to the selected book by analyzing textual features using **Natural Language Processing (NLP)** and **Cosine Similarity**.

The application is deployed as an interactive web application using **Streamlit**.

---

## Demo

https://book-recommender-system-jmlq.onrender.com/

> **Note:** The application is hosted on Render's free tier. The first request may take a few seconds as the server wakes up.

---

## Features

- Content-Based Recommendation System
- Recommends Top 5 similar books
- Displays Book Posters using TMDb API
- Interactive Streamlit User Interface
- NLP-based Feature Engineering
- Cosine Similarity based Recommendation Engine
- Fast Recommendation using Cached Vectorization
- Responsive Layout

---

## Tech Stack

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Scikit-Learn
- NLTK
- Requests
- Pickle
- Streamlit

### Machine Learning

- Natural Language Processing (NLP)
- Count Vectorization
- Cosine Similarity

### API

- TMDb API (Poster Images)

---

# Project Workflow

```
Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
NLP Preprocessing
      │
      ▼
Count Vectorization
      │
      ▼
Cosine Similarity
      │
      ▼
Recommendation Engine
      │
      ▼
Streamlit Web Application
```

---

# Dataset

The project uses the **TMDB 5000 Movies Dataset**.

The following datasets are used:

- tmdb_5000_movies.csv
- tmdb_5000_credits.csv

The datasets are merged using the **title** column.

---

# Data Preprocessing

The preprocessing pipeline includes:

- Merging movie and credit datasets
- Selecting only useful features
- Removing unnecessary columns
- Handling missing values
- Removing duplicate records
- Extracting genres
- Extracting keywords
- Extracting top 3 cast members
- Extracting director information
- Removing spaces from multi-word names
- Converting overview into tokens
- Combining all important textual features into a single **tags** column

---

# Feature Engineering

The following features are combined:

- Overview
- Genres
- Keywords
- Cast
- Director

Example:

```
Overview +
Genres +
Keywords +
Cast +
Director
        ↓
      Tags
```

---

# Text Preprocessing

The generated **tags** column is processed using:

- Lowercase conversion
- Tokenization
- Porter Stemming
- Stop Word Removal

This improves recommendation quality by reducing redundant words.

---

# Recommendation Algorithm

The recommendation system follows a **Content-Based Filtering** approach.

### Step 1

Convert textual information into numerical vectors using:

- CountVectorizer

Parameters:

```python
CountVectorizer(
    max_features=5000,
    stop_words='english'
)
```

### Step 2

Generate vector representations of every movie.

### Step 3

Compute similarity between movies using:

```
Cosine Similarity
```

### Step 4

Sort movies based on similarity score.

### Step 5

Return Top 5 recommendations.

---

# Application Workflow

1. User selects a movie.
2. Movie is converted into its vector representation.
3. Cosine similarity is calculated.
4. Top 5 similar movies are retrieved.
5. Movie posters are fetched using TMDb API.
6. Recommendations are displayed in the Streamlit application.

---

# Project Structure

```
Book_Recommender_System/

│── app.py
│── movie_list.pkl
│── tmdb_5000_movies.csv
│── tmdb_5000_credits.csv
│── requirements.txt
│── README.md
│── .gitignore
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/dnyaneshwarmagar/book_recommender_system.git
```

Move into the project directory

```bash
cd book_recommender_system
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a **.env** file.

```
API_KEY=YOUR_TMDB_API_KEY
```

Never commit your API key to GitHub.

---

# Running the Application

```bash
streamlit run app.py
```

---

# Future Improvements

- Hybrid Recommendation System
- Collaborative Filtering
- Deep Learning Based Recommendation
- User Login
- Personalized Recommendations
- Search History
- Recently Viewed Movies
- Genre-wise Recommendations
- Trending Movies
- IMDb Ratings Integration

---

# Skills Demonstrated

- Data Cleaning
- Feature Engineering
- NLP
- Count Vectorization
- Cosine Similarity
- Recommendation Systems
- API Integration
- Streamlit
- Python
- Machine Learning
- Data Preprocessing

---

# Acknowledgements

- TMDb API
- TMDB 5000 Movies Dataset
- Scikit-Learn
- Streamlit

---

# Author

**Dnyaneshwar Magar**

GitHub:
https://github.com/dnyaneshwarmagar

LinkedIn:
https://www.linkedin.com/in/dnyaneshm

---

## If you found this project useful, consider giving it a ⭐ on GitHub!