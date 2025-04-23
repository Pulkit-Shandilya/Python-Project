import math
x,y,sum=int(input("enter the number: ")),0,0
while x>=y:
    sum+= y/math.factorial(y)
    y+=1
print(sum)
