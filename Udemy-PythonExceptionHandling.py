
def divideByModulus():
	num1 = int(input("Enter a valid number"))
	num2 = int(input("Enter a second valid number"))
	
	result=0
	
	try:
		result = ((num1*num2) + 2/(num2%num1))
		print("result =", result)
	except ZeroDivisionError as e:
		print(e)
	except TypeError as t:
		print(t)


## MAIN
if __name__ == '__main__':
	
	divideByModulus()	
	
	
	