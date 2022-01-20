import math
import time

#taking user info
def User_info():
    # Solve the quadratic equation ax**2 + bx + c = 0
    #input the coeffiecients
    global a
    global b
    global c
    print('the standard form of a Quadratic eqation is ')
    print('')
    print('ax**2 + bx + c = 0')
    print('')
    print('Please enter the respective Coefficients below')
    a = input("Enter the coefficients of a: ")
    b= input("Enter the coefficients of b: ")
    c = input("Enter the coefficients of c: ")
User_info()


#Re-Enter
def User_info_check():
    global int_a
    global int_b
    global int_c
    if a.isnumeric and b.isnumeric() and c.isnumeric():
        print('uhh wtf')
        int_b=int(b)
        int_a=int(a)
        int_c=int(c)
        if int_a==0:
            print(a)
            print('111')
            print('')
            print('We Have Found something Wrong in your Entered Information')
            print('')
            time.sleep(1)
            print('Analysing. . .')
            time.sleep(2)
            print('')
            A_0check()
        else:
            Calculation_V01()
    elif ((a.startswith("-") and a[1:].isnumeric) and b.isnumeric() and c.isnumeric()) or (a.isnumeric and (b.startswith("-") and b[1:].isnumeric()) and c.isnumeric()) or (a.isnumeric and b.isnumeric() and (c.startswith("-") and c[1:].isnumeric())) or ((a.startswith("-") and a[1:].isnumeric) and (b.startswith("-") and b[1:].isnumeric()) and c.isnumeric()) or ((a.startswith("-") and a[1:].isnumeric) and b.isnumeric() and (c.startswith("-") and c[1:].isnumeric())) or (a.isnumeric and (b.startswith("-") and b[1:].isnumeric()) and (c.startswith("-") and c[1:].isnumeric())) or ((a.startswith("-") and a[1:].isnumeric) and (b.startswith("-") and b[1:].isnumeric()) and (c.startswith("-") and c[1:].isnumeric())):
        int_b=int(b)
        int_a=int(a)
        int_c=int(c)
        print('we atleast got in')
        if int_a==0:
            print(a)
            print('111')
            print('')
            print('We Have Found something Wrong in your Entered Information')
            print('')
            time.sleep(1)
            print('Analysing. . .')
            time.sleep(2)
            print('')
            A_0check()
        Calculation_V02()
    else:
        print('')
        print('We Have Found something Wrong in your Entered Information')
        print('')
        time.sleep(1)
        print('Analysing. . .')
        time.sleep(2)   
        print('')
        User_info_Reenter()

#Checking if A==0
def A_0check():
    global a
    int_a=int(a)
    if int_a==0:
        print('301')
        a=input("'A' cannot be 0 please enter a Non-Zero Integer: ")
    User_info_check()

#checking user info
def User_info_Reenter():
    global a
    global b
    global c
    print('101')
    if a.isnumeric()==False:
        print('201')
        a=input("Please Re-enter 'a' : ")
    if b.isnumeric()==False:
        b=input("Please Re-enter 'b' : ")
    if c.isnumeric()==False:
        c=input("Please Re-enter 'c' : ")
    return User_info_check()

def Calculation_V01():
    print(int_a)
    print(int_b)
    print(int_c)

def Calculation_V02():
    negint_a=-(int_a)
    negint_a=int_a
    negint_b=-(int_b)
    negint_b=int_b
    negint_c=-(int_c)

    negint_c=int_c
    
    print(negint_a)
    print(negint_b)
    print(negint_c)
    print('')
    print(1-negint_a)
    print(1-negint_b)
    print(1-negint_c)

User_info_check()