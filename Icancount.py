#I CAN COUNT
#
# this program counts for the user
# the user picks the starting number
# and picks to count by digit ie 1, 3 5
#picks the ending number

print"""
HI I am the Counting Program, Ican Count!
I will count for you if you will only provide a bit of information!
"""

# Ask the User for this information

start_number =int(raw_input("\nPlease give me a starting number from which to count: "))
end_number = int(raw_input("\nPlease give me the number you want me to count to: ")) +1
countby = int(raw_input("\nNow tell me the digits you want me to count by ie, 1, 3, 5, 7: "))


print "I am counting from ", start_number, "till I reach ", end_number, "by", countby, "'s."
for i in range(start_number, end_number, countby):
  print i

raw_input("\nPress enter to exit")
