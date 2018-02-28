import numpy as np
import re
import os
import sys

#Solution 1
'''Write a for loop to print numbers 1 through 100 in ten rows.'''
def tenByTen(a, b):
	for x in range(a, b, 1):
		print x,
		if (x % 10 == 0):
			print

def tenByTenWithNumpy(a,b):
	a = np.arange(a, b, 1).reshape(10,10)
	print(a)
	
#Solution 2
'''Write a for loop to print first 100 even numbers. Make sure the output is in 10 rows and format
the output so that all columns align perfectly.'''
def oneHundredEven():
	for x in range(2, 201, 2):
		print x,
		if (x % 20 == 0):
			print

# Solution 3
'''Write a function isPrime(n), that returns a True if n is a prime number, if not False'''
def isPrime(n):

	result = False
	if n % 2 == 0 & n % 3 == 0:
		result = False;
	for i in range(2, n):
		if n % i == 0:
			result = False
			break;
	else:
		result = True;
	return result

#Solution 4
'''Write a for loop to print Prime numbers between 1 and 1000. Format the output so that all
columns align perfectly.'''
def primeOneThousand():
	count = 1;
	for n in range(1,1000):
		if (isPrime(n)):
			print("{:>3}".format(str(n))),
			count = count +1
			if count == 10:
				print
				count = 1;

#Solution 5
'''Write a function to convert temperature in celsius to fahrenheit'''
def celsiusToFahrenheit(n):
	result = (n * 1.8) + 32
	print(result)
	return result

#Solution 6
'''Write a function to convert temperature in fahrenheit to celsius'''
def fahrenheitToCelsius(n):
	result = (n - 32)/1.8
	print(result)
	return result
	
#Solution 7
'''Convert the following list of Kilometers to miles.
	Conversion: 1 Km = 0.621371 of a Mile.'''
def convertKmToMiles(list):
	for i in list:
		miles = i * 0.621371
		print("%d Km is equal to %d miles"%(i, miles))
		
#Solution 8
'''Write factorial function fact(n) without using recurrsion'''
		
def noRecursionFactorials(n):
	factorial = 1
	if n <= 1:
		return factorial
	else:
		for x in range(1, n + 1):
			print x,
			factorial = factorial * x
	print
	print factorial
	return factorial
	
# Solution 9
'''Write a factorial function factR(n) using recurrsion'''
def factorial(n):
	#with Recursion!
	if n <=1:
		print 1
		return 1
	else:
		print n,
		return n * factorial(n-1)

#Solution 10		
'''Write a function toBinary(n) to convert a decimal number into binary number using
recurrsion.'''
def binaryNum(n):
	#s1 = str(bin(n).strip("0b"))
	s1 = str(bin(n))[2:]
	print s1

binStr =""	

def toBinaryRecursion(n):
	global binStr
	if n <=1:
		binStr = binStr + str(1)
		print 1,
		return 1
	else:
		if n % 2 == 0:
			binStr = binStr + str(0)
			print 0,
		else:
			binStr = binStr + str(1)
			print 1,
		return  toBinaryRecursion(n // 2)

# teachers solution:
def toBinary(n):
	if n>1:
		toBinary(n//2)
	print n % 2,
	
# Solution 11:
'''Write your own mymap() function which works exactly like Python's built-in function
map().'''
def myFun(fn, A):
	result = []
	for x in A:
		result.append(fn(x))
	return result
	
#Solution 12
'''Write your own myreduce() function which works exactly like Python's built-in function
reduce().'''
def myReduce(fn, A):
	result = 0
	for x in A:
		result = fn(result, x)
	return result

#Solution 13
'''Write your own myfilter() function which works exactly like Python's built-in function
filter().'''
def myFilter(fn, A):
	result = []
	for x in A:
		if fn(x):
			result.append(x)
	return result
	
#solution 14
'''Write list comprehensions to produce the following three simple lists
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
[1, 6, 11, 16, 21, 26, 31, 36, 41, 46]'''
def makeLists():
	A = [x for x in range(1,11)]
	B = [x for x in range(1,20,2)]
	C = [x for x in range(1, 47,5)]
	print A
	print B
	print C

#Solution 15
'''Write List comprehensions to produce the following Lists
['P', 'y', 't', 'h', 'o', 'n']
['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]'''

def moreLists():
	A= [x for x in "Python"]
	print A
	B= [x*i for x in ('x',' y', 'z') for i in range(1,5)]
	print B
#Solution 16
'''Write Dictionary comprehensions to produce the following Dictionaries
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}
{'a': 'a', 'b': 'bb', 'c': 'ccc', 'd': 'dddd', 'e': 'eeeee', 'f': 'ffffff'}'''
def makeDicts():
	A = {x: x**3 for x in range(1,10)}
	print A
	str = "abcdef"
	B = {x: x*(str.index(x)+1) for x in str}
	print B


if __name__ == '__main__':
	print(sys.version)
	
	#tenByTen(0, 101)
	#print("="*40)
	#tenByTenWithNumpy(1, 101)
	#oneHundredEven()
	#isPrime(11)
	#isPrime(10)
	#primeOneThousand()
	#celsiusToFahrenheit(0)
	#celsiusToFahrenheit(20)
	#fahrenheitToCelsius(32)
	#fahrenheitToCelsius(68)
	#convertKmToMiles([10,20,30,40,50])
	#facts = factorial(5)
	#print facts
	#noRecursionFactorials(10)
	#binaryNum(156)
	#toBinaryRecursion(156)
	#print "Binary of 156 = " + binStr[::-1]
	#toBinary(156)
	A = [1, 2, 33, 4, 99]
	#print myFun(lambda x:(x+3-2)*4, A)
	#print myReduce(lambda x,y: x+y, A)
	#print myFilter(lambda x: x>2, A)
	#makeLists()
	#moreLists()
	makeDicts()
