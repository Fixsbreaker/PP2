import math

def vol(radius):
    return (4/3 * math.pi * (radius ** 3))

radius = int(input())
print(vol(radius))
