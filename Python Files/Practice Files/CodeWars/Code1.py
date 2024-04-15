
def Ques1():
    def alphabet_position(text):
        nums=''
        alp = "abcdefghijklmnopqrstuvwxyz"
        for i in text.lower():
            if i in alp:
                y=str(alp.find(i)+1)
                nums+=str(y)+' '
        ans=nums
        return ans

    x=alphabet_position("The sunset sets at twelve o' clock.")
    print(x)

def Ques2():
    def duplicate_count(text):
    # Your code goes here
        print('hello')

def Ques3():
    newstring=string_
    for i in string_:
        if i in ['a','e','i','o','u','A','E','I','O','U']:
            newstring=newstring.replace(i , '')
    string_=newstring


def Ques4():
    x="hello"
    print(len(x))



'''Write a function which receives 4 digits and returns the latest time of day that can be built with those digits.

The time should be in HH:MM format.

Examples:

digits: 1, 9, 8, 3 => result: "19:38"
digits: 9, 1, 2, 5 => result: "21:59" (19:25 is also a valid time, but 21:59 is late'''
import itertools

def latest_clock(a, b, c, d):
    stuff=(a,b,c,d)
    stuff_num=int(''.join(map(str, stuff)))
    answer, remain=0 , stuff_num
    for subset in itertools.permutations(stuff, 4):
        res = int(''.join(map(str, subset)))
        check=[str(d) for d in str(res)]
        if res==0:
            return "00:00"
        if (abs(stuff_num-res) < remain and abs(stuff_num-res)>0 and res<2359) and int(check[2])<7:
            answer , remain = check , abs(stuff_num-res)
    answer.insert(2,":")   
    return (''.join(map(str, answer)))
            






#-----------------------------------------------------------------------------------------------------------------

import itertools
def latest_clock1(a, b, c, d):
    stuff=(a,b,c,d)
    stuff_num=[int(''.join(map(str, stuff[:2]))),int(''.join(map(str, stuff[2:])))]

    answer, remain  = 0 , stuff_num

    for subset in itertools.permutations(stuff, 4):
        
        res = [str(''.join(map(str, subset[:2]))),str(''.join(map(str, subset[2:])))]
        res_num = [int(''.join(map(str, subset[:2]))),int(''.join(map(str, subset[2:])))]

        if ((abs(remain[0]-res_num[0]) <= remain[0])  and abs(res_num[0]) < 24):
            if ( (abs(remain[1]-res_num[1]) <= remain[1])  and abs(res_num[1]) < 60):
                
                answer , remain = res , [abs(remain[0]-res_num[0]),abs(remain[1]-res_num[1])]
                
                
    answer.insert(1,":")
    return (''.join(map(str, answer)))
    

    if res_num==0:
        return "00:00"
            







#-----------------------------------------------------------------------------------------------------------------

def latest_clock2(a, b, c, d):
    stuff=[a,b,c,d]
    print(stuff)
    stuff.sort()
    answer=[]
    x=0
    for i in stuff:
        if i==2:
            answer.append(i)
            stuff.remove(i)


    for p in stuff:
        if p==1:
            answer.append(p)
            stuff.remove(p)


    if len(answer)<2:
        answer.append(0)
        stuff.remove(0)
        
        if len(answer)<2:
            x=(stuff[-1])
            answer.append[stuff[-1]] 
            stuff.remove[stuff[-1]]



    if int(''.join(map(str, stuff[::-1]))) <=  int(''.join(map(str, stuff))):
        answer.append(stuff[0])
        answer.append(stuff[1])
    else:
        answer.append(stuff[1])
        answer.append(stuff[0])
    return answer







def latest_clock3(a,b,c,d):
    stuff=[a,b,c,d]
    stuff.sort()
    true , answer= 0 ,[]
    for i in stuff:
        if i==1:
            true=1
        elif i==2:
            if true==1:
                true=3
                break
            else:
                true=2
    print(true)
        # In case of No 1s or 2s and a 0
    if true==0:
        if (stuff[2]*10)+(stuff[1])<60:
            answer.extend((0,stuff[-1],':',stuff[2],stuff[1]))
        else:
            answer.extend((0,stuff[-1],':',stuff[1],stuff[2]))
    

    #In Case of Having a 1 and a 0
    if true==1:
        answer.append(1)
        stuff.remove(1)
        for i in stuff[::-1]:   #looping through
            if i>=1:
                answer.extend((i,':'))
                stuff.remove(i)
                break
        #checking for minutes digits
        check_1=(stuff[0]*10)+(stuff[1])
        check_2=(stuff[1]*10)+(stuff[0])
        if check_1>check_2 and check_1<60:
            answer.extend((stuff[0] , stuff[1]))
        elif check_2<60:
            answer.extend((stuff[1] , stuff[0]))
        elif check_1<check_2 and check_1<60:
            answer.extend((stuff[0] , stuff[1]))
        elif check_2==60:
            print('-----')
        

    
    # In case of having 2s and a 0
    elif true==2 or true==3:
        twocount=0
        for i in stuff:
                if i==2:
                    twocount+=1            
        for i in stuff[::-1]:
            if twocount==1:
                if i<=3 and i!=2:
                    stuff.remove(2)
                    stuff.remove(i)
                    break
            elif twocount==2:
                    stuff.remove(2)
                    stuff.remove(2)
                    i=2
                    break
            elif twocount==3:
                stuff.remove(2)
                stuff.remove(2)
                i=2
                break
        answer.extend((2,i,':'))
        check_1=(stuff[0]*10)+(stuff[1])
        check_2=(stuff[1]*10)+(stuff[0])
        #checking for minutes digits
        if check_1>check_2 and check_1<60:
            answer.extend((stuff[0] , stuff[1]))
        elif check_2<60:
            answer.extend((stuff[1] , stuff[0]))
        elif check_1<check_2 and check_1<60:
            answer.extend((stuff[0] , stuff[1]))
        elif check_2==60:
            print('-----')
            
    return (''.join(map(str, answer)))


print(latest_clock3(3,0,2,2))



