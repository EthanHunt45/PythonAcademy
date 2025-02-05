# Get user input
word = input("Enter a word: ")

# Initialize an empty string for the translation
translation = ""

# Loop through each letter in the input word
for letter in word:
    # Check if the letter is a vowel (a, e, i, o, u)
    if letter.lower() in "aeiou":
        # If the vowel is uppercase, replace it with 'G'
        if letter.isupper():
            letter = "G"
            translation += letter
        # If the vowel is lowercase, replace it with 'g'
        else:
            letter = "g"
            translation += letter
    else:
        # If it's not a vowel, keep the letter unchanged
        translation += letter

# Print the translated word
print(translation)
