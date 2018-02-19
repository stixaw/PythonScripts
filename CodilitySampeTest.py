def solution(A):
	arr = sorted(A)
	myList = list(range(1,len(arr)+2))
	print(myList)
	result = min(set(myList)-set(arr))
	print("this is a debug message: value of result: " + str(result))
	return result


#This is the main program
if __name__ == '__main__':
	solution([1,3,4,5,6])
	solution([1,2,3])
	solution([-1, -2])