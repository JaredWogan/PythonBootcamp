import getpass
import numpy.random as npr

print("Welcome to Rock, Paper, Scissors!")
p1 = input("Please enter player 1's name: ")
p2 = input("Please enter player 2's name: ")

bot = p2.lower() == "bot"

print("\n")
print("Let's play!")
print("\n")

options = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

outcomes = {
    (1,1): "Tie",
    (1,2): f"{p2} wins",
    (2,1): f"{p1} wins",
    (2,2): "Tie",
    (3,1): f"{p2} wins",
    (3,2): f"{p1} wins",
    (1,3): f"{p1} wins",
    (2,3): f"{p2} wins",
    (3,3): "Tie"
}

keep_playing = True
while keep_playing:
    print("Rock, Paper, Scissors")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("\n")

    choice1 = 0
    while choice1 not in (1,2,3):
        choice1 = int(getpass.getpass(f"Please select your choice {p1}: "))

    print(f"Thank you {p1}")
    
    if bot:
        choice2 = npr.randint(1,4)
    else:
        print("\n")
        print("Rock, Paper, Scissors")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("\n")

        choice2 = 0
        while choice2 not in (1,2,3):
            choice2 = int(getpass.getpass(f"Please select your choice {p2}: "))

        print(f"Thank you {p2}")
    print("\n")
    print(f"{p1} chose {options[choice1]}, and {p2} chose {options[choice2]}...")
    print(outcomes[(choice1,choice2)])
    print("\n")
    print("Thanks for playing!")

    answer = ""
    while answer not in ("Y", "N"):
        answer = input("Would you like to play again? (Y/N): ").upper()
    keep_playing = {
        "Y": True,
        "F": False
    }[answer]

    print("\n")
    