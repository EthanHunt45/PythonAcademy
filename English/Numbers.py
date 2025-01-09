# Numbers
from math import *  # A module that provides mathematical functions

# We can directly print an integer.
print(2)  # Outputs 2.

# We can also print a decimal number.
print(2.01034)  # Outputs 2.01034.

# Mathematical operations follow the order of precedence.
print(3 - 4.5 * 2)  # Multiplication happens first: 4.5 * 2 = 9. Then subtraction: 3 - 9 = -6.
print((3 - 4.5) * 2)  # Parentheses are calculated first: 3 - 4.5 = -1.5. Then multiplication: -1.5 * 2 = -3.

# The modulus operator (%) gives the remainder of a division.
print(10 % 3)  # 10 divided by 3 leaves a remainder of 1.

# Variables can be used in mathematical operations.
my_num = 4  # An integer variable
my_num2 = 2  # Another integer variable
print(my_num + my_num2)  # Outputs 6 (4 + 2).

# Numbers can be converted to strings and concatenated with text.
print(str(my_num) + " is my favorite number")  # Without str(), this would cause an error.

# The abs() function calculates the absolute value of a number.
negative_num = -5  # A negative number
print(abs(negative_num))  # Absolute value: |-5| = 5.

# The pow() function calculates the power of a number.
num = 3
print(pow(num, 2))  # 3 raised to the power of 2 = 9.

# The max() function finds the largest value in a list.
print(max(3, 2, 5, 7))  # The largest number is 7.

# The min() function finds the smallest value in a list.
print(min(3, 2, 5, 7))  # The smallest number is 2.

# The round() function rounds a number to the nearest integer.
print(round(3.86))  # Rounds 3.86 to 4.

# The floor() function rounds a number down to the nearest integer.
print(floor(3.86))  # Rounds down to 3.

# The ceil() function rounds a number up to the nearest integer.
print(ceil(3.86))  # Rounds up to 4.

# The sqrt() function calculates the square root of a number.
print(sqrt(4))  # The square root of 4 is 2.
