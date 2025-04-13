import random

#Scores
player_score = 0
computer_score = 0

# Hand signs
signs = {
    1: "✊",
    2: "✋",
    3: "✌",
    4: "🦎",
    5: "🖖"
}

# Win conditions
wins_against = {
    1: [3, 4],  # Rock
    2: [1, 5],  # Paper
    3: [2, 4],  # Scissors
    4: [2, 5],  # Lizard
    5: [1, 3]   # Spock
}

# Game loop
while True:
    print("\n================================")
    print("Rock Paper Scissors Lizard Spock")
    print("================================")
    print("1) ✊")
    print("2) ✋")
    print("3) ✌️")
    print("4) 🦎")
    print("5) 🖖")

    # Get player input
    try:
        player = int(input("Pick a number (1-5): "))
        if player < 1 or player > 5:
            print("Invalid choice. Try again.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Get computer choice
    computer = random.randint(1, 5)

    print("You chose:", signs[player])
    print("CPU chose:", signs[computer])

    # Determine winner
    if player == computer:
        print("It's a tie! 🦖")
    elif computer in wins_against[player]:
        print("The player won! 🎉")
        player_score += 1
    else:
        print("The computer won! 😢")
        computer_score += 1

    #Print scoreboard
    print(f"Score -> Player: {player_score} | CPU: {computer_score}")

    # Ask to play again
    again = input("Play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing! 👋")
        break
