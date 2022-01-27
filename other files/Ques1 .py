import random

def ques1():
    string = "{'A':13, 'B':14, 'C':15}"

    Dict = eval(string)
    print(Dict)
    print(Dict['A'])
    print(Dict['C'])

def ques2():
    dict = {'nikhil': 1, 'abhijeet' : 5,
                'manjot' : 10, 'akshat' : 15}
    print ("initial 1st dictionary", dict)
    dict['akash'] = dict.pop('akshat')
    print ("final dictionary", str(dict))

def ques3():
    Dict = {}
    print("Empty Dictionary: ")
    print(Dict)

    Dict[0] = 'Computer'
    Dict[2] = 'For'
    Dict[3] = 1
    Dict[4]= 'Lamp'
    print("\nDictionary after adding 3 elements: ")
    print(Dict)

    Dict['tuple'] = 2, 3, 4
    print(Dict)

def ques4():
    ini_dict = {'nikhil': 1, 'abhijeet' : 5,
                'manjot' : 10, 'akshat' : 15}
    print ("initial 1st dictionary", ini_dict)
    ini_dict['akash'] = ini_dict.pop('akshat')
    print ("final dictionary", str(ini_dict))

def ques5():
    dictionary = {"a": 1, "b": 2}

    keys = list(dictionary.keys())
    print(keys)

def ques6():
    ini_dict = {'nikhil': 1, 'abhijeet' : 5,
                'manjot' : 10, 'akshat' : 15}
    print(ini_dict)

def ques7():
    ini_dict= {"a": 1, "b": 2}
    x = ini_dict.pop('b')
    print(x)
    print(ini_dict)

def ques8():
    phone_dic={}
    n=int(input('Enter number of friends you have: '))
    while (n>=1):
        name= str(input('Enter The Name: '))
        number= int(input('Enter the Number: '))
        phone_dic[name]= number
        n=n-1
    while (n==0):
        print(' ')
        num_output=str(input('Enter the the person whose number you want: '))
        if num_output in phone_dic:
            print(phone_dic[num_output])
        else:
            print('The Key is not prsent in the Dictionary')

def ques9():
    phone_dic={}
    n=int(input('Enter number of friends you have: '))
    while (n>=1):
        name= str(input('Enter The Name: '))
        number= int(input('Enter the Number: '))
        phone_dic[name]= number
        n=n-1
    list1=list(phone_dic.keys()) #or ".values"
    list1.sort()
    print(list1)

def ques10():
    phone_dic={}
    n=int(input('Enter number of friends you have: '))
    while (n>=1):
        name= str(input('Enter The Name: '))
        number= int(input('Enter the Number: '))
        phone_dic[name]= number
        n=n-1
    print(phone_dic)
    while (n==0):
        print(' ')
        num_output=str(input('Enter the the person whose number you want to delete: '))
        if num_output in phone_dic:
            phone_dic.pop(num_output)
        else:
            print('The Key is not prsent in the Dictionary')
            print(' ')
        print(phone_dic)

def ques11():
    y=int(input('how many random number do you want to add: '))
    list1=['hello', 5, 'lamp']
    while y>0:
        x=random.randint(1,100)
        list1.append(x)
        y-=1
    print(list1)

def ques12():
    x=50
    A=[10,20,30,40,50,60,70,80]
    while x>=0:
        S=random.randint(1,4)
        F=random.randint(S,5)
        x-=1
        for K in range(S, F+1):
            print(A[K], end='#')
        print('')

def ques12p2():
    A=[10,20,30,40,50,60,70,80]
    S=random.randint(1,4)
    F=random.randint(S,5)
    for K in range(S, F+1):
        print(A[K], end='#')
    print('')
