'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. 
Store them in a list and find the score of the runner-up.'''

import os
import sys

def findRunnerUP(n, arr):
	result = sorted(list(set(arr)))[-2]
	print result


if __name__ == '__main__':
	findRunnerUP(4, (1,5,2,7))