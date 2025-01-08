# Strings

name = 'Besiktas'
print(name)

# .upper() function converts all the letters in a string to uppercase.
name = name.upper()
print(name)
# .isupper() and .islower() return a boolean value.
# They check whether all characters are uppercase or lowercase, respectively.
print('Name is all upper characters now. True or False? --> ' + str(name.isupper()))
print('Name is all lower characters now. True or False? --> ' + str(name.islower()))

# .lower() function converts all the letters in a string to lowercase.
name = name.lower()
print(name)
print('Name is all upper characters now. True or False? --> ' + str(name.isupper()))
print('Name is all lower characters now. True or False? --> ' + str(name.islower()))

# len() calculates the length of a string, including spaces and special characters.
name = 'I am learning Python'
print(len(name))  # Since it counts spaces as characters, the length is 20 (17 letters and 3 spaces).

# Index refers to the position of a character. It starts from 0.
job = 'Computer Engineer'
# The number inside [] indicates the index of the character in the string. The first character is always at index 0.
print(job[4])
# .index() finds the starting index of the letter or word we are searching for in the string.
print(job.index('r'))
print(job.index('Engineer'))

# .replace() allows us to replace a character, group of characters, or a word in the string.
job = 'Computer Engineer'
job = job.replace('Computer Engineer', 'Farmer')
print(job)
