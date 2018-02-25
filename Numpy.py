import re
import numpy as np
import os
import sys


#This is the main program
if __name__ == '__main__':
	
	a = [1, 2, 3, 4]
	arr1 = np.array(a)
	print(arr1)
	
	b = [5, 6, 7, 8]
	arr2d = np.array([a, b])
	print(arr2d)
	
	print(arr2d.shape)
	
	c= [11, 10, 12, 13]
	arr3d = np.array([a,b,c])
	print(arr3d)
	print(arr3d.shape)
	
	A = np.arange(10)
	print(A)
	
	B = np.arange(5, 50, 3)
	print(B)
	
	C = np.arange(25).reshape(5,5)
	print(C)
	print(C.sum())
	
	x = np.zeros(10)
	print(x)
	print(x.dtype)
	
	y = np.zeros(25).reshape(5,5)
	print(y)
	print(y.dtype)
	
	z= np.ones([5,5])
	print(z)
	print(z.dtype)