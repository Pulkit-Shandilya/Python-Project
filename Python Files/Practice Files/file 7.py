#list1=['apple', 'ball', 'kit', 'lamp', 'glass', 'headphone', "apple"]
list1=['apple', 'ball', 'kit', 'lamp', 'glass', 'headphone', "book"]

count=len(list1)
x=0
r1=0
r2=0
for i in list1:
    if x==0:
        r1=i
    elif x==count-1:
        r2=i
    x+=1
if r1==r2:
    print()
    print('1st and last are same')
    print()
else:
    print()
    print('they are not same')
    print()