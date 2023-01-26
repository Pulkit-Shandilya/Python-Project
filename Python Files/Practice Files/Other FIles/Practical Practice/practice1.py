import pickle


# Q.Write a Python Program to read a text file line by line and display each word separated by #
def has_between():
    f=open("Python Files\Practice Files\Other Files\Practical Practice\\note2.txt" , 'r')
    x=f.readlines()
    for p in x:
        z=''
        y=p.split()
        for i in y:
            z+=i
            z+='#'
        print(z)

def writerec():
    f=open("Python Files\Practice Files\Other Files\Practical Practice\\Emp.dat" , 'wb')
    
    id = int(input('Please enter your ID: '))
    name = str(input('Please Enter your name: '))
    salary = int(input('Please enter your salary: '))

    list1=[id , name , salary]
    pickle.dump(list1 , f )
    print(list1)

def list_switch():
    list = [3,5,2,7,8,4]
    
    list2 = []
    y=0
    for i in list:
        if y%2==0:
            z=i
        if y%2!=0:
            list2.append(i)
            list2.append(z)
        y+=1
    print(list)
    print(list2)

def four_letter():
    f=open("Python Files\Practice Files\Other Files\Practical Practice\\note2.txt" , 'r')
    x=f.read()
    y=x.split()
    count=0
    for i in y:
        list=[]
        for p in i:
            list.append(p)
        if len(list)==4:
            print(i)
            count+=1
    print('Number of 4 letter words are: ' , count)

def count_letter():
    f=open("Python Files\Practice Files\Other Files\Practical Practice\\note2.txt" , 'r')
    x=f.read()
    list=['a' , 'e' , 'i' , 'o' , 'u']
    count_vowel , count_upper , count_conso , count_lower=0, 0, 0, 0
    for i in x:
        if i.lower() in list:
            count_vowel+=1
        elif i.isalpha():
            count_conso+=1
        if i.isupper():
            count_upper+=1
        if i.islower():
            count_lower+=1
    y=[]
    print("The Number of Vowels are : {0} \n The Number of Consonents are: {1} \n The Number of UpperCase letters are: {2} \n The Number of lower case letters are: {3} " .format(count_vowel , count_conso , count_upper , count_lower))


count_letter()