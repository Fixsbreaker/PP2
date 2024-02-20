def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2


num1 = int(input())
num2 = int(input())
sq = squares(num1, num2)

for i in sq:
    print(i)