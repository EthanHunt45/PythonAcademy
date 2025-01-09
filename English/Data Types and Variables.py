# Data Types and Variables

# String variables are defined within double (" ") or single (' ') quotes.
# Number variables do not require quotes.
character_name = "Erinç"  # A variable of type string
character_age = 21  # A variable of type integer
print(character_name)  # Prints the variable: Erinç
print(character_age)  # Prints the variable: 21

# Variables can be updated with new values.
character_name = "Messi"  # New value for the variable: Messi
character_age = 38  # New value for the variable: 38

# The + operator is used to concatenate (combine) strings.
# However, numbers must be converted to strings before concatenation.
# We use the str() function to convert numbers to strings.
print("Name is " + character_name + " and " + str(character_age) + " years old.")
# Output: Name is Messi and 38 years old.

# f-strings provide a more convenient and readable way to concatenate strings.
# Variable names are placed inside curly braces ({}) to include them in the string.
print(f"Name is {character_name} and {character_age} years old.")
# Output: Name is Messi and 38 years old.

# Numbers can also be defined as floating-point (decimal) values.
character_age = 18.01  # A floating-point variable
print(character_age)  # Output: 18.01

# Python has 3 main data types:
# 1. Number: Includes integers (int) and floating-point numbers (float)
number = 1  # An integer
# 2. String: A sequence of characters
string = "Hello"  # A string variable
# 3. Boolean: Represents True or False values
is_True = True  # A boolean variable

# \n is used to create a new line in the output.
print('Erinç \nis learning coding')
# Output:
# Erinç
# is learning coding

# \' is used as an escape character to include a single quote in a string.
print('Erinç \'is learning\' coding')
# Output: Erinç 'is learning' coding
