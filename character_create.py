#Create a Character Creation program
#30 Points to spend
#Attributes: Str, Health, wisdom, dexterity, endurance
#add and subtract till complete

import os
import sys

print
""" \tWelcome to Character Creation Program"""

print "Each choice you make will determine how your character will perform"

print "Here is a helpful break down of how the stats will affect your character"
print 'Strength determines how much damage you inflict with a melee weapon'
print 'Health determines how many hit points you have'
print 'Wisdom determines how well you deflect spells and cast spells'
print 'Dexterity determines how much damage you avoid'
print 'Endurance determines how long you can fight or cast spells'

character_base={}

sex =raw_input("\nWill you be a Male or Female?: ")
sex = sex.lower()

print "You have chosen", sex
if sex == 'male':
	character_male = {'Strength': 3,'Health': 3,'Wisdom': 3,'Dexterity': 3,'Endurance': 3}
	character_base=character_male
	print "Your Base stats for a Male character are:"
	for stat in character_base:
		print stat, '=', character_base[stat]

if sex == 'female':
	character_female = {'Strength': 2,'Health': 3,'Wisdom': 4,'Dexterity': 5,'Endurance': 5}
	character_base=character_female
	print "Your Base stats for a Female character are:"
	for stat in character_base:
		print stat, '=', character_base[stat]

print "\nNow it is time to choose your Profession"
print "\nEach Profession has additional base stats"
print "\nThe professions are Rogue, Tank, Mage"

character_profession = raw_input("\nWhich profession will you be, Rogue, Tank or Mage: ")
profession = character_profession.lower()

character_rogue={}

if profession == 'rogue':
	rogue = {'Strength': 1,'Health': 1,'Wisdom': 3,'Dexterity': 5,'Endurance': 5}
	print "\nThe base rogue stats are: "
	for stat in rogue:
		print stat, '=', rogue[stat]
	print "\nNow we will combine the stats."
	character_rogue['Strength'] =int(character_base['Strength']) + int(rogue['Strength'])
	character_rogue['Health'] =int(character_base['Health']) + int(rogue['Health'])
	character_rogue['Wisdom'] =int(character_base['Wisdom']) + int(rogue['Wisdom'])
	character_rogue['Dexterity'] =int(character_base['Dexterity']) + int(rogue['Dexterity'])
	character_rogue['Endurance'] =int(character_base['Endurance']) + int(rogue['Endurance'])
	character_base=character_rogue
	
	print "Your Base stats for a Rogue are:"
	for stat in character_base:
		print stat, '=', character_base[stat]

character_tank={}
if profession == 'tank':
	tank = {'Strength': 4,'Health': 4,'Wisdom': 1,'Dexterity': 3,'Endurance': 3}
	print "\nThe base tank stats are: "
	for stat in tank:
		print stat, '=', tank[stat]
	print "\nNow we will combine the stats."
	character_tank['Strength'] =int(character_base['Strength']) + int(tank['Strength'])
	character_tank['Health'] =int(character_base['Health']) + int(tank['Health'])
	character_tank['Wisdom'] =int(character_base['Wisdom']) + int(tank['Wisdom'])
	character_tank['Dexterity'] =int(character_base['Dexterity']) + int(tank['Dexterity'])
	character_tank['Endurance'] =int(character_base['Endurance']) + int(tank['Endurance'])
	character_base=character_tank
	
	print "Your Base stats for a Tank are:"
	for stat in character_base:
		print stat, '=', character_base[stat]

character_mage={}
if profession == 'mage':
	mage = {'Strength': 1,'Health': 2,'Wisdom': 6,'Dexterity': 2,'Endurance': 3}
	print "\nThe base mage stats are: "
	for stat in mage:
		print stat, '=', mage[stat]
	print "\nNow we will combine the stats."
	character_mage['Strength'] =int(character_base['Strength']) + int(mage['Strength'])
	character_mage['Health'] =int(character_base['Health']) + int(mage['Health'])
	character_mage['Wisdom'] =int(character_base['Wisdom']) + int(mage['Wisdom'])
	character_mage['Dexterity'] =int(character_base['Dexterity']) + int(mage['Dexterity'])
	character_mage['Endurance'] =int(character_base['Endurance']) + int(mage['Endurance'])
	character_base=character_mage
	
	print "Your Base stats for a Mage are:"
	for stat in character_base:
		print stat, '=', character_base[stat]

print "\nNow to personalize this budding start of the RPG world"
character_name = raw_input( "\nWhat is your Character's Name? ")


print "\nWelcome Master", profession, character_name,'.'
print "\n Now you will finish your character development by distributing 30 points between your existing stats"

pool={'Strength': 0,'Health': 0,'Wisdom': 0,'Dexterity': 0,'Endurance': 0}
count = 30

while count != 0:
	stat = raw_input("\nwhich stat would you like to add points to, Strength, Health, Wisdom, Dexterity, or Endurance? ")
	stat = stat.lower()
	value = raw_input("\nHow many points do you want to add to %s: " % (stat))
	value = int(value)
	count = count - value
	if stat == 'strength':
		pool['Strength']=value
		character_base['Strength'] =int(character_base['Strength']) + int(pool['Strength'])
		print "you now have these stats"
		for stat in character_base:
			print stat, '=', character_base[stat]
		print "\nYou have ", count, " points left to distribute"
	elif stat == 'health':
		pool['Health']=value
		character_base['Health'] =int(character_base['Health']) + int(pool['Health'])
		print "you now have these stats"
		for stat in character_base:
			print stat, '=', character_base[stat]
		print "\nYou have ", count, " points left to distribute"
	elif stat == 'wisdom':
		pool['Wisdom']=value
		character_base['Wisdom'] =int(character_base['Wisdom']) + int(pool['Wisdom'])
		print "you now have these stats"
		for stat in character_base:
			print stat, '=', character_base[stat]
		print "\nYou have ", count, " points left to distribute"
	elif stat == 'dexterity':
		pool['Dexterity']=value
		character_base['Dexterity'] =int(character_base['Dexterity']) + int(pool['Dexterity'])
		print "you now have these stats"
		for stat in character_base:
			print stat, '=', character_base[stat]
		print "\nYou have ", count, " points left to distribute"	
	elif stat == 'endurance':
		pool['Endurance']=value
		character_base['Endurance'] =int(character_base['Endurance']) + int(pool['Endurance'])
		print "you now have these stats"
		for stat in character_base:
			print stat, '=', character_base[stat]
		print "\nYou have ", count, " points left to distribute"

print "\nYou are out of points to distribute"

print "\nYou are ready to join the world Master", profession, character_name,'!'
for stat in character_base:
	print stat, '=', character_base[stat]

print "\nHave fun storming the castle "






