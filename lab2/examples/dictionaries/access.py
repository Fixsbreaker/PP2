# Example of accessing keys, values, and items in a dictionary in Python

# Create a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Access the value of the "model" key
x = thisdict["model"]
# Alternatively, use the get() method
y = thisdict.get("model")

# Print the value of the "model" key
print(x)
print(y)

# Get a list of keys
keys_list = thisdict.keys()
print(keys_list)

# Add a new item to the dictionary and observe the change in keys list
thisdict["color"] = "white"
print(keys_list)  # Updated keys list

# Get a list of values
values_list = thisdict.values()
print(values_list)

# Make a change in the original dictionary and observe the change in values list
thisdict["year"] = 2020
print(values_list)  # Updated values list

# Get a list of key:value pairs (items)
items_list = thisdict.items()
print(items_list)

# Make a change in the original dictionary and observe the change in items list
thisdict["year"] = 2022
print(items_list)  # Updated items list

# Check if a key exists in the dictionary
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
