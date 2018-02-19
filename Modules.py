import random as rand
import datetime as dt
import os
import myModule as my


def createRandomNumber():
	ranNum = rand.randint(1,100)
	print(ranNum)
	return ranNum

def createSeqIntList():
	num = 0
	num = int(input("Please enter a number for the sequential list?"))
	x = list(range(num))
	return x

def shuffleList(list):
	print(list)
	rand.shuffle(list)
	print(list)
	
def getNow():
	now = dt.datetime.now()
	return now

def getEnvPath():
	path = os.getenv('PATH')
	print(path)
	
def getCurrentWorkingDirectory():
	cd = os.getcwd()
	print(cd)
	return cd
	


#This is the main program
if __name__ == '__main__':

	my.sumNums(10,20,30,40,50)
	x = my.myRange(1, 20,3)
	print(list(x))