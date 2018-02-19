#Flip Coin
#program flips a coin heads goes to the home team
#program flips the coin till it executes the same outcome 2 - 3 times

import random

counter = 100
head_count = 0
tail_count = 0

print "I flip a coin 100 times"
#100 times
while counter > 0:
  flip = random.randrange (2)
  if flip == 1:
    head_count += 1
    counter = counter - 1
  else:
    tail_count += 1
    counter = counter - 1

print "It landed on heads ", head_count, "times and landed on tails ",tail_count, "times."
  
raw_input("\nPress enter to exit")