# Example of updating a key in a dictionary in Python

# Create a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Change the value of the "year" key to 2018
thisdict["year"] = 2018

# Print the updated dictionary
print(thisdict)

# Update the "year" key using the update() method
thisdict.update({"year": 2020})

# Print the dictionary after the update
print(thisdict)
