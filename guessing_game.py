"""
Python Development TechDegree
Project 1 - The Number Guessing Game
--------------------------------
"""


import random


class GuessErrorCustom(Exception):
	"""Custom exception to handle invalid guesses."""
	def __init__(self, message):
		self.message = message
		super().__init__(self.message)


def start_game():
	"""Prompts the user to input an int guess between 1 and 10,
	then guiding them with a feedback showing it the guess is higher than the winning number or lower until the user gets it right.
	Shows the number of attempts before correct guess.
	Keeps count of the best attempts score and allows multiple games to beat best score
	"""
    # write your code inside this function.
	welcome_message = "*****WELCOME TO NUMBER GUESSING GAME*****\n\n"
	print(welcome_message)

	play = 'Y'
	best_score = float('inf')  # Initialize best score with infinity

	while play.upper() == 'Y':
		jackpot = random.randint(1,10)
		guess = 0
		attempts = 0
		print(f"The best score to beat is {best_score} attempts" if best_score != float('inf') else "No best score yet. You could set it!")
		
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

if __name__ == "__main__":
	start_game()
