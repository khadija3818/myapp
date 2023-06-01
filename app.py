!pip install streamlit
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

# Button to process data
if st.button("Process"):
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.success("File uploaded and processed successfully!")
    else:
        st.warning("Please upload a CSV file.")
# Display uploaded data
if uploaded_file is not None:
    st.subheader("Uploaded Data")
    st.write(data)

    # Generate a bar plot
    st.subheader("Bar Plot")
    plt.bar(data['x'], data['y'])
    st.pyplot()

