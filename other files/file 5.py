'''print('')
str1 = input('Enter the string: ')
print()
list1 = []
for i in range (len(str1)):
    for j in range (i+1,len(str1)+1):
        list1.append(str1[i:j])
print(list1)
print()'''

tup1=(9,5,3,[1,2,3],8)
tup1[3][1]=10
print(tup1)
