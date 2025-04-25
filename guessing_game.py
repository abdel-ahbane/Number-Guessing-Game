"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Import the random module.

# Create the start_game function.
# Write your code inside this function.

#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
#   2. Store a random number as the answer/solution.
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".

#   4. Once the guess is correct, stop looping, inform the user they "Got it"
#      and show how many attempts it took them to get the correct number.
#   5. Let the player know the game is ending, or something that indicates the game is over.

# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.

import random


def start_game():
    """Prompts the user to input an int guess between 1 to 10,
    then guiding them with a feedback showing it the guess is higher then the winning number or lower until the user gets it right.
    Shows the number of attempts before correct guess.
    ( More enhancements later... )
    """
    # write your code inside this function.
    welcome_message = "*****WELCOME TO NUMBER GUESSING GAME*****\n\n"
    print(welcome_message)

    jackpot = random.randint(1,10)
    guess = 0
    attempts = 0
	
    while guess != jackpot:
        guess = int(input("what's your guess (1 - 10)? "))
        if guess > jackpot:
            print("it's lower")
        elif guess < jackpot:
            print("it's higher")
        attempts +=1
    
    print("\nCongrats, YOU GOT IT!")
    print(f"It took you {attempts} attempts to guess it correctly")

    exit_message = "\n\n***** GAME OVER - Goodbye! *****"
    print(exit_message)

# Kick off the program by calling the start_game function.
start_game()
