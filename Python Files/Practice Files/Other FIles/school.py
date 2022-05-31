
x = float(input("Enter the 1st number: "))
y = float(input("Enter the 1st number: "))
z = float(input("Enter the 1st number: "))

sum = ((x+y+z)/300)*(100)

if (sum>=90):
    print('You Have Scored "A" Grade with' , sum , '%')
elif (sum>80) and (sum<90):
    print('You Have Scored "B" Grade with' , sum , '%')
else:
    print('You Have Scored "D" Grade with' , sum , '%')
