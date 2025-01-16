# Calculator

def calculator(is_first=True):
    # Print a welcome message if this is the first call to the calculator.
    if is_first:
        print("Welcome to Calculator")

    # Prompt the user to choose an operation.
    operator = input("Choose an operator:\n"
                     "1. Addition\n"
                     "2. Subtraction\n"
                     "3. Multiplication\n"
                     "4. Division\n")

    # Perform the operation based on the user's choice.
    if operator == "1":
        # Addition
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print("Result:", result)

    elif operator == "2":
        # Subtraction
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 - num2
        print("Result:", result)

    elif operator == "3":
        # Multiplication
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 * num2
        print("Result:", result)

    elif operator == "4":
        # Division
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Error: Division by zero is not allowed.")

    else:
        # Invalid operator
        print("Invalid operator. Please try again.")

    # Ask the user if they want to perform another calculation.
    again = input("Do you want to continue? (y/n): ")
    if again.lower() == "y":
        calculator(is_first=False)
    else:
        print("Goodbye")

# Start the calculator.
calculator()
