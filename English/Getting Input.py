#Getting Inputs

# Asks the user for their name and greets them.
name = input("Enter your name: ")  # input() is used to take user input as a string.
print("Hello, " + name + "!")  # Prints a greeting with the user's name.

# Asks the user for their age and displays it.
age = int(input("Enter your age: "))  # input() takes a string; we convert it to an integer using int().
print("You are " + str(age) + " years old.")  # Converts the number back to string for concatenation.

# A simple calculator: Adds two numbers.
num1 = int(input("Enter first number: "))  # Takes the first integer input from the user.
num2 = int(input("Enter second number: "))  # Takes the second integer input from the user.
toplam = num1 + num2  # Adds the two numbers.
print("Your summation is: " + str(toplam))  # Prints the result of the addition.

# The above calculator works only with integers.
# To handle decimal numbers (float), we can use float instead of int.

num1 = float(input("Enter first number: "))  # Takes the first decimal number input.
num2 = float(input("Enter second number: "))  # Takes the second decimal number input.
toplam = num1 + num2  # Adds the two decimal numbers.
print("Your summation is: " + str(toplam))  # Prints the result of the addition.
