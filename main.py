import random


def get_choice():
    player_choice = input("Enter your choice(rock,paper,scissors)")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"Player choice {player} and computer choice{computer}")
    if player == computer:
        return "It's tie!"
    elif player == "rock":
        if computer == "scissors":
            return "You Win!"
        else:
            return "You lose!"
    elif player == "paper":
        if computer == "rock":
            return "You Win!"
        else:
            return "You lose!"
    elif player == "scissors":
        if computer == "paper":
            return "You Win!"
        else:
            return "You Lose"


choices = get_choice()
result = check_win(choices["player"], choices["computer"])
print(result)
