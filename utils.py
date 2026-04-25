import random

def get_user_choice():
    print("\nChoose:")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissors")

    choice = input("Enter choice: ")
    choices = {"1": "Stone", "2": "Paper", "3": "Scissors"}

    return choices.get(choice, None)

def get_computer_choice():
    return random.choice(["Stone", "Paper", "Scissors"])