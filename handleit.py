#handle exceptions

#try/except

try:
	num = float(raw_input("Enter a Number: "))
except:
	print "That was not a number"

#handle Valueerror specific only
try:
	num = float(raw_input("Enter a Number: "))
except(ValueError):
	print "that was not a number hoser!"


#handle multiple exceptions
print
for value in (None, "hi!")
	try:
		print "attempting to convert", value, "->",
		print float(value)
	except(TypeError, ValueError):
		print "you screwed"
