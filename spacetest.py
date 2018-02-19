phrase = "Use the force"

def phrase_update():
  length = len(phrase)
  count = 0
  while length > count:
    for i in phrase:
        if i in phrase:
            print i
        elif space in phrase:
            print " "
        else:
            print "_ "
  count = count + 1

phrase_update()

raw_input("\npress enter to exit")
