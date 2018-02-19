#This is the main program
if __name__ == '__main__':
		
	squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
	print(squares[2:5])
	print(squares[3:8])
	print(squares[0:1])
	print(squares[7:5:-1])
	
	nums = [i*2 for i in range(10)]
	print(nums)
	
	evens = [i**2 for i in range(10) if i**2 % 2 == 0]
	print(evens)
	
	a = [i for i in range(20) if i%3 ==0]
	print(a)
	
	nums = [4,5,6]
	msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])
	print(msg)
	
	print("{0}{1}{0}".format("abra", "cad"))
	
	nums = (1,2,3,4,0,2,8,1)
	print(min(nums))
	print(max(nums))
	print(sum(nums))
	result = 4/7
	print(round(result,2))
	print(round(result,3))
	
	a = min([sum([11,22]), max(abs(-30), 2)])
	print(a)
	
	nums = [55, 44, 33, 22, 11, 66]
	
	if all([i>5 for i in nums]):
		print("All larger than 5")
		
	if any([i%2 == 0 for i in nums]):
		print("At least one is even")
	
	for v in enumerate(nums):
		print(v)
		
	nums = [-1, 2, -3, 4, -5]
	if all ([abs(i) < 3 for i in nums]):
		print(1)
	else:
		print(2)

