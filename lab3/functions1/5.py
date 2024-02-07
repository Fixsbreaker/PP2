from itertools import permutations

def print_permutations(input_string):
    perms = permutations(input_string)
    
    for perm in perms:
        print(''.join(perm))

input_string = input("")
print_permutations(input_string)
