# Lists and Tuples

# Here, I created a list of friends. This list stores the names of my friends.
friends = ["Erinc", "Bahar", "Defne", "Berke", "Bahar", "Yaren"]

# Lists can contain different types of data: a string, a boolean, and an integer.
List = ["Name", True, 2]

# We can also create a list that only contains numbers.
numbers = [3, 2, 1]

# I am printing a specific element from the list. In this case, it selects index 1 and prints "Bahar".
print(friends[1])

# I am printing the last element of the list. I can do this using a negative index.
print(friends[-1])

# I am printing a specific range from the list. It selects and prints elements from index 1 to 3 (3 not included).
print(friends[1 : 3])

# I am finding the index of the first occurrence of "Bahar" in the list.
print(friends.index("Bahar"))

# I am counting how many times "Bahar" appears in the list.
print(friends.count("Bahar"))

# I am sorting the list alphabetically.
friends.sort()
print(friends)

# I am reversing the order of the list.
friends.reverse()
print(friends)

# I am copying the list and creating a new one.
friends2 = friends.copy()
print(friends2)

# I am changing a specific element in the list. I replace the element at index 0 with "Erinc".
friends[0] = "Erinc"
print(friends[0])

# I am extending the list by appending another list at the end.
friends.extend(numbers)
print(friends)

# I am creating a new list called "best_players" and adding elements to it.
best_players = ["Messi", "Ronaldo"]
best_players.append("Neymar")
print(best_players)

# I am inserting an element at a specific position in the list. "Quaresma" is added to the beginning.
best_players.insert(0, "Quaresma")
print(best_players)

# I am removing an element from the list. In this case, I remove "Ronaldo".
best_players.remove("Ronaldo")
print(best_players)

# I am removing the last element of the list.
best_players.pop()
print(best_players)

# I am clearing all elements from the list.
best_players.clear()
print(best_players)

# Here, I am creating a tuple, which is an immutable data structure.
coordinates = (3, 4)

# I am printing a specific element from the tuple. I select the element at index 1.
print(coordinates[1])
