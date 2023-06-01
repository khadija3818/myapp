import streamlit as st

def count_words(text):
    words = text.split()
    return len(words)

# Streamlit app
st.title("Word Count Tool")

# User input for text
text = st.text_area("Enter your text here")

# Count the number of words when the user clicks the "Count" button
if st.button("Count"):
    num_words = count_words(text)
    st.success(f"Number of words: {num_words}")
