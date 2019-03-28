import os
import sys


def makeRange(n):
	result = (range(1,n+1))
	print(*result,sep="")

def makeLexicon(x,y,z,n):
	result = [[a,b,c] for a in range(x+1) for b in range (y+1) for c in range(z+1) if a+b+c != n]
	print (result)
	
def runnerUp(arr):
	result = sorted(set(arr))[-2]
	print(result)
	
students = [['Harry', 37.21], [Berry, 37.21], ['Tina', 37.2], ['Akrti', 41], ['Harsh', 39]]



if __name__ == '__main__':
