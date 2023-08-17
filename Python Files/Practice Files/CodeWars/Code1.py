
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

Ques1()
