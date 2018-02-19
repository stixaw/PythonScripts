#High Scores
#Demonstrate the list methods

scores = []
choice = None

#Setup menu choices

while choice != "0":
  print \
  """
  High Scores Keeper
  0 - Exit
  1 - Show Scores
  2 - Add a Score
  3 - Delete a Score
  4 - Sort Scores
  """
  
  choice = raw_input("Choice: ")
  print
  
  #exit the program
  if choice == "0":
    print "Good Bye!"
  
  # print scores
  elif choice == "1":
    print "High Scores"
    for score in scores:
      print score
  
  #add a score
  elif choice == "2":
    score = int(raw_input("What score would you like to add: "))
    scores.append(score)
  
  #delete a score from list
  elif choice == "3":
    score = int(raw_input("Delete which score?: "))
    if score in scores:
      scores.remove(score)
    else:
      print score, "isn't in the high scores list"
  
  #sort the list
  elif choice == "4":
    scores.sort()
    scores.reverse()
    for score in scores:
      print score

  else:
    print "Sorry, but", choice, "isn't a valid choice."

raw_input("\nPress enter to exit")
    
