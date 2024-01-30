# Example of creating a dictionary containing three dictionaries

# Method 1: Creating a dictionary that contains three dictionaries
myfamily = {
  "child1": {
    "name": "Emil",
    "year": 2004
  },
  "child2": {
    "name": "Tobias",
    "year": 2007
  },
  "child3": {
    "name": "Linus",
    "year": 2011
  }
}

# Method 2: Creating three dictionaries and then creating a dictionary that contains them
child1 = {
  "name": "Emil",
  "year": 2004
}
child2 = {
  "name": "Tobias",
  "year": 2007
}
child3 = {
  "name": "Linus",
  "year": 2011
}

myfamily_method2 = {
  "child1": child1,
  "child2": child2,
  "child3": child3
}

# Accessing items in nested dictionaries
print("Name of child 2 using Method 1:", myfamily["child2"]["name"])
print("Name of child 2 using Method 2:", myfamily_method2["child2"]["name"])
