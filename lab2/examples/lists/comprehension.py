# Using a for loop with if condition to create a new list:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# Using list comprehension to achieve the same result in one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)

# Example of list comprehension syntax:
# newlist = [expression for item in iterable if condition == True]

# Example: Only accept items that are not "apple":
newlist = [x for x in fruits if x != "apple"]

# Example with no if statement:
newlist = [x for x in fruits]

# Example using the range() function to create an iterable:
newlist = [x for x in range(10)]

# Example accepting only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]

# Example setting the values in the new list to upper case:
newlist = [x.upper() for x in fruits]

# Example setting all values in the new list to 'hello':
newlist = ['hello' for x in fruits]

# Example using conditions to manipulate the outcome:
newlist = [x if x != "banana" else "orange" for x in fruits]
