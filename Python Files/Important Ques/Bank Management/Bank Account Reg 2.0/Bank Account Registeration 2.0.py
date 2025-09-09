import random
import math
import time
import pickle
from turtle import end_fill

input_value=0

#------------------------List and Tuples Used------------------------
Account_Register={}
account_list=[]

#------------------------Database Upload
Register_data=open("Python Files\Important Ques\Bank Management\Bank Account Reg 2.0\Register" , "rb")
Account_Register = pickle.load(Register_data)
Register_data.close()

Register_data_ACno=open("Python Files\Important Ques\Bank Management\Bank Account Reg 2.0\Register ACno" , "rb")
account_list = pickle.load(Register_data_ACno)
Register_data_ACno.close()

#------------------------Account Number Generation------------------------
def Acc_num_gen():
    global acc_num
    acc_num=random.randint(100000,999999)
    Acc_num_gen_check()

def Acc_num_gen_check():
    if acc_num in account_list:
        Acc_num_gen()
    else: 
        account_list.append(acc_num)

#------------------------Aaccount Generation------------------------
def Create_Account():
    global User_Name
    global User_Age
    global User_Dep_Ammount
    
    Acc_num_gen()
    User_Name=str(input('Enter your Name (Put Hyphen[-] between Words): '))
    User_Age=str(input('Enter Your Age-above 15: '))
    User_Dep_Ammount=str(input('Enter Deposite amount more than Rs.1000 (without commas): '))
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
                print('')
                User_Dep_Ammount=str(input('Please Enter Deposite amount more than Rs.1000 again: '))
                Create_Account_Check()
        else:
            print('')
            User_Age=str(input('Enter Your Age Again: '))
            Create_Account_Check()
    else:
        print('')
        User_Name=str(input('Please Enter your Name Again: '))
        Create_Account_Check()

def Create_Account_Check():
    if User_Name.isalpha():
        if User_Age.isdigit() and int(User_Age)>=16:
            if User_Dep_Ammount.isdigit() and int(User_Dep_Ammount)>=1000:
                #Account Creation
                print('')
                print('Please Remember Your Account Number you will need that to access your account in the future: ')
                print('')
                print('------------------------------------')
                Account_Register[acc_num]=[acc_num , User_Name , User_Age , User_Dep_Ammount]
                print('Acc.No \t Name \t Age \t Dep.Amount')
                for i in Account_Register[acc_num]:
                    print(i , '\t' , end="")
                print('\n')
                print('------------------------------------')
                print('')
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

#|------------------------Show Account Info------------------------|

def Account_info():
    global Account_info_enter
    if len(account_list)>0:
        Account_info_enter=str(input('Enter the Account number: '))
        account_info_check()
    else:
        time.sleep(1)
        print('')
        print('There are no Accounts Registered Yet, Please Create an Account . . .')
        print('')
        Start_Menu()


def account_info_check():
    #checking 1.0
    if Account_info_enter.isdigit():
        if int(Account_info_enter) in account_list:
            if int(Select_menu)==3:
                Deposit_Money()
            elif int(Select_menu)==4:
                Withraw_Money()
            else:
                print('')
                print('------------------------------------')
                print('Acc.No \t Name \t Age \t Dep.Ammount')
                for p in Account_Register[int(Account_info_enter)]:
                    print(p , '\t' , end="")
                print('\n')
                print('------------------------------------')
                time.sleep(1)
                print('')
                Start_Menu()
        else:
            time.sleep(1)
            print('')
            print('We have Found something Wrong in your Entered Information. . . ')
            account_info_check_re()
    else:
        time.sleep(1)
        print('')
        print('We have Found something Wrong in your Entered Information. . . ')
    account_info_check_re()


def account_info_check_re():
    #rechecking 2.0
    global Account_info_enter
    if Account_info_enter.isdigit():
        if Account_info_enter in account_list:
            account_info_check()
        else:
            time.sleep(1)
            print('')
            Account_info_enter=str(input('Please Enter the Account number Again: '))
            account_info_check()
    else:
        time.sleep(1)
        print('')
        Account_info_enter=str(input('Please Enter the Account number Again: '))
        account_info_check()


#|------------------------Deposit/Withraw  Money------------------------|

