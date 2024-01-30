# Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# A set with strings, integers, and boolean values:
set1 = {"abc", 34, True, 40, "male"}
print(type(set1))

# Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)
