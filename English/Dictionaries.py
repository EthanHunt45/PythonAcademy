# Dictionaries

# The first part is called the key part; it must be unique.
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    # You can use numbers too; the only rule is that they must be unique.
      0  : "July",
      1  : "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

# Accessing dictionary values using keys
print(monthConversions["Jan"])  # Output: January
print(monthConversions["Feb"])  # Output: February

# Using the get() method to retrieve a value by key
print(monthConversions.get("Jan"))  # Output: January

# If there is no key, you can provide a default value.
print(monthConversions.get("Max", 'No key!'))  # Output: No key!
