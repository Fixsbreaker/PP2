# Example of adding a new key-value pair to a dictionary in Python

# Create a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Add a new key-value pair "color": "red" using the update() method
thisdict.update({"color": "red"})

# Print the updated dictionary
print(thisdict)
