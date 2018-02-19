#Word Jumble Game
#
#computer picks a random word and jumbles it
#the player has to guess the word

import random

WORDS = ("snake-eyes", "Elektra", "Gambit", "Wolverine", "Deadpool", "Batman")

# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble =""
while word:
  position = random.randrange(len(word))
  jumble += word[position]
  word = word[:position] + word[(position + 1):]

#START GAME

"""
           Welcome to Hero Word Jumble!
        
   Unscramble the letters to figure out the Hero's Name!
(Press the enter key at the prompt to quit.)
"""
print "the jumble is: ", jumble

guess = raw_input("\nYour guess: ")
guess = guess.title()
while (guess != correct) and (guess != ""):
  print "Sorry, that's not it."
  guess = raw_input("Your guess: ")
  guess = guess.title()

if guess == correct:
  print "THATS IT! \n"

print "Thanks and come again!"

raw_input("\nPress enter to exit")
