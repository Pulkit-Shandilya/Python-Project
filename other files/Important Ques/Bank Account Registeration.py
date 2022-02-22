import random
import math
import time

input_value=0

#List and Tuples Used
Account_Register={}
account_list=[]

#Account Number Generation
def Acc_num_gen():
    global acc_num
    acc_num=random.randint(100000,999999)
    Acc_num_gen_check()

def Acc_num_gen_check():
    if acc_num in account_list:
        Acc_num_gen()
    else: 
        account_list.append(acc_num)

#Aaccount Generation
def Create_Account():
    global User_Name
    global User_Age
    global User_Dep_Ammount
    
    Acc_num_gen()
    User_Name=str(input('Enter your Name: '))
    User_Age=str(input('Enter Your Age-above 15: '))
    User_Dep_Ammount=str(input('Enter Deposite amount more than Rs.1000: '))
    Create_Account_Check()

def Create_Account_Check_Re():
    global User_Name
    global User_Age
    global User_Dep_Ammount

    if User_Name.isalpha():
        if User_Age.isdigit() and int(User_Age)>=16:
            if User_Dep_Ammount.isdigit() and int(User_Dep_Ammount)>=1000:
                Create_Account_Check()
            else:
                print(3)
                User_Dep_Ammount=str(input('Please Enter Deposite amount more than Rs.1000 again: '))
                Create_Account_Check()
        else:
            print(2)
            User_Age=str(input('Enter Your Age Again: '))
            Create_Account_Check()
    else:
        print(3)
        User_Name=str(input('Please Enter your Name Again: '))
        Create_Account_Check()

def Create_Account_Check():
    if User_Name.isalpha():
        if User_Age.isdigit() and int(User_Age)>=16:
            if User_Dep_Ammount.isdigit() and int(User_Dep_Ammount)>=1000:
                #Account Creation
                Account_Register[acc_num]=[User_Name , User_Age , User_Dep_Ammount]
                print('Name \t Age \t Deposited Amount')
                for i in Account_Register[acc_num]:
                    print(i , '\t' , end="")
                time.sleep(1)
                print('')
                Start_Menu()
            else:
                time.sleep(1)
                print('')
                print('We have Found something Wrong in your Entered Information. . .')
                Create_Account_Check_Re()
        else:
            time.sleep(1)
            print('')
            print('We have Found something Wrong in your Entered Information. . .')
            Create_Account_Check_Re()
    else:
        time.sleep(1)
        print('')
        print('We have Found something Wrong in your Entered Information. . .')
        Create_Account_Check_Re()


#Start Menu
def Start_Menu():
    global Select_menu
    Select_menu=str(input("Select One of the Following options \n 1. Create New Account \n 2. Show Account Info \n 3. Deposit Money \n 4. Withdraw Money \n 5. Action Logs \n \n Enter: "))
    if int(Select_menu)==1:
        Create_Account()
    if int(Select_menu==2):
        print('')
    else:
        print("Incorrect Input Please Enter Again")

Start_Menu()

