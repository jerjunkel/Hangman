# Just a simple hangman game
from random_word import RandomWordGenerator
from game_functions import GameFunctions

game_func = GameFunctions()

word_to_guess = RandomWordGenerator().get_random_word()

game_is_active = True
user_guess_letter = False
user_strike_count = 0

# List comprehension
word_guess = list(["_" for x in range(len(word_to_guess))]) #Creates a list with the random word length.

#print(word_guess)

while game_is_active:
	userinput = input("Enter a character: ")

	if not game_func.is_user_input_valid(userinput):
		continue

	if game_func.character_already_used(userinput):
		continue

	for index, char in enumerate(word_to_guess): #Returns the index and value 
		if userinput == char:
			word_guess[index] = char
			user_guess_letter = True

	if not user_guess_letter:
		user_strike_count += 1
	else:
		user_guess_letter = False

	print("End of loop")
	print(word_guess)

	if user_strike_count == 6:
		print("You lost")
		game_is_active = False
		break

	if "_" not in word_guess:
		print("YOU WON!!")
		game_is_active = False
		break

	print("User strike count " + str(user_strike_count))

	#game_is_active = False
