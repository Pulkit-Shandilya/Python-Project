import csv


rows= [
    [1,'xyz'],[2,'pqr'],[3, 'abc']
]


with open('Python Files\Practice Files\CSV files\\a.csv','w') as newFile:

    what =csv.writer(newFile)
    what.writerow(['userid' , 'beneficiary'])
    what.writerows(rows)

'''    new = csv.reader(newFile) 
    for lines in new:
        print(lines)'''





'''    newFileWriter = csv.writer(newFile)
    newFileWriter.writerow(['user_id','beneficiary'])
    newFileWriter.writerow([1,'xyz'])
    newFileWriter.writerow([2,'pqr'])
    newFileWriter.writerow([3, 'abc'])
    newFile.close()'''