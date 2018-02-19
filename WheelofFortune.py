#Better Wheel of Fortune

import random

#list of phrases
WORDS = ("lightsaber", "blaster", "force", "deathstar", "wookie", "jedi", "droid", "sandpeople")

#get a random phrase from tuple
r_word = random.choice(WORDS)

word_l = (len(r_word))
guesses = (word_l) -2
lguess = ""
secret = "_ " * (word_l)

def word_update(r_word, lguess):
  for letter in r_word:
      if letter in lguess:
          print letter,
      else:
          print "_",
 
#start the game

print """
\t\tWelcome to the Wheel of Fortune!
\t\tToday's theme is Star Wars!
"""

print "=" * 32
print "the word is: ", secret
print "\nYou have", guesses, " guesses to figure the word out"


while guesses > 0:
    letter = raw_input("\nGuess a letter: ").lower()
    #check for already guessed letters
    if letter in lguess:
        print "you already guessed that letter"
    else:
        guesses = guesses - 1
        print "you have", guesses, "guesses left"
        lguess = lguess + letter
    word_update(r_word, lguess)
    
print "\nOk you have all the clues we can give you... now guess the word!"

word_guess = raw_input("\nWhat is it? ")
if word_guess == r_word:
  print "DING DING DING, you are correct"
else:
  print "BUZZZZZZZ, I'm sorry that is not correct"
  print "The correct word was: ", r_word

print "thanks for playing Wheel of Fortune!"

raw_input("\nPress enter to exit")

