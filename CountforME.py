#Count for me
#this program asks for a starting number
# an ending number
# and the multiple to count by

import os

#introduction
print """Hi I am the Counting Program, I will ask you for a starting
Number, and Ending number and a multipler to count by. Example
Starting number 1, ending number 20 and multipler 2 should produce
me counting from 1 to 20 by 2s. Got it? Ok Lets begin"""

#ask for the variables
#get the Starting Number
StartNum = raw_input("\nPlease give me a number to start my count: ")
try:
  i = int(StartNum)
except ValueError:
  StartNum = raw_input("\nNo Really, Please give me a number to start my count: ")

#get the ending number
EndNum = raw_input("\nPlease give me a number to end my count: ")
try:
  i = int(EndNum)
except ValueError:
  EndNum = raw_input("\nNo Really, Please give me a number to end my count: ")

#get the multiplier
bynum = raw_input("\nPlease give me a number by which I count: ")
try:
  i = int(bynum)
except ValueError:
  bynum = raw_input("\nNo Really, Please give me a number by which I count: ")

#Counting Loop
for i in range(int(StartNum), int(EndNum), int(bynum)):
  print i