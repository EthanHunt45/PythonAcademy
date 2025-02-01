# Looping through a string
for letter in "Python":
    print(letter)  # Prints each letter in "Python"

# List of friends
friends = ["Erinc", "Bahar", "Defne", "Berke", "Bahar", "Yaren"]
# We can name 'friend' however we want, e.g., name, word...
for friend in friends:
    print(friend)  # Prints each friend's name

# Looping through a list using an index
for index in range(len(friends)):
    if friends[index] == "Erinc":
        print("He is Erinc.")  # Prints a special message if the name is "Erinc"
    else:
        print("Not Erinc")  # Prints this message for other names

# Looping through a range (not including 10)
for index in range(10):
    print(index)  # Prints numbers from 0 to 9

# Looping through a range (including 3 but not 10)
for index in range(3, 10):
    print(index)  # Prints numbers from 3 to 9

# Function to calculate exponentiation
def exponent_function():
    result = 1
    base_num = int(input("Enter base number: "))  # User input for base number
    pow_num = int(input("Enter exponent number: "))  # User input for exponent number
    for i in range(pow_num):
        result = float(result * base_num)  # Multiplying base number repeatedly
    return result  # Returning the final result

# Calling the function and printing the result
print(exponent_function())
