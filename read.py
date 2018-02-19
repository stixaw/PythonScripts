# Read it program
#reading from a text file

print "\nOpening and Closing the file"

text_file = open("C:\\read_it.txt", "r")
text_file.close()

print "\nreading characters from read_it.txt"
text_file = open("C:\\read_it.txt", "r")
print text_file.read(1)
print text_file.read(5)
text_file.close()

print "\nreading the file"
text_file = open("C:\\read_it.txt", "r")
print text_file.read()
text_file.close()



print "\nreading charcaters from a line"
text_file=open("C:\\read_it.txt", "r")
print text_file.readline(1)
print text_file.readline(3)
text_file.close()

print "\nreading file line by line"
text_file=open("C:\\read_it.txt", "r")
print text_file.readline()
print text_file.readline()
print text_file.readline()
text_file.close()

print "\nreading file line into list"
text_file=open("C:\\read_it.txt", "r")
lines=text_file.readlines()
print lines
print len(lines)
for line in lines:
	print line
text_file.close()

print "\nLooping through the lines"
text_file=open("C:\\read_it.txt", "r")
for line in text_file:
	print line
text_file.close()
