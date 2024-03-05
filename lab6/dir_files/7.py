file_to_copy = input()
file_to_paste = input()

try:
    with open(file_to_copy, 'r') as file1:
        data = file1.read()

    with open(file_to_paste, 'w') as file2:
        file2.write(data)
except FileNotFoundError:
    print('somthing went wrong')