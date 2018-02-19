import os
import sys

scores= []

print \
"""
High Scores Keeper
0 - Exit
1 - Show Scores
2 - Add a score
3 - Delete a score
4 - Sort Scores
"""
choice = raw_input("\n Enter your choice: ")


while choice != "0":
	print \
	"""
	High Scores Keeper
	0 - Exit
	1 - Show Scores
	2 - Add a score
	3 - Delete a score
	4 - Sort Scores
	"""
	choice = raw_input("\n Enter your choice: ")
# exit
if choice =="0":
	print "Goodbye"
#list scores
elif choice == "1":
	print  "High scores"
	for score in scores:
		print score
#add score
elif choice == "2":
	score = int(raw_input("what score do you want to add?"))
	scores.append(score)
#delete a score
elif choice == "3":
	score = int(raw_input("What score do you want to remove? "))
	if score in scores:
		scores.remove(score)
	else:
		print score, "isn't in the high scores list."
#sort score
elif choice == "4":
	print "here are the scores in ascending order:"
	scores.sort()
	