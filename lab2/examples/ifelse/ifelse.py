# Example of if, elif, else statements

# Basic if statement
a = 33
b = 200
if b > a:
  print("b is greater than a")

# Elif statement
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# Else statement
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Else statement without elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Short hand if
a = 5
b = 10
print("a is greater than b") if a > b else print("b is greater than or equal to a")

# Short hand if else
a = 5
b = 10
print("A") if a > b else print("B") if a == b else print("A and B are not equal")

# Logical operators (and, or, not)
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

if a > b or a > c:
  print("At least one of the conditions is True")

if not a > b:
  print("a is NOT greater than b")

# Nested if statements
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# The pass statement
a = 33
b = 200
if b > a:
  pass
