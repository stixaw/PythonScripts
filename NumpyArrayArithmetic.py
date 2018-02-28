import numpy as np
import os
import sys


if __name__ == '__main__':
	
	arr = np.array([[1,2,3,4],[5,6,7,8]])
	print(arr, type(arr))
	
	print(arr + 10)
	print(arr * arr)
	
	print(arr ** 2)
	
	print(arr - arr)
	print("*"*30)
	
	# Transpose Array
	A= np.arange(25).reshape(5,5)
	print(A)
	print("*"*30)
	print(A.T)
	print("*"*30)
	
	B = np.arange(6).reshape(2,3)
	print(B)
	print("*"*30)
	bt = B.T
	print(bt)
	print("*"*30)
	
	print(np.dot(B, bt))