

from datetime import datetime
from datetime import timedelta
from datetime import date

'''import re

x= '2123 34'



y= bool(re.match('[0-4]+$' , x))

print(y)'''

def hello():
    x= ' hellow'
    y=20

    return x , y

m , n = hello()

print(m)
print(n)

  
# taking input as the current date
# today() method is supported by date 
# class in datetime module
Begindatestring = date.today()
  
# print begin date
print("Beginning date")
print(Begindatestring)
# calculating end date by adding 4 days
Enddate = Begindatestring + timedelta(days=4)
  
# printing end date
print("Ending date")
print(Enddate)

x=[Begindatestring , Enddate]

print(x)
for i in x:
    print(i)