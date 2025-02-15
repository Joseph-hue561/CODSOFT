import random

options = ("rock", "paper", "scissors" )

running =  True
user_score = 0
computer_score = 0

print("Welcome to Rock-Paper-Scissors!")
print("Instructions: Choose rock, paper, or scissors to play against the computer.")
print("Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.")
print("Try to outscore the computer. Good luck!\n")


while running:
    print("---------------------------------")
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")
        if player not in options:
         print("Invalid choice. Please enter rock, paper, or scissors.")

    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}\n")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win this round!")
        user_score += 1
    elif player == "paper" and computer == "rock":
        print("You win this round!")
        user_score += 1
    elif player == "scissors" and computer == "paper":
        print("You win this round!")
        user_score += 1
    else:
        print("You lose this round!")
        computer_score += 1
    print(f"Score - You: {user_score} | Computer: {computer_score}\n")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False
print("\nThanks for playing! Final Score - You: {} | Computer: {}".format(user_score, computer_score))
print("Goodbye!")