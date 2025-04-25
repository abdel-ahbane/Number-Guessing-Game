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

#Option to Play Again Prompt
#As a player, after I guess correctly and win, I should be prompted if I would like to play again.

#Display a High Score
#As a player, at the start of each game, I should be shown the current high score (least amount of guess attempts) so that I know what I am supposed to beat.

#Generate a New Winning Number
#Every time a player decides to play again, the random number to guess is updated so that players are guessing something new each time.


# Kick off the program by calling the start_game function.

import random


class GuessErrorCustom(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def start_game():
    """Prompts the user to input an int guess between 1 to 10,
    then guiding them with a feedback showing it the guess is higher then the winning number or lower until the user gets it right.
    Shows the number of attempts before correct guess.
	Keeps count of the best attempts score and allows multiple games to beat best score
    """
    # write your code inside this function.
    welcome_message = "*****WELCOME TO NUMBER GUESSING GAME*****\n\n"
    print(welcome_message)

	play = 'Y'
    best_score = 10

	while play.upper() == 'Y':
		jackpot = random.randint(1,10)
    	guess = 0
    	attempts = 0
		print(f"The best score to beat is {best_score} attempts")
		
	    while guess != jackpot:
	        try:
	            guess = int(input("what's your guess (1 - 10)? "))
	            if guess > 10 or guess < 1:
	                raise GuessErrorCustom("the guess should be an integer between 1 and 10")
	        except GuessErrorCustom as e:
	            print(f'invalid input! {e}')
	            continue
	        except ValueError:
	            print("Invalid input! Please enter an integer number.")
	            continue
	
	        if guess > jackpot:
	            print("it's lower")
	        elif guess < jackpot:
	            print("it's higher")
	        attempts +=1

		if attempts < best_score:
			best_score = attempts
		
		print("\nCongrats, YOU GOT IT!")
		print(f"It took you {attempts} attempts to guess it correctly")

		play = input("Would you like to play again (Y or N)? ")

    exit_message = "\n\n***** GAME OVER - Goodbye! *****"
    print(exit_message)

# Kick off the program by calling the start_game function.
start_game()
