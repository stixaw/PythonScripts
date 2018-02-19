import os
import sys

geek = {'404': 'Clueless. from the web error message 404, meaning page not found.',
	"Googling": "searching the internet for background information on a person or object",
	"Keyboard Plaque":"the collection of debris found on computer keyboards",
	"Link Rot": "the process by which web page links become obsolete",
	"Percussive Maintenance" : "the act of striking an electronic device to make it work",
	"Uninstalled": "being fired, Especially popular during the dot-bomb era"}

choice = None
while choice != '0':
	print \
	"""
	0-Quit
	1-Look up Geek Term
	2-Add a Geek Term
	3-Redefine a Geek Term
	4-Delete a Geek Term
	5-Print Know Terms
	"""
	choice = raw_input("Make your choice: ")

	if choice == "0":
		print 'Goodbye'
	elif choice == "1":
		term = raw_input("What term do you want to translate?: ")
		if term in geek:
			definition = geek.get(term)
			print "\n", term, "means", definition
		else:
			print "So Sorry no Geek term matching", term
	elif choice == "2":
		term = raw_input("What term do you want to add?: ")
		if term not in geek:
			definition = raw_input("What is its definition?: ")
			geek[term] = definition
			print term, 'has been added'
		else:
			print "so sad i already knew that one"
	elif choice == "3":
		term = raw_input("What term do you want to redefine?: ")
		if term not in geek:
			definition = raw_input("What is the new definition?: ")
			geek[term] = definition
			print term, "has been redefined"
		else:
			print "so sorry that doesn't exist in my knowledge try adding it"
	elif choice == "4":
		term = raw_input("What term is obsolete and must be deleted?: ")
		term = term.
		if term in geek:
			del geek[term]
			print "It is done"
		else:
			print "I do not understand that term is not in my data banks"
	elif choice == "5":
		for term in geek:
			print term
	else:
		print "Are you Daft? that is not a valid choice"