from games.rps import play_rps
from games.dice import roll_dice

while True:
    print("\n--- GAME MENU ---")
    print("1. Stone Paper Scissors")
    print("2. Dice Game")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        play_rps()

    elif choice == "2":
        roll_dice()

    elif choice == "3":
        break

    else:
        print("Invalid choice")