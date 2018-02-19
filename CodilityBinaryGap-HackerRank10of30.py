
def binaryGap(n):
	
	s1 = str(bin(n).strip("0b"))
	print("{} is {} in binary".format(str(n), s1))
	count = 0
	maxGap = 0
	
	sLen = len(s1)
	print("length = {}".format(sLen))
	
	for i in range(sLen):
		if s1[i] == "0":
			count += 1
		if s1[i] == "1":
			count = count
			if maxGap < count:
				maxGap = count
			count = 0
	print(maxGap)
	return(maxGap)

def binaryOnes(n):
	
	s1 = str(bin(n).strip("0b"))
	print("{} is {} in binary".format(str(n), s1))
	count = 0
	maxGap = 0
	
	sLen = len(s1)
	print("length = {}".format(sLen))
	
	for i in range(sLen):
		print(s1[i])
		if s1[i] == "1":
			count += 1
		else:
			count = 0
		if maxGap < count:
			maxGap = count
	print(maxGap)
	return(maxGap)


#This is the main program
if __name__ == '__main__':
	
	binaryGap(146)
	binaryGap(1041)
	binaryGap(1)
	binaryOnes(1)
	binaryOnes(146)
	binaryOnes(13)
	binaryOnes(16)