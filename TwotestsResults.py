import os

class Hobbies:
	
	@staticmethod

	def find_hobbyists(hobbies, hobby):
		result = ""
		for name, hobbies in hobbies.items():
			if hobby in hobbies:
				result = name
		message = ("%s has a hobby called %s" % (result, hobby))
		print(message)


#This is the main program
if __name__ == '__main__':
	
	hobbies={
		"John":["Print", "Fart", "Burp"],
		"James":["Sing", "Fizz", "Dance"]
	}
	
	s1 = "ababcd"
	letters ={}
	
	for c in s1:
		try:
			letters[c] += 1
		except:
			letters[c] = 1

	print(letters)
	
	for k, v in  letters.items():
		if v == 1:
			result = k
			print(result)
			break
	
	Hobbies.find_hobbyists(hobbies, 'Burp')
	Hobbies.find_hobbyists(hobbies, 'Fizz')



	