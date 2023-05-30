import streamlit as st
import string
import random

def generate_password(length, include_digits, include_letters, include_special_chars):
    characters = ""

    if include_digits:
        characters += string.digits
    if include_letters:
        characters += string.ascii_letters
    if include_special_chars:
        characters += string.punctuation

    if not characters:
        st.error("Please select at least one character type.")
        return ""

    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    st.title("Password Generator")
    st.write("Customize and generate a secure password.")

    # Password length
    length = st.slider("Password Length", min_value=6, max_value=30, step=1, value=12)

    # Character types
    include_digits = st.checkbox("Include Digits")
    include_letters = st.checkbox("Include Letters")
    include_special_chars = st.checkbox("Include Special Characters")

    if st.button("Generate Password"):
        password = generate_password(length, include_digits, include_letters, include_special_chars)
        st.success("Generated Password:")
        st.text(password)

if __name__ == "__main__":
    main()
