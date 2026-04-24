import random

def play_rps():
    options = ["stone", "paper", "scissors"]
    user = input("Enter stone/paper/scissors: ").lower()
    comp = random.choice(options)

    print(f"Computer chose: {comp}")

    if user == comp:
        print("Draw!")
    elif (user == "stone" and comp == "scissors") or \
         (user == "paper" and comp == "stone") or \
         (user == "scissors" and comp == "paper"):
        print("You win!")
    else:
        print("Computer wins!")