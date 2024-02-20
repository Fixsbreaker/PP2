def square(n):
    for num in range(n):
        yield num ** 2

n = int(input()) 
squares = square(n)
for i in squares:
    print(i, end = " ")