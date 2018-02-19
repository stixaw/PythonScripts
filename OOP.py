class Person:
	
	def __init__(self, firstName, lastName, age):
		self.firstName = firstName
		self.lastName = lastName
		self.name = firstName + " " + lastName
		self.age = age
	
	def changeAge(self, age):
		self.age = age
	
	def __str__(self):
		result =  self.name + '--' + str(self.age)
		return result
#------------------------------------------------------------
class Address:
	def __init__(self, street, city, state):
		self.street = street
		self.city = city
		self.state = state
	
	def changeCity(self, city):
		self.city = city
	
	def changeStreet(self, street):
		self.street = street
		
	def changeState(self, state):
		self.state = state
	
	def __str__(self):
		result =  str(self.street) + '--' + self.city+ '--' + self.state
		return result
	

#------------------------------------------------------------

class Student(Person, Address):
	
	def __init__(self, firstName, lastName, age, grade, gpa, street, city, state):
		Person.__init__(self,  firstName, lastName, age)
		Address.__init__(self, street, city, state)
		self.grade = grade
		self.gpa = gpa
	
	def changeGrade(self, grade):
		self.grade = grade
	
	def changeGpa(self, gpa):
		self.gpa = gpa
	
	def __str__(self):
		result = Person.__str__(self) + '--' + str(self.grade) + '--' + str(self.gpa) + '--' + Address.__str__(self)
		return result
	

#This is the main program
if __name__ == '__main__':
	
	p1 = Person("John", "Smith",  20)
	p1.changeAge(34)
	print(p1)
	s1 = Student("James", "Jones", 18, 12, 3.2, "East La Salle", "Brigham City", "Utah")
	s2 = Student("Peter", "Pumpkineater", 22, 12, 4.0, "49th Street", "New York City", "New York")
	print(s2)
	s2.changeGpa(3.8)
	print(s2)
	s2.changeAge(21)
	print(s2)
	s1.changeCity("Colorado Springs")
	s1.changeState("Colorado")
	print(s1)
	