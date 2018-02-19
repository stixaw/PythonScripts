#hero inventory
# demonstrates tuples

#create a tuple
inventory = ("sword",
                   "dagger",
                   "armor",
                   "shield",
                   "healing potion")

#get the number of items in inventory
print "You have ", len(inventory), "items in your possession."

#print each element in the Tuple
print "\nIn your Inventory you carry: "
for item in inventory:
  print item

#test for stamina potions
if "stamina potion" in inventory:
  print "you have additional supplies to allow you to go farther"
else:
  print "you will run out of stamina you fool go back and get some food or stamina potions"

print "as you travel down the road out of town you find a chest"

chest = ("10 gold pieces", "food", "water", "leather boots")

print "\nYou open the chest and find: "
print chest

print "1 = 10 gold pieces"
print "2 = food"
print "3 = water"
print "4 = leather boots"

print "you may add 2 items from the chest to your inventory"
index1 = int(raw_input("\nEnter 1-4 to select your first item: ")) -1
index2 = int(raw_input("\nEnter 1-4 to select your first item: ")) -1
item1 = chest[index1]
item2 = chest[index2]

print "you have selected ",item1, "and", item2, "and add them to your inventory."

inventory += item1, item2

print "Your Inventory is now:"
for item in inventory:
  print item

raw_input("\nPress enter to exit")