import csv
fields=['name','class','year','percent']
choice=int(input("enter the number of entries:"))
f=open("Python Files\Practice Files\CSV files\stu1.csv",'w')
csvv=csv.writer(f)
csvv.writerow(fields)

for i in range (choice):
    name=input("enter name: ")
    classt=input("enter class: ")
    year=input("enter year: ")
    percent=input("enter percentage: ")

    csvv.writerow([name,classt,year,percent])
    print("file created")