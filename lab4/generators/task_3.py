def divisible(number):
    for item in range(number + 1):
        if item % 3 == 0 and item % 4 == 0:
            yield item


num = int(input())
div = divisible(num)

for i in div:
    print(i)