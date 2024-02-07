# from random import randint


# def guess():
#     print('Hello! What is your name?')
#     name = str(input())
#     print(f'Well, {name}, I am thinking of a number between 1 and 20.')
#     num = randint(1, 20)
#     counter = 0
#     while num < 100:
#         print('Take a guess.')
#         per_num = int(input())
#         if per_num < num:
#             print('Your guess is too low.')
#             counter += 1
#         elif per_num > num:
#             print('Your guess is too big.')
#             counter += 1
#         else:
#             print(f'Good job, {name}! You guessed my number in {counter} guesses!')
#             break

# guess()

from random import randint

def guess():
    print('Hello! What is your name?')
    name = input()
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')
    num = randint(1, 20)
    counter = 0
    while True:
        print('Take a guess.')
        per_num = int(input())
        if per_num < num:
            print('Your guess is too low.')
            counter += 1
        elif per_num > num:
            print('Your guess is too big.')
            counter += 1
        else:
            print(f'Good job, {name}! You guessed my number in {counter} guesses!')
            break

guess()
