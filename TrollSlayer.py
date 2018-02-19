#losing battle
# bad loop

print "You are a lone hero, and are surrounded by a massive army of trolls. "
print "their decaying green bodies stretch out, melting into the horizon"
print "you unshealthe your sword to begin the final battle of your life.\n"

try:
  health = int(raw_input("\nEnter your the amount of your health at the start: "))
except ValueError:
  print "Enter your health as a numeric value please"
  health = int(raw_input("\nEnter your the amount of your health at the start: "))

trolls = 0
damage = 4

while health >= 0:
  trolls += 1
  health = health - damage
  
  print "you swing your sword and defeat an evil troll. "\
          "but you take ", damage, " damage points.\n"

print "You fought nobly lone hero and defeated ", trolls, "trolls."
print "but alas you are no more... and your life will live in a bard's song"

raw_input("\nPress the enter key to exit")