# answer = input ("Player one: pick a word")
#
#
# word = (answer)
# word = word.lower()
# wordList = list(word)
#
# currentWord = "_" * len(word)
# currentWord_list = list(currentWord)
#
# tries = 6
#
# while(tries > 0):
#     guess = input("Guess a letter for the word i'm thinking of! ")
#     guess = guess.lower()
#
#     if(guess in wordList):
#         index1 = wordList.index(guess)
#         currentWord_list[index1] = guess
#
#         tries -= 1
#         print(currentWord_list)
#         #  imports the ability to get a random number
# from random import *
#
# # Generates a random integer.
# aRandomNumber = randint(1, 20)
# # print(aRandomNumber)
# # For Testing: print(aRandomNumber)
#
# # creates a variable that holds the number of tries a user has
# tries = 3
#
# while tries > 0:
# 	guess = input("Guess a number between 1-20:")
# 	if not guess.isnumeric(): # checks if a string is only digits 0 to 9
# 		print("That's not a positive whole number, try again!")
# 	else:
# 		tries -= 1 # shorthand for tries = tries - 1
# 		guess = int(guess) # converts a string to an integer
# 		# print(f"Our guess is {guess}. Our random number is {aRandomNumber}")
# 		if (guess == aRandomNumber):
# 			print("Congrats!")
# 			break
# 		elif (guess > aRandomNumber):
# 			print("Your guess is higher than my number.")
# 		else:
# 			print("Your guess is lower than my number.")
#
# # print(f"Number of tries:{tries}")
# print("You lose")
import random

# A list of words that
potential_words = ["example", "words", "someone", "can", "guess"]

word = random.choice(potential_words)

# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
# current_word = ["_", "_" * len(word)] # TIP: the number of letters should match the word
current_word = list(word)
# Some useful variables
guesses = [] #holds all previously gussed letters
maxfails = 7
fails = 0

while fails < maxfails:
    guess = input("Guess a letter: ").lower()
# This is making sure that the guess is a letter, that it is only one letter, and not the same as the previous guess
    if guess.isalpha() and len(guess) == 1 and guess not in guesses:
            # if guess in word
            # print (guess and len(word) - 1) this is wrong
            guesses.append(guess)
            if guess in current_word:
                # the guess is right
                print(" You guessed a letter correctly!")
            else:
                print( "You guessed incorrectly")
                fails = fails + 1

	#or you can write fails += +1
    #str just mkes the input into a string
    print("You have " + str(maxfails - fails) + " tries left!")
    display =""
    winning = ""
    for i in current_word:
        if i in guess:
            display += i + ""
            winning += i
            # print(i)
        else:
            display += "_ "
            # print("_")
    print(display)
    if winning == word:
        print("You won!")
        exit(0)

print(" You lost. The answer was {current_word}")
