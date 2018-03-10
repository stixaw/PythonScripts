import sys
import os

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores     

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        grade = 'T'
        avg = sum(self.scores)/len(self.scores)
        
        if avg >= 90:
            grade = 'O'
        elif avg>=80 and avg<90:
            grade = 'E'
        elif avg>=70 and avg<80:
            grade = 'A'
        elif avg>=55 and avg<70:
            grade = 'P'
        elif avg>=40 and avg<55:
            grade = 'D'
        else:
            grade = 'T'
        return grade

if __name__ == "__main__":
	
	line = input().split()
	firstName = line[0]
	lastName = line[1]
	idNum = line[2]
	numScores = int(input()) # not needed for Python
	scores = list( map(int, input().split()) )
	s = Student(firstName, lastName, idNum, scores)
	s.printPerson()
	print("Grade:", s.calculate())
	
#Python condensed:
class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        avg = sum(self.scores)/len(self.scores)
        if avg>=90:
            return 'O'
        elif avg>=80:
            return 'E'
        elif avg>=70:
            return 'A'
        elif avg>=55:
            return 'P'
        elif avg>=40:
            return 'D'
        else:
            return 'T'

#minimal python
class Student(Person, object):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    def calculate(self):
        iAvg = sum(self.scores)/len(self.scores)
        return 'O' if iAvg > 89 else 'E' if iAvg > 79 else 'A' if iAvg > 69 else 'P' if iAvg > 54 else 'D' if iAvg > 39 else 

#java or C#
public char calculate(){
        int avg = 0;
        int sum = 0;
        char grade = '\0';
        for(int i = 0;i<testScores.length;i++){ 
            sum = sum + testScores[i];
        }
        avg = sum/testScores.length;
       if(avg>=90&&avg<=100)
           grade = 'O';
       if(avg>=80&&avg<90)
           grade = 'E';
       if(avg>=70&&avg<80)
           grade = 'A';
       if(avg>=55&&avg<70)
           grade = 'P';
       if(avg>=40&&avg<55)
           grade = 'D';
       if(avg<40)
           grade = 'T';
        return grade;
    }
}