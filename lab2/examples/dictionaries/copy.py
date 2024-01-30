# Example of making a copy of a dictionary in Python

# Given dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Make a copy of the dictionary with the copy() method
mydict = thisdict.copy()
print("Copy using copy() method:")
print(mydict)

# Another way to make a copy is to use the built-in function dict()
mydict = dict(thisdict)
print("\nCopy using dict() function:")
print(mydict)
