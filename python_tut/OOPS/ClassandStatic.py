# Python program to demonstrate 
# use of class method and static method. 
from datetime import date 

class Person: 
	def __init__(self, name=None, age=None):
		self.name = name 
		self.age = age 
	
	# a class method to create a Person object by birth year. 
	@classmethod
	def fromBirthYear(cls, name, year): 
		return cls(name, date.today().year - year) 
	
	# a static method to check if a Person is adult or not. 
	@staticmethod
	def isAdult(age): 
		return age > 18

person1 = Person('mayank', 21) 
person2 = Person.fromBirthYear('mayank', 1996)
person3= Person('Anirudh')

'''The setattr() function takes three parameters:

	object - object whose attribute has to be set
    name - attribute name
    value - value given to the attribute
'''
setattr(person3,'age',30)

print (person1.age)
print (person2.age )
print (person3.age )



# print the result 
print (Person.isAdult(22) )
