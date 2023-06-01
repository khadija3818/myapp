import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load the movie ratings data
ratings_data = pd.read_csv('ratings.csv')

# Load the movie metadata
movies_metadata = pd.read_csv('movies.csv')

# Create a pivot table of user ratings
user_ratings = ratings_data.pivot_table(index='userId', columns='movieId', values='rating')

# Calculate item-item similarity using cosine similarity
item_similarity = cosine_similarity(user_ratings.fillna(0))

# Streamlit app
st.title('Movie Recommendation System')

# User input for movie selection
selected_movie = st.selectbox('Select a movie:', movies_metadata['title'].values)

# Get the index of the selected movie
selected_movie_index = movies_metadata[movies_metadata['title'] == selected_movie].index[0]

# Get similar movies based on item-item similarity
similar_movies = list(enumerate(item_similarity[selected_movie_index]))

# Sort similar movies by similarity score
sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)

# Display recommended movies
st.subheader('Recommended Movies:')

for i in range(5):
    movie_index = sorted_similar_movies[i][0]
    recommended_movie = movies_metadata.iloc[movie_index]['title']
    st.write(f'{i+1}. {recommended_movie}')
