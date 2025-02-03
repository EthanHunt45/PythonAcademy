# We must handle exceptions for every possible situation.
try:
    # This will cause a ZeroDivisionError
    value = 10 / 0

    # Asking for user input and converting it to an integer
    number = int(input("Enter a number: "))

    # Printing the entered number
    print(number)

# Handling division by zero error
except ZeroDivisionError as err:
    print(err)  # Prints the error message

# Handling invalid input error (if the user enters a non-numeric value)
except ValueError:
    print("Invalid input")  # Prints an error message for invalid input
