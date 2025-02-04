# 'a' (append) mode adds content to an existing file without deleting previous data.
employee_file = open("employees.txt", "a")

# Writing a new employee record to the file
new_employee = employee_file.write("\nBahar - Computer Engineer")

# Closing the file after writing
employee_file.close()

# 'w' (write) mode overwrites the entire file, deleting previous content.
employee_file = open("employees.txt", "w")

# Writing a new employee record (this will erase the previous content)
new_employees = employee_file.write("\nBahar - Computer Engineer")

# Closing the file
employee_file.close()
