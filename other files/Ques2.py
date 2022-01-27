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
ques13()