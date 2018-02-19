#Poor Man Wheel of Fortune!
#computer randomly picks a word from a list or tuple
#computer tells the player how many letters in word
#player gets 5 letter guesses
#computer answers y or n
#player must guess word success or fail

import random

WORDS = ["cat",
                "dog",
                "horse",
                "elephant",
                "gorrilla",
                "monkey"
  ]

word = random.choice(WORDS)

length = len(word)

good = ""
guesses = 5

print """
Welcome to the Poor Man Wheel of Fortune!
I am thinking of an animal
you have 5 chances to guess a letter in the word I am thinking of,
once you are done you will get to give me your final guess.
GOOD LUCK!
"""
while guesses > 0:
  letter = raw_input("Guess a letter: ").lower()
  if letter in word:
    print "Yes", letter, "is in my word"
    good = good + letter
    guesses -= 1
  else:
    print "Sorry no that is not a letter in my word"
    guesses -= 1

print "\nYou guesses show ", good, "are all in the word."

final_guess = raw_input("\nWhat is the animal I am thinking of? ").lower()
if final_guess == word:
  print "DING DING DING, THAT IS CORRECT!"
else:
  print "BOO!!! so sorry, the word was ", word,

raw_input("\nPress enter to exit")
