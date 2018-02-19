import sys
import os


#Given an array of integers, can you find the sum of its elements?

def simpleArraySum(n, ar):
	sum = 0
	for num in ar:
		sum += num
	print(sum)
	return(sum)
	
def solve(a0, a1, a2, b0, b1, b2):
    aScore = (a0 > b0) + (a1 > b1) + (a2 > b2)
    bScore = (b0 > a0) + (b1 > a1) + (b2 > a2)
    result = "{}{}".format(aScore, bScore)
    return result

#given a start and stop of an range return only the odd numbers:
def oddNumbers(l,r):
    x = []
    for num in range(l, r+1):
        if num % 2 != 0:
            x.append[num]
    return x

# Declare second integer, double, and String variables.
# Read and save an integer, double, and String to your variables.
# Print the sum of both integer variables on a new line.
# Print the sum of the double variables on a new line.
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
def dataTypes():
	i = 4
	d = 4.0
	s = 'HackerRank '

	i2 = int(input('Enter a number'))
	d2 = float(input('Enter a floating number'))
	s2 = input('enter a string that starts with a verb')

	print( i + i2)
	print(d + d2)
	print( "{}{}".format(s, s2))

def arrayRotation( d, k):
	arr = []
	ksplit = k.split()
	for i in ksplit:
		arr.append(int(i))
	if d > 0:
		nlist = arr[d:]
		nlist.extend (arr[:d])
	elif d < 0:
		nlist = arr[-d:]
		nlist.extend (arr[:-d])
	else:
		nlist = arr
	print(nlist)

def listRotation(d,arr):
	if d > 0:
		nlist = arr[d:]
		nlist.extend (arr[:d])
	elif d < 0:
		nlist = arr[-d:]
		nlist.extend (arr[:-d])
	else:
		nlist = arr
	print(nlist)
	
def arrayRotate( d, k):
	str1 = ""
	arr = [int(x) for x in str(k)]
	print(arr)
	if d > 0:
		nlist = arr[d:]
		nlist.extend (arr[:d])
	elif d < 0:
		nlist = arr[-d:]
		nlist.extend (arr[:-d])
	else:
		nlist = arr
	print(nlist)
	for i in nlist:
		if len(str1) == 0:
			str1 += str(i)
		else:
			str1 += " " + str(i)
	print( str1 )
		

	


#This is the main program
if __name__ == '__main__':

	meal_cost = float(input("type in the meal cost").strip())
	tip_percent = int(input("type in tip percent, just the number").strip())
    tax_percent = int(input("type in the tax rounded to nearest dollar).strip())
    
    tip_dec = tip_percent/100
    tax_dec = tax_percent/100
    
    tip = meal_cost * tip_dec
    tax = meal_cost * tax_dec
    total = meal_cost + tip + tax
    totalcost = int(round(total))
    
    print("The total meal cost is {} dollars.".format(totalcost))


