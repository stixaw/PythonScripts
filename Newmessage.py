#No Vowels
#demonstrates creating a new string from an existing one wihtout Vowels

print "this program takes a message and creates a new one without Vowels"

#get the message
message = raw_input("Please enter a message: ")

#set up for new message
new_message = ""
VOWELS = "a","e","i","o","u"

print
for letter in message:
  if letter.lower() not in VOWELS:
    new_message += letter
    print "A new string has been created:", new_message

print "\nYour new message without vowels is: ", new_message

raw_input("\nPress Enter to exit")