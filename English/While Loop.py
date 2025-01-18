# While Loop

# Initialize a variable
i = 1
numbers = []

# A while loop that continues as long as the condition is true
while i <= 10:
    # Append the current value of i to the list
    numbers.append(i)
    # Increment i by 2
    i = i + 2

# Print the resulting list
print(numbers)

# Initialize variables
x = 10
numbers1 = []  # List to hold numbers divisible by 10
numbers2 = []  # List to hold numbers not divisible by 10

# A while loop that continues as long as x is less than or equal to 100
while x <= 100:
    # Check if x is divisible by 10
    if x % 10 == 0:
        # Add x to numbers1 if divisible by 10
        numbers1.append(x)
        x = x + 2
    else:
        # Add x to numbers2 if not divisible by 10
        numbers2.append(x)
        x = x + 2

# Print the lists
print(numbers1)  # List of numbers divisible by 10
print(numbers2)  # List of numbers not divisible by 10
