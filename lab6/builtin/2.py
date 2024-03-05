def low_up(string):
    low_case = 0
    upper_case = 0

    for i in string:
        if i.islower():
            low_case += 1
        elif i.isupper():
            upper_case += 1
    return low_case, upper_case


input_stream = input()
bullshit = '!@#$%^&*()_+=-/;:?'
if isinstance(input_stream, str):
    for i in input_stream:
        if i.isdigit() or i in bullshit:
            raise ValueError('Digit or bullshit in str')
else:
    raise ValueError('Not str')
ob = low_up(input_stream)
print(f'low_case: {ob[0]}, upper_case: {ob[1]}')