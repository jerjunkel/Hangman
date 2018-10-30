# All the functions neeed for the hangman game

class GameFunctions():
	"""Handles all the functions needed for the game."""

	def __init__(self):
		"""Initializes game function object"""

		self.characters_used_set = set()

	def character_already_used(self, character):
		"""Checks if character was already used by the user"""
		if character in self.characters_used_set:
			print("Character already used")
			return True
		else:
			self.characters_used_set.add(character)
			print("Character added")
			return False

	def is_user_input_valid(self, user_input):
		"""Check if user input is a valid entry"""
		stripped_input = user_input.strip()

		if len(stripped_input) > 1:
			print("Input to long! One character only")
			return False
		elif len(stripped_input) == 0: 
			print("Not enough characters")
			return False

		return True