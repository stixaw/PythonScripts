
#Craps Roller Program
# simulates rolling 2 dice for sudo craps game.

import random

#generate the 2 dice roll
die1 = random.randrange(6) + 1
die2 = random.randrange(6) + 1

total = die1 + die2
#present results

print "You rolled a ",die1, "& a ",die2, "for a total of ", total, "."

raw_input("\nPress Enter to exit")