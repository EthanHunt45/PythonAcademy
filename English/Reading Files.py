# 'r' means read mode.
employee_file = open('employees.txt', 'r')

# Check if the file is readable (returns a boolean value)
print(employee_file.readable())  # Output: True if readable, False otherwise

# Read and print one line from the file
print(employee_file.readline())  # Reads the first line

# Each time we call readline(), it moves to the next line
print(employee_file.readline())  # Reads the second line

# If we open a file, we must ensure to close it.
employee_file.close()

#### Reading a specific line ####
employee_file = open('employees.txt', 'r')

# Read all lines into a list and print the second line (index 1)
print(employee_file.readlines()[1])  # Prints the second line

employee_file.close()

#### Reading all lines in a loop ####
employee_file = open('employees.txt', 'r')

# Looping through all lines in the file and printing each one
for employee in employee_file.readlines():
    print(employee)

employee_file.close()
