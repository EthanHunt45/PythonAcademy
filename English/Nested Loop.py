# 2D list (nested list)
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# The first index refers to the row index, the second refers to the column index.
print(numbers[0][2])  # Prints the element at row 0, column 2 (Output: 3)

# Looping through each row in the 2D list
for row in numbers:
    print(row)  # Prints each row

# Nested loop to access each element in the 2D list
for row in numbers:
    for col in row:
        print(col)  # Prints each element in the matrix
