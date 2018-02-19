#tipper program
#this program will help you with tipping a waiter or waitress
#your options will be 15% or 20% and for the bad waiter or waitress 2%

try:
  bill = float(raw_input("You are in a resturant, and you ask for the check, how much was the check? "))
except ValueError:
  print "please enter the bill in dollar and cents"
  bill = float(raw_input("\nWhat is your total food bill? "))

utah_tip = bill * .06
avg_tip = bill  * .10
good_tip = bill * .15
ny_tip = bill * .20
bad_tip = bill * .02

print "if you were my dad you would tip the waiter: %.2f" % utah_tip, " or 6%."
print "the average tip most people leave would be: %.2f" % avg_tip, "or 10%."
print "most people consider a good tip to be: %.2f" % good_tip, " or 15%."
print "in New York you are the big tipper so its: %.2f" % ny_tip, " or 20%."
print "When the waiter stinks you just give them: %.2f" % bad_tip, "or what Symantec figures is a good annual raise!"

raw_input("\nPress enter key to exit")