# Task 8: Rock-Paper-Scissors Game

import random

def get_user_choice():
    return input("Enter your choice (rock, paper, scissors): ")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Game loop
user_wins = 0
computer_wins = 0
while user_wins < 3 and computer_wins < 3:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose {user_choice}, computer chose {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

    if result == "You win!":
        user_wins += 1
    elif result == "Computer wins!":
        computer_wins += 1


