import streamlit as st
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    winner = determine_winner(user_choice, computer_choice)

    st.write(f"You chose {user_choice}, and the computer chose {computer_choice}.")
    st.write(winner)

def main():
    st.title("Rock-Paper-Scissors Game")
    st.write("Select your move:")

    user_choice = st.selectbox("", ('rock', 'paper', 'scissors'))

    if st.button("Play"):
        play_game(user_choice)

if __name__ == '__main__':
    main()
