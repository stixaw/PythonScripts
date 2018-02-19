#Mood program
# Demonstrates if - elif -else

import random

print """
Welcome to my mood detecting program...
through some technical jumbo I can feel your energy..
and sense your aura.
We are about to begin, please let the cosmos commune
through you...
...........
I sense your energy... yes its coming to me now...
let your energy flow....
yes yes yes.... its almost there...
"""

mood = random.randrange(3)

if mood == 0:
    #happy
    print \
    """
       ----------
       |  /     \  |
       |   0   0  |
       |    <     |
       | -____- |
       |   \__/  |
       |           |
       ----------
       Aren't You the happy Git!"""

elif mood == 1:
    #neutral
    print \
    """
       ----------
       | _   _    |
       | 0   0    |
       |   <      |
       | -----   |
       |           |
       |           |
       ----------
      You don't care today."""

elif mood == 2:
    #sad
    print \
    """
       ----------
       |  \   /    |
       |  0   0   |
       |    <      |
       |  ____   |
       | /      \  |
       |           |
       ----------
    BAD MOOD WATCH OUT"""

else:
    print "I am loosing it... your aura is fading... gone"

raw_input("\nPress Enter key to exit")


    
