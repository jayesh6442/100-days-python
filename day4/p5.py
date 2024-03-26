import random

print("Let's play Rock-Paper-Scissors!")
player_choice = input("Choose rock, paper, or scissors: ").lower()

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)

print(f"You chose {player_choice}, and the computer chose {computer_choice}.")

if player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == "rock" and computer_choice == "scissors") or \
     (player_choice == "paper" and computer_choice == "rock") or \
     (player_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("Computer wins!")