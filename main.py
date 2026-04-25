from game.utils import get_user_choice, get_computer_choice
from game.logic import decide_winner

def menu():
    print("\n===== STONE PAPER SCISSORS =====")
    print("1. Play Game")
    print("2. Exit")

def play():
    user = get_user_choice()
    if not user:
        print("Invalid choice!")
        return

    computer = get_computer_choice()

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    result = decide_winner(user, computer)
    print(f"Result: {result}")

# infinite loop
while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        play()
    elif choice == "2":
        print("Exiting Game...")
        break
    else:
        print("Invalid choice!")