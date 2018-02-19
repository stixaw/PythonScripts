#Message Analyzer
#analyzes a message for "e" and length

import random

message = raw_input("Enter a message: ")

print "\nthe length of the message is: ", len(message)

print "\nThe most common letter in the English language is 'e'."
if "e" in message:
  print "e is in your message"
else:
  print "the letter 'e' is in not in your message"
  
raw_input("\npress enter to exit")