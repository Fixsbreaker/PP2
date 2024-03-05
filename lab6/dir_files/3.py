import os

path = os.path.abspath(input())
if os.path.exists(path):
    for folder, subfolder, files in os.walk(path):
        print(folder, files)
else:
    raise FileNotFoundError('No such path')

# /Users/alnurkunbolov/PP2_id/PP2/lab6/dir_files 