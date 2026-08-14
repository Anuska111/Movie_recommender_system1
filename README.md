# 🎬 Movie Recommender System

A Content-Based Movie Recommender System built using Python, Pandas, Scikit-learn, and Streamlit.

## 📌 Project Overview

This project recommends movies similar to the movie selected by the user. It uses movie information such as genres, keywords, cast, crew, and overview to identify similar movies.

The project follows a content-based recommendation approach using CountVectorizer and Cosine Similarity.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle
- Google Colab / Jupyter Notebook

## 📊 Dataset

The project uses the TMDB 5000 Movies Dataset and TMDB 5000 Credits Dataset.

The datasets contain information such as:

- Movie Title
- Genres
- Keywords
- Cast
- Crew
- Overview

## ⚙️ Working Process

1. Movie and credits datasets are merged.
2. Relevant movie information is extracted.
3. Genres, keywords, cast, crew, and overview are combined into a `tags` feature.
4. CountVectorizer converts the text-based tags into numerical vectors.
5. Cosine Similarity is used to identify similar movies.
6. The top 5 recommendations for each movie are precomputed and stored in `recommendations.pkl`.
7. A Streamlit application provides an interactive movie recommendation interface.

## 🎯 Features

- 🎬 Select a movie from the dropdown
- 🤖 Get 5 similar movie recommendations
- ⚡ Fast recommendation using precomputed results
- 🖥️ Interactive Streamlit interface
- 📱 Easy to deploy online

## 📁 Project Structure

Movie-Recommender-System/
│
├── app.py
├── requirements.txt
├── movie_dict.pkl
├── recommendations.pkl
├── Movie_recommender_system.ipynb
└── README.md

## 🚀 Run Locally

Clone the repository:

    git clone YOUR_GITHUB_REPOSITORY_URL

Install the required libraries:

    pip install -r requirements.txt

Run the Streamlit application:

    streamlit run app.py

## 🌐 Deployment

The application can be deployed using Streamlit Community Cloud by connecting this GitHub repository.

Main application file:

    app.py
## 🌐 Live Demo

🚀 **Streamlit App:** [Click here to try the Movie Recommender System](https://movierecommendersystem1-rcrpduvvkkqxdccn2uzbzk.streamlit.app/)

## 🔮 Future Improvements

- Add movie posters using the TMDB API
- Display movie ratings and release dates
- Add detailed movie information
- Improve the user interface
- Add personalized recommendations
- Deploy the application online

## 👩‍💻 Author

Anuska Biswas

B.Tech – Mechanical Engineering  
IIT (BHU) Varanasi

⭐ If you like this project, consider giving the repository a star!
