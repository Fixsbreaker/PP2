def get_even(number):
    for item in range(number + 1):
        if item % 2 == 0:
            yield item


num = int(input())
ev = get_even(num)

for i in ev:
    print(i, end=', ')
