
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


Ques4()