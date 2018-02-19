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
# pick one word randomly from the sequence
#word = random.choice(WORDS)

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

print """
           Welcome to Hero Jumble!
        
   Unscramble the letters to figure out the Hero's Name!
   Try to guess the Hero's name in as few guesses as possible
   the highest score is the winner!
   (Press the enter key at the prompt to quit.)
"""

print "\nThe jumble is: ", jumble

guess = " "
lst = range(len(jumble)) 
hint_str = '_'*len(jumble)
score = 100


guess = raw_input("\nYour guess: ")
guess = guess.title()

while (guess != correct) and (guess != ""):
  print "SORRY try again: "
  get_hint = raw_input("would you like a hint? y or n: ")
  if get_hint == "y":
    i = random.choice(lst)
    print correct[i], "is the", i+1, "letter"
    score -= 10
    guess = raw_input("Your guess: ")
    guess = guess.title()
  else:
    guess = raw_input("Your guess: ")
    guess = guess.title()
    score -= 5

if guess == correct:
  print "That's it! You guessed it! \n Your Score is: ", score

print "Thanks and come again!"

raw_input("\nPress enter to exit")
