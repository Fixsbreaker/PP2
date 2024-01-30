# Basic Comparison:
print(10 > 9)
print(10 == 9)
print(10 < 9)

# If-Else Statement:
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Boolean Evaluation with bool() function:
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

# Truthy Values:
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

# Falsy Values:
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# Functions Returning Boolean:
def myFunction():
    return True

print(myFunction())

def myFunction():
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")

# Built-in Function isinstance():
x = 200
print(isinstance(x, int))
