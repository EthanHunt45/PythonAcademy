# Mad Libs Game

# Mad Libs is a fill-in-the-blank game based on word types.
# A story template is prepared with certain words left blank.
# The player is asked for words of specific types (e.g., adjective, noun, verb).
# These words are inserted into the blanks of the story template.
# The resulting story is usually funny and entertaining.
# This game is a great way to have fun while learning Python basics!

# Game start message
print("Welcome to Mad Libs Game!")
print("We will ask for some words to create a funny story.\n")

# Gathering inputs from the user
day = input("What is your favorite day of the week? ")
age = input("Your age: ")
name = input("Your name: ")
food = input("Your favorite food: ")
place = input("A place you like: ")
animal = input("Your favorite animal: ")
verb = input("A verb (action): ")
adjective = input("An adjective: ")

# Story template
story = f"""
Once upon a time, on a {adjective} {day}, a {age}-year-old named {name} woke up feeling very hungry.
{name} decided to eat {food} for breakfast, but realized there was none left!
So, {name} packed their bag and went to {place}.
On the way, {name} saw a {animal} trying to {verb}. It was the funniest thing they had ever seen!
{name} laughed so hard that everyone around started laughing too. 
And that’s how {name}'s {day} became the most {adjective} day ever!
"""

# Output the story
print("\nHere is your Mad Libs story:\n")
print(story)
