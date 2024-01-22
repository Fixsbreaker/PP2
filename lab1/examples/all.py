# HOME
print("Hello, World!")


# Intro
print("Hello, World!")

#  syntax
# Correct indentation
if 5 > 2:
    print("Five is greater than two!")

# Incorrect indentation (Syntax Error)
"""
if 5 > 2:
print("Five is greater than two!") 
"""

# Varying number of spaces in the same block (Syntax Error)
if 5 > 2:
    print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 

# Inconsistent indentation in the same block (Syntax Error)
"""
if 5 > 2:
    print("Five is greater than two!")
        print("Five is greater than two!")
"""

# Comments
# Single-line comment
# This is a comment
print("Hello, World!")

# Single-line comment at the end of a line
print("Hello, World!")  # This is a comment

# Comment to prevent code execution
# print("Hello, World!")
print("Cheers, Mate!")

# Multi-line comments using multiple single-line comments
# This is a comment
# written in
# more than just one line
print("Hello, World!")

# Multi-line comment using a multiline string
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

# variables 
# Creating variables
x = 5
y = "John"
print(x)
print(y)

# Variables can change type
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Printing variable types
print(type(x))  # <class 'str'>
print(type(y))  # <class 'int'>
print(type(z))  # <class 'float'>

# variables names
# Legal variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal variable names
# 2myvar = "John"   # Cannot start with a number
# my-var = "John"   # Cannot contain hyphens
# my var = "John"   # Cannot contain spaces

#multiple values 
# Multiple values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#output variables
# Output a single variable
x = "Python is awesome"
print(x)

# Output multiple variables using commas
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# Concatenate and output multiple variables using the + operator
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# Mathematical operation with numbers
a = 5
b = 10
print(a + b)

# Error when combining a string and a number
# x = 5
# y = "John"
# print(x + y)

# Output multiple variables of different data types using commas
x = 5
y = "John"
print(x, y)


# global variables
# Create a variable outside of a function and use it inside the function
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

# Create a variable inside a function with the same name as the global variable
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

# The global variable remains unchanged outside the function
print("Python is " + x)

# data types
# Print the data type of the variable x
x = 5
print(type(x))

# Setting the Data Type

# Different data types and their examples
x = "Hello World"          # str
x = 20                      # int
x = 20.5                    # float
x = 1j                      # complex
x = ["apple", "banana", "cherry"]  # list
x = ("apple", "banana", "cherry")  # tuple
x = range(6)                # range
x = {"name": "John", "age": 36}    # dict
x = {"apple", "banana", "cherry"}  # set
x = frozenset({"apple", "banana", "cherry"})  # frozenset
x = True                    # bool
x = b"Hello"                # bytes
x = bytearray(5)            # bytearray
x = memoryview(bytes(5))    # memoryview
x = None                    # NoneType

# Setting the Specific Data Type using constructor functions
x = str("Hello World")      # str
x = int(20)                  # int
x = float(20.5)              # float
x = complex(1j)              # complex
x = list(("apple", "banana", "cherry"))   # list
x = tuple(("apple", "banana", "cherry"))  # tuple
x = range(6)                 # range
x = dict(name="John", age=36)  # dict
x = set(("apple", "banana", "cherry"))   # set
x = frozenset(("apple", "banana", "cherry"))  # frozenset
x = bool(5)                  # bool
x = bytes(5)                 # bytes
x = bytearray(5)             # bytearray
x = memoryview(bytes(5))     # memoryview

# numbers
# Numeric types in Python

# Integers
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# Floats
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# Floats as scientific numbers
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# casting
# Specify a variable type using casting

# Integers
x = int(1)     # x will be 1
y = int(2.8)   # y will be 2
z = int("3")   # z will be 3

# Floats
a = float(1)   # a will be 1.0
b = float(2.8) # b will be 2.8
c = float("3") # c will be 3.0
d = float("4.2") # d will be 4.2

# Strings
p = str("s1")  # p will be 's1'
q = str(2)     # q will be '2'
r = str(3.0)   # r will be '3.0'

# Print the types of the variables
print(type(x), type(y), type(z))
print(type(a), type(b), type(c), type(d))
print(type(p), type(q), type(r))


# Python Strings
# Displaying a string literal with the print() function
print("Hello")
print('Hello')

# Assigning a string to a variable
a = "Hello"
print(a)

# Multiline strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Slicing strings
b = "Hello, World!"
print(b[2:5])  # Get characters from position 2 to 5 (not included)
print(b[:5])   # Get characters from the start to position 5 (not included)

# String methods: upper(), lower(), strip()
a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.strip())  # Remove whitespace

# String concatenation
a = "Hello"
b = "World"
c = a + b
print(c)
c = a + " " + b  # Add a space between strings
print(c)

# String format() method
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Escape characters
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Other escape characters
print('Hello\tWorld')  # Tab
print('Hello\nWorld')  # New Line
print('Hello\bWorld')  # Backspace
