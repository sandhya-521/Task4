import random

print("=== Rock, Paper, Scissors Game ===")

options = ["rock", "paper", "scissors"]
scores = {"You": 0, "Computer": 0}

def play_round(user_pick):
    comp_pick = random.choice(options)
    print(f"Computer chose: {comp_pick}")

    if user_pick == comp_pick:
        return "Tie"
    elif (user_pick, comp_pick) in [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]:
        return "You"
    else:
        return "Computer"

while True:
    user_choice = input("\nEnter rock, paper, or scissors (or 'quit' to exit): ").lower().strip()

    if user_choice == "quit":
        print("\nGame Over! Final Scores:")
        print(f"You: {scores['You']} | Computer: {scores['Computer']}")
        break

    if user_choice not in options:
        print(f"❌ Invalid choice: '{user_choice}'. Please type 'rock', 'paper', or 'scissors'.")
        continue

    winner = play_round(user_choice)

    if winner == "Tie":
        print("Result: It's a tie!")
    else:
        print(f"Result: {winner} wins this round!")
        scores[winner] += 1

    print(f"Current Score → You: {scores['You']} | Computer: {scores['Computer']}")
