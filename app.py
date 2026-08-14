
import streamlit as st
import pickle
import pandas as pd

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

recommendations = pickle.load(open('recommendations.pkl', 'rb'))


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]

    movie_indices = recommendations[movie_index]

    recommended_movies = []

    for i in movie_indices:
        recommended_movies.append(movies.iloc[i].title)

    return recommended_movies


st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button("Recommend"):
    recommended_movies = recommend(selected_movie)

    st.subheader("Recommended Movies:")

    for movie in recommended_movies:
        st.write("🎥", movie)
