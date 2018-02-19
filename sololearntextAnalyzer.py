import os
import sys

def openText():
	filename = "C:\\Users\\Owner\\Dropbox\\PythonScripts\\test.txt"
	with open(filename) as f:
		text = f.read()
	return text
	
def countChar(text, char):
	count = 0
	for c in text:
		if c == char:
			count += 1
	return count
	
def letterPercentage(text):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	for char in alphabet:
		perc = 100 * countChar(text, char)/len(text)
		print("{0}={1}%".format(char, round(perc,2)))




#This is the main program
if __name__ == '__main__':
	
	text = openText()
	countChar(text, 'l')
	letterPercentage(text)
	
	nums =(55,44,66,22)
	print(max(min(nums[:2]), abs(-42)))