def Deposit_Money():
    global Deposit_Amount
    Deposit_Amount=str(input('Enter the Amount you want to Deposit: '))
    Deposit_Withraw_Money_Check()

def Deposit_Withraw_Money_Check():
    if int(Select_menu)==3:
        if Deposit_Amount.isdigit():
            if int(Deposit_Amount)>0:
                Deposit_Variable=int(Account_Register[int(Account_info_enter)][3])   #Calculation
                (Account_Register[int(Account_info_enter)])[3] = Deposit_Variable + int(Deposit_Amount)
                print('')
                print('Amount Successfully Deposited')
                print('')
                print('------------------------------------')
                print('Acc.No \t Name \t Age \t Dep.Ammount')
                for p in Account_Register[int(Account_info_enter)]:
                    print(p , '\t' , end="")
                print('\n')
                print('------------------------------------')
                time.sleep(1)
                print('')
                Start_Menu()
            else:
                print('')
                print('We have Found something Wrong in your Entered Information. . . ')
                print('')
                Deposit_Money()
        else:
            print('')
            print('We have Found something Wrong in your Entered Information. . . ')
            print('')
            Deposit_Money()
    elif int(Select_menu)==4:
        if Withraw_Amount.isdigit():
            if int(Withraw_Amount)>0:
                Deposit_Variable=int(Account_Register[int(Account_info_enter)][3])#Calculation
                (Account_Register[int(Account_info_enter)])[3] = Deposit_Variable - int(Withraw_Amount)
                print('')
                print('Amount Successfully Withrawn')
                print('')
                print('------------------------------------')
                print('Acc.No \t Name \t Age \t Dep.Ammount')
                for p in Account_Register[int(Account_info_enter)]:
                    print(p , '\t' , end="")
                print('\n')
                print('------------------------------------')
                time.sleep(1)
                print('')
                Start_Menu()
            else:
                print('')
                print('We have Found something Wrong in your Entered Information. . . ')
                print('')
                Withraw_Money()
        else:
            print('')
            print('We have Found something Wrong in your Entered Information. . . ')
            print('')
            Withraw_Money()

def Withraw_Money():
    global Withraw_Amount
    Withraw_Amount=str(input('Enter the Amount you want to Withraw: '))
    Deposit_Withraw_Money_Check()


#|------------------------All Data------------------------|
def Data_Call():
    Data_Password=str(input('Please Enter the Authorisation Passoword: '))
    Password_var='iampulkit'
    if Data_Password==Password_var:
        time.sleep(1)
        print('\n Access Granted. . ')
        time.sleep(2)
        print('\n file created. . ')
        Data_show=open("Python Files\Important Ques\Bank Management\Bank Account Reg 2.0\All User Data" , 'w')
        for z in account_list:
            Data_show.write('----------------------------------')
            Data_show.write(f"\n Account Number: {Account_Register[z][0]} \n Name: {Account_Register[z][1]} \n Age: {Account_Register[z][2]} \n Amount Deposited: {Account_Register[z][3]}\n")
        Data_show.close()

        Start_Menu()

    else:
        print('incorrect Auth key.')
        time.sleep(1)
        print('')
        Start_Menu()

#|------------------------Start Menu------------------------|

def Start_Menu():

    Register_data= open('Python Files\Important Ques\Bank Management\Bank Account Reg 2.0\Register' , 'rb+')
    pickle.dump(Account_Register , Register_data)
    Register_data.close()

    Register_data_ACno=open("Python Files\Important Ques\Bank Management\Bank Account Reg 2.0\Register ACno" , "rb+")
    pickle.dump(account_list , Register_data_ACno)
    Register_data_ACno.close()

    global Select_menu
    print('')
    Select_menu=str(input("Select One of the Following options \n 1. Create New Account \n 2. Show Account Info \n 3. Deposit Money \n 4. Withdraw Money \n 5. All Data \n \n Enter: "))
    if Select_menu.isdigit():
        print('')
        if int(Select_menu)==1:
            Create_Account()
        elif int(Select_menu)==2:
            Account_info()
        elif int(Select_menu)==3:
            Account_info()
        elif int(Select_menu)==4:
            print('test')
            Account_info()
        elif int(Select_menu)==5:
            Data_Call()
        else:
            Start_Menu()
    else:
        print('10')
        Start_Menu()

Start_Menu() 