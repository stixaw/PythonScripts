import os

if (os.environ['PROCESSOR_ARCHITECTURE']) == True or (os.environ['PROCESSOR_ARCHITEW6432'] == 'AMD64'):
  print "64bit"
elif  (os.environ['PROCESSOR_ARCHITECTURE'] == 'x86'):
  print "32bit"
else:
  print "no clue what you have"