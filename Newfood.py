#New Food
# This program takes a person's favorite foods and create a new food by combining the 2 favorite foods

print 
"""
Hi there we are going to create a new and fantastic food, 
based on your two favorite foods!
"""

fav_1 = raw_input("\nWhat is your favorite food? ")

print "ok, your favorite food is " + fav_1

fav_2 = raw_input("\nWhat is your second favorite food? ")

print "and your second favorite food is " + fav_2

print "\nnow for a bit of food magic, a new food you might like is:"

new_food = fav_2 + fav_1

print "\n" + new_food


