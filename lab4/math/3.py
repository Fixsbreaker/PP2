import math

num_of_sides = int(input('Input number of sides: '))
length_of_side = float(input('Input the length of a side: '))

area = (pow(length_of_side, 2) * num_of_sides) / (4 * math.tan(math.radians(180 / num_of_sides)))
print(f'The area of the polygon is: {area}')