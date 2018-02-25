import re
import os
import sys


#This is the main program
if __name__ == '__main__':
	
	text= ['1 123 456 7890','123 456 7890','+1 (123) 456 7890', '(123) 456 7890', '123-466-7890', '123.456.7890', '1234567890']
		
	pat = r'(\+?\d?)\s?(\(?\d{3}\)?)[\s\-\.]?(\d{3})[\s\-\.]?(\d{4})'
	patc = re.compile(pat)
	for dt in text:
		m = re.search(patc, dt)
		if m:
			print(m.group(),m.group(1),m.group(2),m.group(3),m.group(4))
	print('-'*40)
	
	text= ['123 456 7890', '(123) 456 7890', '123-466-7890', '123.456.7890', '1234567890']
		
	pat = r'\(?\d{3}\)?[\s\-\.]?\d{3}[\s\-\.]?\d{4}'
	for dt in text:
		m = re.search(pat, dt)
		if m:
			print(m.group())
	print('-'*40)
	
	text= ['123 456 7890', '(123) 456 7890', '123-466-7890', '123.456.7890']
		
	pat = r'\(?\d{3}\)?[\s\-\.]\d{3}[\s\-\.]\d{4}'
	for dt in text:
		m = re.search(pat, dt)
		if m:
			print(m.group())
	print('-'*40)
	
	
	text= ['123 456 7890', '(123) 456 7890', '123-466-7890']
	
	pat = r'\(?\d{3}\)?[\s\-]\d{3}[\s\-]\d{4}'
	for dt in text:
		m = re.search(pat, dt)
		if m:
			print(m.group())
	print('-'*40)
	
	text= ['123 456 7890', '(123) 456 7890']
	
	pat = r'\d{3}\s\d{3}\s\d{4}'
	for dt in text:
		m = re.search(pat, dt)
		if m:
			print("we got the first phone number ", m.group())
			
	pat = r'\(\d{3}\)\s\d{3}\s\d{4}'
	for dt in text:
		m = re.search(pat, dt)
		if m:
			print("we got the second phone number ", m.group())
			
	pat = r'\(?\d{3}\)?\s\d{3}\s\d{4}'
	for dt in text:
		m = re.search(pat, dt)
		if m:
			print(m.group())