#password program
#demonstrates the if statement

print "welcome to my computer program for computer security"
print "please enter the correct password and you will get a big surprise!"

password = raw_input("\nEnter the Password: ")

if password == "secret":
  print "Access Granted, YEA!, WOOPEE! Did you like your surprise?"
else:
  print "FAIL!!!!"
  print "\a"
  

raw_input("\nPress enter to exit")  
