import os
import sys
import random

#program that prints a list of words in random order not repeating any

#list of words
WORDS =["ANIMAL","BEAR","CAT","DOG","ELEPHANT","FLIPPER","GOAT"]
count = 7
used = []
word = random.shuffle(WORDS)

while count != 0:
	for word in WORDS:
		if word not in used:
			print word
			used.append(word)
			count -=  1
	print used