
#Functional Programming:
#Use of higher order functions. 
#higher order functions take other functions as arguments, or return them as results.
def apply_twice(func, arg):
	result = func(func(arg))
	print("apply_twice result {}".format(result))
	return result

def add_five(x):
	result = x + 5
	print result
	return result

def test(func, arg):
	result = func(func(arg))
	print("Test result: {}".format(result))
	return result

def mult(x):
	output = x * x
	print output
	return output
	
#Pure Functions
'''Functional Programming seeks to use Pure Functions. 
Pure functions hae no side affects and return a value that depends only on their argument'''

#pure:
def pure_function(x,y):
	temp = x + 2 * y
	result = temp/(2*y +y)
	print(" temp = {}, result = {}".format(temp, result))
	return result

#impure:

def impure(arg):
	some_list.append(arg)
	for x in some_list:
		print(x)
'''If your answer to all questions is "yes" then your function is pure
1. Does my function depend only on its arguments and nothing else? Or
Does my function always return the same result given the same arguments?
2. can I run my function anywhere in the script without causing any trouble or 
side effects whatsoever?
3. Can I run my function with the same arguments many times and
still return the same result each time?
4. Is it true that my function does not change anything outside it, 
but only returns something?
5. Can my function be used by other functions or scripts with equal success?'''

def func(x):
	y = x**2
	z = x + y
	print("Func returns {}".format(z))

'''Pure functions Advantages are:
	- easier to reason about and test. 
	- more efficient, (Memoization) the result can be stored and referred to the next time the function
	of that input is needed, reducing the number of times the function is called
	- easier to run in parallel
Disadvantages:
	- majorly complicate the otherwise simple task of I/O, since this appears to inherently require side
	side effects.
	- they can be difficult to write in some situations'''
	


#This is the main program
if __name__ == '__main__':
	
	apply_twice(add_five, 10)
	test(mult, 2)
	
	some_list = []
	
	pure_function(2, 4)
	impure("Peter")
	
	func(2)
	func(2)
	func(4)
	