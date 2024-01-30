# Example of printing key names and values from a dictionary in Python

# Given dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Print all key names in the dictionary, one by one
print("Print all key names:")
for x in thisdict:
  print(x)

# Print all values in the dictionary, one by one
print("\nPrint all values:")
for x in thisdict:
  print(thisdict[x])

# Use the values() method to return values of a dictionary
print("\nUse values() method:")
for x in thisdict.values():
  print(x)

# Use the keys() method to return the keys of a dictionary
print("\nUse keys() method:")
for x in thisdict.keys():
  print(x)

# Loop through both keys and values, using the items() method
print("\nLoop through both keys and values:")
for x, y in thisdict.items():
  print(x, y)
