from random import choice
print("Welcome to Rock-Paper-Scissors!")
player_choice = str(input("Choose rock, paper, or scissors: "))
print(f"You chose: {player_choice}")
choices = ["rock", "paper", "scissors"]
computer_choice = choice(choices)
print(f"Computer chose: {computer_choice}")
