
import mysql.connector
import time


l=[1,3,4,5,6,3,7,8,28,343,6436,66]

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mypassword123",
    database="airline"
)
mycursor=mydb.cursor()

mycursor.execute("select * from ticket")

x = mycursor.fetchmany(3)
for i in x:
    print(i)

'''import csv 

x = open('Python Files\Practice Files\Other FIles\Practice\hello.csv' , 'r+')
hello = csv.writer(x)

l=['id' , 'name']
l2= [['101' , 'lamp'] , ['202' , 'table'] , ['303' , 'mobile']]

hello.writerow(l)

for i in l2:
    hello.writerow(i)


x= (csv.reader(x))

for i in x:
    print(i)
'''