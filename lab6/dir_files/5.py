
file_name = input()
list = [1, 2, 3, 4, 5, 6]

with open(file_name, 'w') as file:
    for i in list:
        file.write(str(i) + '\n')
        