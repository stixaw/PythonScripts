import re
import os
import sys


#This is the main program
if __name__ == '__main__':
	
	text = "123-4567 is my telephone."
	
	pat = re.compile(r'(?P<first3>[\d]{3})-(?P<last4>[\d]{4})')
	m = re.search(pat, text)
	m1 = re.findall(pat, text)
	print(m.group(), m.groups(), m.group('first3'), m.group('last4'))
	print(m1)
	
	pat = re.compile(r'[\d]{3}-[\d]{4}')
	m = re.search(pat, text)
	m1 = re.findall(pat, text)
	print(m.group())
	print(m1)
	
	pat = re.compile(r'([\d]{3})-([\d]{4})')
	m = re.search(pat, text)
	m1 = re.findall(pat, text)
	print(m.group(), m.groups(), m.group(1), m.group(2))
	print(m1)