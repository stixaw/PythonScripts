#Hero's Inventory 3.0

inventory = [
    "bath towel",
    "sword",
    "bag of gold",
    "shield",
    "healing potion",
    "frog"
]


def print_inv():
    for items in inventory:
      print(items)

print("You are a young hero,")
print("You have", len(inventory), "items in your inventory as you start out on your hero's path")
print_inv()

if "muton" in inventory:
    print("hey you have food!")
else:
    print("how far do you think you will go without food!")

#index = int(raw_input("\nEnter the index number for an item in inventory: ")) -1
#print "the item which correlates with that number is: ", index + 1, inventory[index]

#display slice
# begin = int(raw_input("\nEnter the start: ")) -1
#end = int(raw_input("\nEnter the end: ")) -1
#print "inventory [", begin, ":", end, "]\t\t",
#print inventory[begin:end]

print("\nYou come across a chest as you wander about the land.")

chest = [
    "flagon of wine",
    "feather",
    "muton",
    "slightly blue pear",
    "silver framed mirror"
]

print("\nyou open it to find it filled with: ")
print(chest)

print("flagon of wine = 1")
print("feather = 2")
print("muton = 3")
print("slightly blue pear = 4")
print("silver framed mirror = 5")

print("\nYou may add 3 items from the chest to add to your inventory.")
index1 = int(input("\nEnter 1-4 to select your first item: ")) -1
index2 = int(input("\nEnter 1-4 to select your second item: ")) -1
index3 = int(input("\nEnter 1-4 to select your third item: ")) -1
item1 = chest[index1] 
item2 = chest[index2]
item3 = chest[index3]

print("\nYou have selected ",item1, ",", item2, "and", item3, "you add them quickly to your inventory.")

inventory += item1, item2, item3

print("\nYou now have", len(inventory), "items in your inventory.")
print("\nYour Inventory is now:")
print_inv()

if "muton" in inventory:
    print("\nHey you have food now!")
else:
    print("\nHow far do you think you will go without food!")

if "flagon of wine" in inventory:
    print("\nYou take a swig of Wine...")
    print("hic hic hic")

print("\nAs you continue down the trail you come across a weaponsmith.")
print("He offers you a trade, one of his slick new crossbows for your bath towel.")

trade_request = input("\nDo you accept the trade? (y or n)")
if trade_request == "y":
    print("\nYou have accepted his trade!")
    inventory[0] = "crossbow"
else:
    print("\nReally?? How often do you think you are going to take a bath?")

print("\nYour inventory now contains: ")
print_inv()

print("\nYou continue your journey, as you walk along you see a bag of gems on the ground.")
bag = ["gems"]

take_gems = input("\nDo you take the gems? (y or n)")
if take_gems == "y":
    print("You look around and seeing that no one there you the gems in your inventory.")
    inventory += bag
else:
    print("""You look around and seeing that no one is there..
          you consider that if I just leave them here they will be taken any way...
            so you pick up the gems and ad them to your inventory... /naughty naughty
          """)
    inventory += bag

print("\nYou wander a bit more and come to the 'SHOP O MYSTICS!'")
print("You see a sign on the window 'TODAY ONLY, Orb of Future Telling!'")
print("\nYou decide to go in and see about getting one of these orbs.")

buy_orb = input("\nThe orb will cost you your gold, do you buy it? (y or n)")
if buy_orb == "y":
    print("\nYou buy the orb of future telling for your gold")
    inventory[2] = "orb of future telling"
    print("You gaze into the orb and see nothing... perhaps you should have gotten some instructions!")
else:
    print("\nThe mystic waves a hand as you turn to leave, and says 'you will trade you gold for my orb'")
    print("Your eyes glaze over saying 'I will trade my gold for your orb', and hand him your gold")
    print("You gaze into the orb and see nothing... perhaps you should have gotten some instructions!")
    inventory[2] = "orb of future telling"

print("Your inventory now contains: ")
print_inv()

print("\nYou are suddenly attacked by a bandit")
print("Wouldn't it have been nice to see that in the orb of future telling?")
print("You defeat the bandit, but as he runs away you notice your", inventory[5], "is dead!")

bury_frog = input("\nDo you bury the frog? (y or n)")
if bury_frog == "y":
    print("\nYou bury it and as you do you shed a little tear...")
    del inventory[5]
else:
    print("you toss the frog into some nearby bushes and continue on down the path.")
    del inventory[5]

print("\nYou now carry these items in your inventory: ")
print_inv()

print("\nIts getting dark and you decide to rest for the night in a nearby cave.")
print("You gaze in the orb once more before closing your eyes to see nothing but the reflection of your face.")
print("While you sleep you are decended upon by theives")
print("\nThey take two of your",len(inventory), "items: ")
stolen_item1 = int(input("\nchoose a number for the first item to loose: ")) +1
stolen_item2 = int(input("\nchoose a number for the second item to loose: ")) +1
print("\nThe Dam theives took your: ", inventory[stolen_item1], "and",inventory[stolen_item2])
del inventory[stolen_item1], inventory[stolen_item2]
print("\nYou wake up to find these items left in your inventory: ")
print_inv()

print("\nYou look up to the sky and scream NOOOOOOOOOOOOOOOOOOOO")

input("\nPress enter to exit")
