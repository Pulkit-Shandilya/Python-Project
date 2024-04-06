
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
    answer, remain , log=0 , stuff_num, 0
    for subset in itertools.permutations(stuff, 4):
        res = int(''.join(map(str, subset)))
        
        check=[str(d) for d in str(res)]
        if res==0:
            return "00:00"
        if (abs(stuff_num-res) < remain and abs(stuff_num-res)>0 and res<2359) and int(check[2])<7 and int(check[0])<2:
            answer , remain = check , abs(stuff_num-res)
    answer.insert(2,":")   
    return (''.join(map(str, answer)))
            



print(latest_clock(6, 0, 0, 5))