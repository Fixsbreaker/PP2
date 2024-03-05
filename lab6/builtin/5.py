def all_true(tup):
    return all(tup)


tup = (True, True, True)
if isinstance(tup, tuple):
    print(all_true(tup))
else:
    raise ValueError('Is not tuple')