import os

class Hobbies:
	
	@staticmethod

	def find_hobbyists(hobbies, hobby):
		for name, hobbies in hobbies.items():
			if hobby in hobbies:
				result = name
				return result
	


#This is the main program
if __name__ == '__main__':
	
	hobbies={
	"John":["Print", "Fast"],
	"James":["Run", "Fart"]
	}
	
	print(Hobbies.find_hobbyists(hobbies, 'Fart'))
	
	