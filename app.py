!pip install streamlit
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
def main():
    st.title("Data Visualization Web App")

    # File uploader
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        columns = df.columns.tolist()

        # Select box for choosing the column
        selected_column = st.selectbox("Select a column", columns)

        if st.button("Plot"):
            # Plotting the selected column as a line chart
            plt.plot(df[selected_column])
            plt.xlabel("Index")
            plt.ylabel(selected_column)
            st.pyplot(plt)

if __name__ == "__main__":
    main()
