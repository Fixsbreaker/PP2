import os

path = os.path.abspath(input())

if os.access(path, os.F_OK & os.R_OK & os.W_OK & os.X_OK):
    os.remove(path)
else:
    print('Somthing went wrong')