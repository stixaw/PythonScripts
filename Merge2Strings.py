
def stringMerge(str1, str2):
	newStr = ""
	i = 0

	if len(str1) >= len(str2):
		print("Str1 =" + str(len(str1)), len(str2))
		for c in str1:
			if i <= len(str1) -1:
				newStr +=str1[i]
			if i <= len(str2) -1:
				newStr +=str2[i]
			i += 1

	elif len(str2) >= len(str1):
		print("Str2 =" + str(len(str2)), len(str1))
		for c in str2:
			if i <= len(str1)-1:
				newStr +=str1[i]
			if i <= len(str2)- 1:
				newStr +=str2[i]
			i += 1

	print(newStr)


#This is the main program
if __name__ == '__main__':
	stringMerge("abcd", "efg")
	stringMerge("abcd","efgh")
	stringMerge("abc", "efgh")