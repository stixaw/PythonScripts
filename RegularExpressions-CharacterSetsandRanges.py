#Regular expressions character sets and ranges
import re
import os
import sys


#This is the main program
if __name__ == '__main__':
	
	text = "xxy xyxyx xaxb xxyy aaxz"
	print("using x[^xy]+ pattern")
	pat1 = re.compile(r'x[^xy]+')
	m = re.search(pat1, text)
	print(m.group(), m.span())
	m1 = re.findall(pat1, text)
	print(m1)
	
	print("using x[xy]+ pattern")
	pat1 = re.compile(r'x[xy]+')
	m = re.search(pat1, text)
	print(m.group(), m.span())
	m1 = re.findall(pat1, text)
	print(m1)
	
	print("using x[xy] pattern")
	pat1 = re.compile(r'x[xy]')
	m = re.search(pat1, text)
	print(m.group(), m.span())
	m1 = re.findall(pat1, text)
	print(m1)
	
	text1 = "This is a sample text. -- with some Punctuation marks!!!"

	print("using '[A-Z][a-z]' pattern")
	pat1 = re.compile(r'[A-Z][a-z]*')
	m = re.search(pat1, text1)
	print(m.group(), m.span())
	m1 = re.findall(pat1, text1)
	print(m1)
	
	print("using '[^.\-! ]' pattern")
	pat1 = re.compile(r'[^.\-! ]+')
	m = re.search(pat1, text1)
	print(m.group(), m.span())
	m1 = re.findall(pat1, text1)
	print(m1)


	