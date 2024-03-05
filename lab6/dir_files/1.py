import os

path = os.path.abspath(input())
if os.path.exists(path):
    for folder, subfolder, files in os.walk(path):
        print(folder)
    print('===============================================================')
    for folder, subfolder, files in os.walk(path):
        print(files)
    print('===============================================================')
    for folder, subfolder, files in os.walk(path):
        print(folder, files)
else:
    raise FileNotFoundError('No such path')
