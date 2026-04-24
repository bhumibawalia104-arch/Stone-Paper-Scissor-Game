import random

def roll_dice():
    user = random.randint(1, 6)
    comp = random.randint(1, 6)

    print(f"You rolled: {user}")
    print(f"Computer rolled: {comp}")

    if user > comp:
        print("You win!")
    elif user < comp:
        print("Computer wins!")
    else:
        print("Draw!")
    