import pickle
import streamlit as st
import requests
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import os


st.set_page_config(layout="wide")
st.markdown('<span style="color:green">App started</span>', unsafe_allow_html=True)

load_dotenv()

API_KEY = os.getenv("API_KEY")

movies = pickle.load(open('movie_list.pkl','rb'))
st.markdown('<span style="color:green">Movie list loaded</span>', unsafe_allow_html=True)

cv = CountVectorizer(
    max_features=5000,
    stop_words="english"
)

vector = cv.fit_transform(movies["tags"])

# similarity = cosine_similarity(vector)


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"

    try:
        response = requests.get(url)
        # print(response.status_code)
        # print(response.json())      # <-- Add this

        response.raise_for_status()

        data = response.json()
        poster_path = data.get("poster_path")

        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path
        else:
            return None

    except Exception as e:
        # print(e)
        return None


# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movie_names = []
#     recommended_movie_posters = []
#     for i in distances[1:6]:
#         # fetch the movie poster
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         recommended_movie_names.append(movies.iloc[i[0]].title)

#     return recommended_movie_names,recommended_movie_posters

from sklearn.metrics.pairwise import cosine_similarity

def recommend(movie):

    index = movies[movies["title"] == movie].index[0]

    scores = cosine_similarity(
        vector[index:index+1],
        vector
    ).flatten()

    distances = sorted(
        enumerate(scores),
        key=lambda x: x[1],
        reverse=True
    )

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters

st.header('Movie Recommender System')

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    # print(recommended_movie_posters)
    cols = st.columns(5)

    for i, col in enumerate(cols):
        with col:
            st.markdown(
                f"""
                <div style="
                    font-size:18px;
                    font-weight:bold;
                    text-align:center;
                    height:50px;
                    color:red;
                    margin-bottom:10px;
                ">
                    {recommended_movie_names[i]}
                </div>
                """,
                unsafe_allow_html=True
            )
            if recommended_movie_posters[i]:
                st.image(recommended_movie_posters[i])
            else:
                st.write("Poster not available")