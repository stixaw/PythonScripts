#Random Access Program 
#Indexing and Random Access

import random

print "this program works with random access based on indexing"
print "it uses word length to randomly pick an index location"

try:
  word = raw_input("enter a word: ")
  print "the word is ",word, "\n"
except ValueError:
  word = raw_input("enter a word: ")

high = len(word)
low = -len(word)

for i in range(10):
  position = random.randrange(low, high)
  print "word[", position, "]\t",word[position]

raw_input("\nPress enter key to exit")