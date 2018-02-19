#Select Network
#Compound conditions

print """Sith Training program"
        Where we strip you of your helpful tendancies"""
print "Login to gain access"

security = 0

username = ""
while not username: 
  username = raw_input("Username: ")

password = ""
while not password:
  password = raw_input("Password: ")

if username == "Awilliams" and password == "Puddi":
  print "Welcome Sith Lord Angel, we bow to your power and evil"
  security = 5
  print "Security Clearance ", security

elif username == "guest" or password == "guest":
  print "sith initiate, prepare to suffer for your skills"
  security = 1
  print "Security Clearance ", security

elif username == "Cclark" and password == "Harley":
  print "my apprentice... you descent to the dark side is almost complete"
  security = 3
  print "Security Clearance ", security

else:
  print "You are not a Sith Lord.../choke...."


raw_input("\nPress Enter to exit")