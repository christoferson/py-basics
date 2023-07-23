import random

# Rock Paper Scissors

choices = ["Rock", "Paper", "Scissor"]

choice = input("Rock(0) Paper(1) Scissors(2): ")

choice_player = int(choice) % 3
choice_computer = random.randint(0, 2)

print(f"Player: {choices[choice_player]} Computer: {choices[choice_computer]}")

if choice_player == 0:
    if choice_computer == 0:
        print("Tie. Both Rock")
    elif choice_computer == 1:
        print("Lose")
    elif choice_computer == 2:
        print("Win")
elif choice_player == 1:
    if choice_computer == 0:
        print("Win")
    elif choice_computer == 1:
        print("Tie. Paper")
    elif choice_computer == 2:
        print("Lose")
else:
    if choice_computer == 0:
        print("Lose")
    elif choice_computer == 1:
        print("Win")
    elif choice_computer == 2:
        print("Tie. Scissors")