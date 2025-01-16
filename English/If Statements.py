# If Statements

# These variables represent whether someone is male and/or tall.
is_Male = True
is_Tall = False

# We use a series of conditions to determine the output.
if is_Male and is_Tall:
    print("You are a tall male!")  # If both conditions are true.

elif is_Male or is_Tall:
    print("You are either male or tall!")  # If at least one condition is true.

elif is_Male and not is_Tall:
    print("You are a short male!")  # If male but not tall.

elif not is_Male and is_Tall:
    print("You are a tall female!")  # If not male but tall.

else:
    print("None!")  # If none of the conditions are met.

# This function finds the maximum value among three numbers provided by the user.
def find_max():
    # Input three numbers and store them in a list.
    numbers = [float(input("Enter first number: ")), float(input("Enter second number: ")), int(input("Enter third number: "))]

    # Compare the numbers to find the largest one.
    if numbers[0] >= numbers[1] and numbers[0] >= numbers[2]:
        return numbers[0]  # First number is the largest.
    elif numbers[1] >= numbers[0] and numbers[1] >= numbers[2]:
        return numbers[1]  # Second number is the largest.
    elif numbers[2] >= numbers[1] and numbers[2] >= numbers[0]:
        return numbers[2]  # Third number is the largest.
    else:
        return 'Null'  # No valid result.

# Call the function and print the result.
print(find_max())
