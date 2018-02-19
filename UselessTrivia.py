#Useless Trivia Program
#
# Gets personal information from the user and then prints
#true, but useless facts about him or her

#Getting the user input name, age, weight
print "Hi there and welcome to the Useless trivia program"

print "First we need to gather some information about you!"

print "Please answer each question and enjoy the Trivia!"

name = raw_input("What is your name? ")

try:
  age = int(raw_input("How old are you? "))
except ValueError:
  print "That was not a number please try again"
  age = int(raw_input("How old are you? "))

try:
  weight = int(raw_input("Ok, last one, how much do you weigh? "))
except ValueError:
    print "That was not a number please try again"
    weight = int(raw_input("Ok, last one, how much do you weigh? "))
  
dog_years = age / 7
print "\nDid you know that you are just", dog_years, "in dog years"

seconds = age * 365 * 24 * 60 * 60
print "\nYou are also over", seconds, "seconds old!"

called = name * 15
print """
\nIf Stewie Griffin was trying to get your attention, "\
your name would become:"
"""
print called

moon_weight = weight / 6.0
print "\nYour weight on the moon would be", moon_weight, "pounds."

sun_weight = weight * 27.1
print "\nAnd your weight on the sun would be", sun_weight, "pounds."

raw_input("\nPress enter key to exit")
