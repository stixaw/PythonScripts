#Fortune Cookie
#random fortune each time it runs

#create 1-10 fortunes
import random

fortune_1 = '"He who has wisdom will not piss off Angel, less he meet an untimely ending at the edge of her sword"'
fortune_2 = '"On the 3rd day of the 5th month, on the 309th second, you will be graced with a thought"'
fortune_3 = '"You are foolish if you believe your life can be determined by the fortune I give"'
fortune_4 = '"Ninja and Pirates are mortal enemies, it is a basic law of nature."'
fortune_5 = '"The law of inverse ninja strength states that as the ninja deplete in number so the remaining ninja increases in strength"'
fortune_6 = '"The hooker who gives her wares away for free is not much of a hooker"'

fortune = random.randrange(13) +1

#create rules for randomly selecting the fortune based on random data provided by the user

letter = raw_input("what is the first letter of your first name: ")
age = int(raw_input("what is your age: "))
sign = raw_input("What is your horoscope sign: ")

print "Confusious, peers deep into the cookie bin and pulls out a fortune cookie"
print "You crack open your fortune and read"

#generate a random fortune
if fortune == 1 or fortune == 12:
  print fortune_6

elif fortune == 2 or fortune == 11:
  print fortune_1

elif fortune == 3 or fortune == 10:
  print fortune_2

elif fortune == 4 or fortune == 9:
  print fortune_5

elif fortune == 5 or fortune == 8:
  print fortune_3

else:
  print fortune_4


raw_input("\nPress Enter to exit")