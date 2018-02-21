''' Regular Expressions'''
import re
import os
import sys


#This is the main program
if __name__ == '__main__':
	
	str1="This is a string - not a paragraph"
	
	m = re.search(r'is', str1)
		
	print(m.group())
	print(m.start(), m.end())
	print(m.span())
	print("-" * 50)
	
	#beginning of the string only
	print(re.match(r'is', str1))
	m1 = re.match(r'Th', str1)
	print(m1.group(), m1.start(), m1.end(), m1.span())
	print("-" * 50)
	
	text = "abararabarabar"
	r = re.findall(r'ar', text)
	print len(r)
	print r,
	print
	print "-" * 50
	
	rit = re.finditer(r'ar', text)
	print rit
	for i in rit:
		print(i.group(), i.start(), i.end())
	print(sys.version)
	
	print re.sub(r'ar', 'ti', text)
	print re.sub(r'ar', 'ti', text, count=2)
	
	pat = re.compile(r'ba')
	print re.findall(pat, text)
	
	text3 = "akaks ksdkdkd; aksakks: ajsjss, shshs; ususu;    hshs"
	test = list(text3.split())
	print test 
	
	print re.split(r'[ ;:,]\s*', text3)