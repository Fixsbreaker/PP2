# Example of for loop, break, continue, else, range(), nested loops, and pass statement

# Print each fruit in a fruit list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Loop through the letters in the word "banana"
for x in "banana":
  print(x)

# Exit the loop when x is "banana"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# Exit the loop when x is "banana", but break comes before the print
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# Do not print banana using continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# Using the range() function
for x in range(6):
  print(x)

# Using the start parameter in range()
for x in range(2, 6):
  print(x)

# Increment the sequence with 3 using range()
for x in range(2, 30, 3):
  print(x)

# Else in for loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

# Break the loop when x is 3, and see what happens with the else block
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

# Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# Pass statement in an empty for loop
for x in [0, 1, 2]:
  pass
