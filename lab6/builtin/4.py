import time


num = input()
miliseconds = input()
try:
    num = int(num)
    milli = int(miliseconds)
    seconds = milli / 1000
    time.sleep(seconds)
    print(f'Square root of {num} after {miliseconds} miliseconds is {pow(num, 0.5)}')
except ValueError:
    raise ValueError('Not int')