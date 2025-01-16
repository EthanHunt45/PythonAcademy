# Functions

# This is a simple function definition. The function 'say_hello' prints "Hello World".
def say_hello():
    print("Hello World")  # Prints "Hello World" to the screen.

# We call the function.
say_hello()

# This function takes user input for name and age.
def say_hi():
    # The user's name is taken as input.
    name = input("What is your name?")

    # The user's age is taken as input and converted to an integer.
    age = int(input("What is your age?"))

    # A message is printed to the user with their name and age.
    print("Hello, " + name + "! You are " + str(age) + " years old.")

# We call the function.
say_hi()

# This function takes two parameters: name and age.
def say_hi2(name, age):
    # A message is printed using the parameters provided.
    print("Hello, " + name + "! You are " + str(age) + " years old.")

# We call the function and provide the required parameters.
say_hi2("John", 12)

# This function calculates the cube of a given number.
def cube(number):
    # The cube of the number is calculated and stored in a variable.
    cube = number * number * number

    # The calculated value is returned.
    return cube

# We call the function and print its result.
print(cube(5))  # Prints 125, which is the cube of 5.
