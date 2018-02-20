''' Regular Expressions 2'''
import re
import os
import sys


#This is the main program
if __name__ == '__main__':
	
	text = "aaabbbbbaaabbbbababbababbbbabcad"
	
	# followed by zero or more bs
	print("using ab* repetition")
	pat = re.compile(r'ab*')
	m= re.search(pat, text)
	m1 = re.findall(pat, text)
	print(m.group(), m.span())
	print(m1)
	
	# followed by one or more b
	print("using ab+ repetition")
	pat1 = re.compile(r'ab+')
	m = re.search(pat1,text)
	m1 = re.findall(pat1,text)
	print(m.group(), m.span())
	print(m1)
	
	# followed by zero or one b
	print("using ab? repetition")
	pat3 = re.compile(r'ab?')
	m = re.search(pat3,text)
	m1 = re.findall(pat3,text)
	print(m.group(), m.span())
	print(m1)
	
	# followed by n bs
	print("using ab{2} repetition")
	pat4 = re.compile(r'ab{2}')
	m = re.search(pat4,text)
	m1 = re.findall(pat4,text)
	print(m.group(), m.span())
	print(m1)
	
	# followed by min m and max n bs
	print("using ab{1,3} repetition")
	pat5 = re.compile(r'ab{1,3}')
	m = re.search(pat5,text)
	m1 = re.findall(pat5,text)
	print(m.group(), m.span())
	print(m1)
	
	# followd by min m, unlimited b
	print("using ab{1,} repetition")
	pat6 = re.compile(r'ab{1,}')
	m = re.search(pat6,text)
	m1 = re.findall(pat6,text)
	print(m.group(), m.span())
	print(m1)
	
	# followed by a single non newline character
	print("using ab. repetition")
	pat7 = re.compile(r'ab.')
	m = re.search(pat7, text)
	m1 = re.findall(pat7, text)
	print(m.group(), m.span())
	print(m1)
	
	