#Word Jumble Game
#computer picks a random word and jumbles it
#the player has to guess the word

import random

WORDS = [ "Snake-eyes",
               "Elektra", 
               "Gambit", 
               "Wolverine", 
               "Deadpool", 
               "Batman"
               ]
HINTS = [  "GI-Joe Ninja",
                "Ultimate Female Assassin",
                "Ragin Cajin",
                "Claws and Muscles",
                "Mercenary with a mouth",
                "Dark Knight"
                ]

# pick one word randomly from the sequence
#word = random.choice(WORDS)

word = random.choice(WORDS)

if word == 'Snake-eyes':
  index = 0
elif word == 'Elektra':
  index = 1
elif word == 'Gambit':
  index = 2
elif word == 'Wolverine':
  index = 3
elif word == 'Deadpool':
  index = 4
else:
  index = 5

# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble =""
while word:
  position = random.randrange(len(word))
  jumble += word[position]
  word = word[:position] + word[(position + 1):]

#START GAME

print """
           Welcome to Hero Jumble!
        
   Unscramble the letters to figure out the Hero's Name!
(Press the enter key at the prompt to quit.)"""

print "\nThe jumble is: ", jumble

guess = raw_input("\nYour guess: ")
guess = guess.title()
while (guess != correct) and (guess != ""):
  print "Sorry, that's not it."
  get_hint = raw_input("would you like a hint? y or n: ")
  if get_hint == "y":
    print HINTS[index]
    guess = raw_input("Your guess: ")
    guess = guess.title()
  else:
    guess = raw_input("Your guess: ")
    guess = guess.title()

if guess == correct:
  print "THATS IT!"

print "Thanks and come again!"

raw_input("\nPress enter to exit")
