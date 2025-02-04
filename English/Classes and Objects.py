# Defining a class named 'Person'
class Person:
    def __init__(self, name, age):
        # Initializing attributes
        self.name = name
        self.age = age

    # Method to check if the person is old
    def is_old(self):
        if self.age <= 65:
            return False
        else:
            return True

# Creating an instance of Person
person1 = Person("John", 25)
print(person1.name)  # Prints the person's name
print(person1.age)   # Prints the person's age
print(person1.is_old())  # Checks if the person is old (False)

person2 = Person("Karen", 70)
print(person2.name)  # Prints the person's name
print(person2.age)   # Prints the person's age
print(person2.is_old())  # Checks if the person is old (True)

# Creating a subclass named 'Student' that inherits from 'Person'
class Student(Person):
    def __init__(self, name, age, major, gpa):
        super().__init__(name, age)  # Calling the constructor of the parent class
        self.major = major  # Initializing new attribute 'major'
        self.gpa = gpa  # Initializing new attribute 'gpa'

    # Method to check if the student is on the honor roll
    def is_on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

# Creating an instance of Student
student = Student("Erinc", 21, "Computer Engineering", 3.5)
print(student.name)  # Prints the student's name
print(student.age)   # Prints the student's age
print(student.major) # Prints the student's major
print(student.gpa)   # Prints the student's GPA
print(student.is_old())  # Checks if the student is old (False)
print(student.is_on_honor_roll())  # Checks if the student is on the honor roll (True)
