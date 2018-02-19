#Guess The Number Game

# computer generates a random number between 1 and 100 
#the player generates guesses
# the program evaluatest the guess as high or low
#the program keeps track of the number of guesses 
#when the number is guessed the program says right and done in this many guesses

import random

#program generates a Number to be guessed
print "I am thinking of a number between 1 and 100"
print "Try to guess the number in as few guesses as possible."

number = random.randrange(100) +1
low = 1
high = 100

#program asks the player to guess the number and program tracks the number of guesses
guess = int(raw_input("Guess the number: "))
tries = 1

#program evaluates number
while guess != number:
  if (guess > number):
    high = guess
    print "your guess is too high"
    print "the number is now between ", low, "and", high
    guess = int(raw_input("Guess the number: "))
    tries += 1
  
  else:
    low = guess
    print "your guess is too low"
    print "the number is now between ",low , "and", high
    guess = int(raw_input("Guess the number: "))
    tries += 1
  
print "Congratulations you guessed the number", number, "in", tries, "tries."

raw_input("\nPress enter to exit")