import csv 

with open('Python Files\Practice Files\CSV files\stu.csv' , 'w') as csvfile:
    wrt=csv.writer(csvfile)
    for i in range(2):
        name = input('Enter Your Name: ')
        marks = input('Enter your marks: ')
        wrt.writerow([name , marks])
