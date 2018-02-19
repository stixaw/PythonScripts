import os
import sys


def modifyString2(str1 = raw_input()):
	strSplit = str1.split()
	print(strSplit)
	str2 = ""
	count = 0
	print(len(strSplit))
	while count < len(strSplit):
		for i in strSplit:
			letters = []
			print i
			for c in i:			
				if c not in letters:
					letters.append(c)
					print(letters)
			word = i[0] + str(len(letters)) + i[len(i)-1]
			print(word)
			if len(str2) == 0:
				str2 += word
			else:
				str2 += " " + word
			count += 1
	print(str2)


def modifyString():
str1 = raw_input("type a string")
	strSplit = str1.split()
	print(strSplit)
	str2 = ""
	count = 0
	print(len(strSplit))
	while count < len(strSplit):
		for i in strSplit:
			letters = []
			print i
			for c in i:			
				if c not in letters:
					letters.append(c)
					print(letters)
			word = i[0] + str(len(letters)) + i[len(i)-1]
			print(word)
			if len(str2) == 0:
				str2 += word
			else:
				str2 += " " + word
			count += 1
	print str2
	return str2


#This is the main program
if __name__ == '__main__':
	
	print"HI"
	sr1 = ""
	raw_input()
	