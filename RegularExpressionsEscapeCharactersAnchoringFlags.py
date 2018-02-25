#Regular expressions EscapeCharacters, Anchoring and Flags
import re
import os
import sys


#This is the main program
if __name__ == '__main__':
	
	text = "Python is fun. Learning python."
	print(text)
	
	pat = re.compile(r'Py')
	print(re.sub(pat, 'My', text))
	print(re.sub(r'Py', 'My', text, flags=2))
	
	
	text = '''Py\nthon.'''
	print(text)
	
	print("using r'.+'")
	#pat = re.compile(r'Python')
	m = re.search(r'.+', text, re.DOTALL)
	m1 = re.findall(r'.+', text, re.DOTALL)
	print(m.group(), m.span())
	print(m1)
	
	text = "The cost of Python course is $125.	"
	print(text)
	
	print("using '\d+'")
	pat = re.compile(r'\d+')
	m = re.search(pat, text)
	m1 = re.findall(pat, text)
	print(m.group(), m.span())
	print(m1)
	
	print("using '\D+'")
	pat = re.compile(r'\D+')
	m = re.search(pat, text)
	m1 = re.findall(pat, text)
	print(m.group(), m.span())
	print(m1)
	
	text1 = "This is a beautiful day."
	print(text1)
	
	print("using r'^T' pattern")	
	pat = re.compile(r'^T')
	m = re.search(pat, text1)
	m1 = re.findall(pat, text1)
	print(m.group(), m.span())
	print(m1)
	
	print("using r'\.$' pattern")	
	pat = re.compile(r'\.$')
	m = re.search(pat, text1)
	m1 = re.findall(pat, text1)
	print(m.group(), m.span())
	print(m1)
	
	print("using r'\bis\b' pattern")	
	pat = re.compile(r'\bis\b')
	m = re.search(pat, text1)
	m1 = re.findall(pat, text1)
	print(m.group(), m.span())
	print(m1)
	