# Data Types and Variables

# String type variables are stored within " ", while number type variables don't require this.
character_name = "Erinc"
character_age = 21
print(character_name)
print(character_age)

# Here, the variables are being updated, meaning we can update a variable later.
character_name = "Messi"
character_age = 38

# The + operator is used to concatenate strings while printing.
# Since character_age is a number and not a string, it is converted to a string using str().
print("Name is " + character_name + " and " + str(character_age) + " years old.")

# Alternatively, f-strings can be used.
print(f"Name is {character_name} and {character_age} years old.")

# Numbers can also be written in decimal format.
character_age = 18.01
print(character_age)

# There are 3 types of data:
# Number
number = 1
# String
string = "Hello"
# Boolean
is_True = True

# /n creates a new line.
print('Erinc \nis learning coding')

# /' ensures that the following quote is treated as a literal character.
print('Erinc is learning \'coding\'')
