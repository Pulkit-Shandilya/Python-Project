def palindrome():
    print()
    str1 = input ('Enter the string:- ')
    print()
    l = len (str1)
    p = l - 1
    index = 0
    while (index < p) :
        if (str1[index] == str1 [p]):
            index = index + 1
            p = p-1
        else :
            print ('String is not a palindrome')
            print()
            break
        
    else:
        print('String is a palindrome')
        print()

def evenno():
    print()
    x=int(input('Your Number: '))
    print()
    solve=x%2
    if solve==0:
        print()
        print('Even No. ')
        print()
    else:
        print()
        print('Odd No.')
        print()

def table():
    x=int(input('Enter your Number: '))
    z=0
    while (z<=9):
        multi=x*(z+1)
        z+=1
        print('{0} x {1} = {2}' .format(x,z,multi))

def divisble():
    print()
    x=int(input('Enter your 1st Number: '))
    y=int(input('Enter your 2nd Number: '))
    print()
    sum=0
    for i in range(x,y+1):
        if i%35==0:
            sum+=i
    print('{0} is the sum of the numbers which are divisible by 7 and 5 in the given range' .format(sum))
    print()

def even2():
    x=int(input('Enter your 1st Number : '))
    y=int(input('Enter your 2nd Number: '))
    num=0
    for i in range(x,y+1):
        if i%2==0:
            num+=1
    print(num)

def armstrong():
    x=int(input('Enter a Number: '))
    y=0
    sum=0
    dupe=x
    while x>0:
        y=x%10
        x=x//10
        sum+=y**3
    if sum==dupe:
        print()
        print('Number is Armstrong')
        print()
    else:
        print()
        print('Number is not Armstrong')
        print()

def prime():
    print()
    x=int(input('Enter a number: '))
    y=0
    z=0
    for i in range(1,x+1):
        if x==1:
            print()
            print('{0} is unique' .format(x))
            print()
            exit()
        y=x%i
        if y==0:
            z+=1
    if z!=2:
        print()
        print('{0} is composite' .format(x))
        print()
    else:
        print()
        print('{0} is Prime' .format(x))
        print()

def lessthan3():
    list1=['apple','ball','white','car','plane']
    print()
    for i in list1:
        if len(i)>3:
            print(i)
    print()

def swaplist():
    list1=['apple','ball','white','car','plane','glass','headphones','lamp']
    n=len(list1)

    print()
    print('Your Current list is :' , list1)
    temp= list1[0]
    list1[0]=list1[4]
    list1[4]=temp
    print()
    print('the new list is {0}' .format(list1))
    print()

def enter():
    num=int(input('Enter the amount of elements you want to be in the list: '))
    list1=[]
    for i in range (0,num):
        print()
        input_num=input("Enter Element: ")
        list1.append(input_num)
    print('here is the final list' , list1)

def duplicate():
    list1=[1,2,3,4,5,6,1,2,3,4,5,6]
    list2=[]
    print()
    print('your current list is' , list1)
    for i in list1:
        if i not in list2:
            list2.append(i)
    print()
    print(list2)
    print()

def largestinlsit():
    list1=[1,3,5,5,3,23,1]
    x=0
    r=0
    y=0
    for i in list1:
        if i%2==0:
            y+=1
            if i>x:
                x=i
                r=i
    if y!=0:
        print()
        print(r)
        print()
    else:
        print()
        print('no even numbers')
        print()








def perfectSquares():
    l = int(input('Enter Number: '))
    r = int(input('Enter Number: '))

    for i in range(l, r + 1):
        if (i**(.5) == int(i**(.5))):
            print(i)

def mean():
    n_num = [1, 2, 3, 4, 5]
    n = len(n_num)
    n_num.sort()

    if n % 2 == 0:
        median1 = n_num[n//2]
        median2 = n_num[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = n_num[n//2]
    print("Median is: " + str(median))


def mode():
    list1=[1,2,3,4,5,1,4,1]
    list2=[]
    r=0
    for i in list1:
        x=i
        y=0
        for p in list1:
            if x==p:
                y+=1
        if y>r:
            r=x
    print()
    print('mode is', x)
    print()



print("Enter the marks of five subjects::")

subject_1 = float (input ())
subject_2 = float (input ())
subject_3 = float (input ())
subject_4 = float (input ())
subject_5 = float (input ())

total, average, percentage, grade = None, None, None, None

# Calculation part
total = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
average = total / 5.0
percentage = (total / 500.0) * 100

if average >= 90:
    grade = 'A'
elif average >= 80 and average < 90:
    grade = 'B'
elif average >= 70 and average < 80:
    grade = 'C'
elif average >= 60 and average < 70:
    grade = 'D'
else:
    grade = 'E'

# output
print ("\nThe Total marks is:   \t", total, "/ 500.00")
print ("\nThe Average marks is: \t", average)
print ("\nThe Percentage is:    \t", percentage, "%")
print ("\nThe Grade is:         \t", grade)