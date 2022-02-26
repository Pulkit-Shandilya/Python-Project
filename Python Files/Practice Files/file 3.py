
x = float(input("Enter the 1st number: "))

if ((x % 5) == 0):
    print(int(x) , ' the number is Divisible by 5')
elif ((x % 11) == 0):
    print(int(x) , ' the number is Divisible by 11')
else:
    print(int(x) , ' is not disvible by 5 or 11')
