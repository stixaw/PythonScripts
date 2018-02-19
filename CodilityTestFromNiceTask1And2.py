import os
import functools

class Hobbies:
	
	@staticmethod

	def find_hobbyists(hobbies, hobby):
		result = ""
		for name, hobbies in hobbies.items():
			if hobby in hobbies:
				result = name
		message = ("%s has a hobby called %s" % (result, hobby))
		print(message)

def countChars(*args):
	letters = {}
	for i in args:
		for c in i:
			try:
				letters[c.upper()] += 1
			except:
				letters[c.upper()] = 1
	print(letters)

def indexOfNumber(A, B):
	
	strB = str(B)
	strA = str(A)
	result = strB.find(strA)
	print(result)
	return(result)
	
def listPlusOne(numList):
	
	if numList[0] == 0:
		result = []
	else:
		result = []
		num1 = 0
		num1 = int("".join(map(str, numList)))
	
		num2 = int(num1) + 1
	
		for num in str(num2):
			result.append(int(num))
	print(result)
	return(result)
	
def changeString(str1):
	
	if "AB" in str1:
		index = str1.find("AB")
		str2 =str1.replace("AB", "AA")
		print(index, str2)
		
	elif "AA" in str1:
		index = str1.find("AA")
		str2 = str1.replace("AA", "AC")
		print(index, str2)
		
	elif "AC" in str1:
		index = str1.find("AC")
		str2 = str1.replace("AC", "AA")
	
	print("original {}, converted {}".format(str1, str2))

	
#This is the main program
if __name__ == '__main__':
	
		#indexOfNumber(14, 132456)
		#indexOfNumber(32, 132456)
		
		#listPlusOne([1,2,3])
		#listPlusOne([0,0,12])
		
		changeString("ACAAAB")