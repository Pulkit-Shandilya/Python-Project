x = float(input("Enter the 1st number: "))
y = float(input("Enter the 2nd second: "))
z = float(input("Enter the 3rd second: "))

if (x > y):
    if (x > z):
        largest = x
elif (y > x):
    if (y > z):
        largest = y
    else:
        largest = z

print('Largest Number is ' , int(largest))