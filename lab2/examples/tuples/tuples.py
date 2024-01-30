# Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Print the number of items in the tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Tuple items can be of any data type:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# A tuple with strings, integers, and boolean values:
tuple1 = ("abc", 34, True, 40, "male")

# What is the data type of a tuple?
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(thistuple)
