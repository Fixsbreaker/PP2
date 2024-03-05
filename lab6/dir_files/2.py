import os

path = os.path.abspath(input())
print('Exist: ', os.access(path, os.F_OK))
print('Readable:', os.access(path, os.R_OK))
print('Writable:', os.access(path, os.W_OK))
print('Executable:', os.access(path, os.X_OK))

"""
os.F_OK: Tests existence of the path.
os.R_OK: Tests readability of the path.
os.W_OK: Tests writability of the path.
os.X_OK: Checks if path can be executed.
"""