file_name = input()
counter = 0

try:
    with open(file_name, 'r') as file:
        for line in file.readlines():
            counter += 1
    print(counter)
except FileNotFoundError:
    print('No such file')

# 4.py