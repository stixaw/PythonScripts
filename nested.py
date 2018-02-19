import os
import sys


#High Scores 2.0
# nested sequences

scores = []

choice = None
while choice != "0":
	print\
	"""
	High Scores Keeper
	
	0 - Quit
	1 - List Scores
	2 - Add Score
	"""
	try:
		choice = raw_input("What is your Choice: ")
	except:
		choice = raw_input("What is your choice? ")
	#exit
	if choice == '0':
		print "Goodbye"
	#display High Scores
	elif choice == '1':
		print "Name\tScore"
		for entry in scores:
			score, name = entry
			print name, "\t\t", score
	#add score
	elif choice == '2':
		name = raw_input("What is the player's name? ")
		score = int(raw_input("What score did the player get? "))
		entry = (score, name)
		scores.append(entry)
		scores.sort() #want the highest score first
		scores = scores[:5]  #keep only the top 5 scores
	else:
		print "sorry choice is not valid"
