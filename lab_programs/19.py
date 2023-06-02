# String Methods
string = "Hello, World!"

# Length of the string
length = len(string)
print("Length of the string:", length)

# Convert string to uppercase
uppercase = string.upper()
print("Uppercase string:", uppercase)

# Convert string to lowercase
lowercase = string.lower()
print("Lowercase string:", lowercase)

# Count occurrences of a substring
count = string.count("o")
print("Number of 'o' in the string:", count)

# List Methods
my_list = [1, 2, 3, 4, 5]

# Length of the list
length = len(my_list)
print("Length of the list:", length)

# Append an element to the list
my_list.append(6)
print("List after appending element:", my_list)

# Sort the list
my_list.sort()
print("Sorted list:", my_list)

# Reverse the list
my_list.reverse()
print("Reversed list:", my_list)

# Dictionary Methods
my_dict = {"name": "John", "age": 25, "city": "New York"}

# Length of the dictionary
length = len(my_dict)
print("Length of the dictionary:", length)

# Get all keys in the dictionary
keys = my_dict.keys()
print("Keys in the dictionary:", keys)

# Get all values in the dictionary
values = my_dict.values()
print("Values in the dictionary:", values)

# Check if a key exists in the dictionary
key_exists = "age" in my_dict
print("Does 'age' exist in the dictionary?", key_exists)

# Remove a key-value pair from the dictionary
my_dict.pop("age")
print("Dictionary after removing 'age':", my_dict)
