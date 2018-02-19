#Lambdas
'''Creating a function normally (using def)' assigns it to a variable automatically.
This is different from the creation of other objects - such as strings and integers
- which can be created on the fly, with out assigning them to a variable.
The same is possible with functions, provided that they are created using LAMBDA syntax.
Functions created this way are known as anonymous!
This approach is most commonly used when passing a smiple function as an argument
 to another function.
 The syntax:
 lambda keyword followed by a list of arguments, a colon and the expression to evaluate 
 and return.'''
#lambdas are just unnamed functions or assigned to a variable
''' lambdas can only do things that require a single expression -
usually equivalent to a single line of code.'''

def my_func(f, arg):
	result = f(arg)
	print("the result of {}".format(result))
	return result

def polynomial(x):
	result = x**2+5*x+4
	print("Polynomial result: {}".format(result))


#This is the main program
if __name__ == '__main__':
	
	fn = (lambda x: 2*x*x)
	my_func(fn, 5)
	
	polynomial(-4)
	
	fn2 = (lambda x: x**2+5*x+4)
	my_func(fn2, -4)
	
	print((lambda x:x**2+5*x+4)(-4))
	
	a = ((lambda x: x*x)(8))
	print(a)
	
	triple= (lambda x: x*3)
	add = (lambda x,y: x+y)
	result = (add(triple(3),4))
	print("result:{}".format(result))
	
