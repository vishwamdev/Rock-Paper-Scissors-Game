import random

options = ("scissor", "paper", "rock")
playing = True

print("---SPR Game---")

while playing:
    player = input(f"Enter a choice {options}: ")
    computer = random.choice(options)

    while player not in options:
        print("Your choice is not valid.")
        player = input(f"Please enter a choice from the brackets{options}: ")

    print(f"Player: {player}")
    print(f"computer: {computer}")

    if player == computer:
            print("It's a tie!")
    elif player == "rock" and computer == "scissor":
            print("You win!")
    elif player == "scissor" and computer == "paper":
            print("You win!")
    elif player == "paper" and computer == "rock":
            print("You win!")
    else:
            print("You lose!")

    play_again = input("Play again?(y/n): ").lower()

    if not play_again == "y":
        playing = False

print("Thanks for playing")