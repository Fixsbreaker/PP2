def revers(number):
    for i in range(number, -1, -1):
        yield i


num = int(input())
rev = revers(num)

for i in rev:
    print(i)