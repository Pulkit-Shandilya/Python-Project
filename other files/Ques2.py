import random as r

def ques13():
    x=30
    while x>=0:
        SUB=['ENG','PHY', 'CHEM', 'CS', 'MATHS']
        R=r.randint(1,3)
        OS=""
        for J in range(R,0,-1):
            OS+=SUB[J]+'$'
        print(OS)
        x-=1

def ques14():
    dict1={}
    no_emplyees=int(input('Enter the Number of emplyees: '))
    no_emplyees-=1
    while no_emplyees>=0:
        name = str(input('Enter your Name: '))
        salaray =  int(input('Enter the Salaray: '))
        house_rent = int(input('Enter the  House rent: '))
        conveyance_allowance = int(input('Enter the Conveyance allowance: '))
        dict1[name]=(name , salaray , house_rent , conveyance_allowance )
        print('')
        no_emplyees-=1
    print(dict1)

ques14()