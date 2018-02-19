def greet(n):
	i = 0
	while i<n:
		i+=1
		print("Hello World")
		
def sumNums(*args):
	sum = 0
	for n in args:
		sum += n
		print(sum)

def myRange(start, stop, step):
	i = start
	while i <=stop:
		yield i
		i += step
