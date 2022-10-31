#WAP for playing Rock Paper Scissors
#Made by Divyansh

import random
name = input('Enter your name here:')
print(f'Welcome back {name}, lets play')
while True:
    user = input("Enter your choice (rock, paper, scissors): ")
    choices = ["rock", "paper", "scissors"]
    Enemy = random.choice(choices)
    print(f"\nYou have chosen {user}, Enemy have chosen {Enemy}.\n")

    if user == Enemy:
        print(f"Both players selected {user}. It's a draw!")
    elif user == "rock":
        if Enemy == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user == "paper":
        if Enemy == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user == "scissors":
        if Enemy == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
