# Remove "banana" using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# Remove "banana" using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# Remove a random item using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# Clear the set using the clear() method:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# Delete the set completely using the del keyword:
thisset = {"apple", "banana", "cherry"}
del thisset  # This will raise an error if you try to print(thisset) after deletion
