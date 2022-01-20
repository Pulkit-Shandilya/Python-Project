print('Type the sides in any order: -')
x = float(input('Side 1: '))
y = float(input('Side 2: '))
z = float(input('Side 3: '))

if (x == y == z):
    print('This is a Equilateral Triangle!')
elif (x == y) or (x == z) or (y == z):
    print('This is a Isoceles Triangle!')
else:
    print('This is a Scalene Triangle!')

'''
hello
'''