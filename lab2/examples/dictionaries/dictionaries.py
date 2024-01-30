# Example of creating and printing a dictionary in Python

# Create and print a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Access a specific value using key
print(thisdict["brand"])

# Dictionaries are ordered in Python 3.7 and later
# Duplicate keys will overwrite existing values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# Get the number of items in the dictionary
print(len(thisdict))

# Values in dictionary items can be of any data type
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(thisdict))

# Using the dict() constructor to create a dictionary
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)
