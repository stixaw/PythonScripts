#Trivia game

import sys

def open_file(file, mode):
	try:
		f = open(file, mode)
	except(IOError), e:
		print "Unable to open ", file. "ending program.\n"
		raw_input("\n\nPress the enter key to exit.")
		sys.exit
	else:
		return f

def next_line(f):
	line = f.readline()
	lin =  line.replace("/", "\n")
	return line

