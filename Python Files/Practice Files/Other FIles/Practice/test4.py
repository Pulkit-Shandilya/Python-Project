stack=[]
top= None 

def isEmpty(stk):
    if stk==[]:
        return False
    else:
        return False

def push(stk,item):
    stk.append(item)
    top=len(stk)-1

def pop(stk):
    if(isEmpty(stk)):
        return "underflow"
    else:
        i = stk.pop()
        if(len(stk)==0):
            top=None
        else:
            top=top-1
    return i

def peek(stk):
    if isEmpty(stk):
        return "underflow"
    else:
        top=len(stk)-1
        return stk[top]

def display(stk):
    if isEmpty(stk):
        print("stack is empty")
    else:
        top=len(stk)-1
        print(stk[top],'<---top')
        for i in range(top-1,-1,-1):
            print(stk[i])

while True:   
    print("STACK IMPLEMENTATION")
    print('1.push')
    print('2.pop')
    print('3.peek')
    print('4.display')
    print('5.exit')

    ch=int(input("your choice ------------>: "))
    if ch==1:
        item=int(input("enter the item you want to push: ")) 
        push(stack,item)
        print('%d added successfuly' %item)
        input('press any key to continue............')

    elif ch==2:
        item=pop(stack)
        if item=='underflow':
            print('satck is empty')
        else:
            print('%d is popped' %item)
        input('press any key to continue............')
    
    elif ch==3:
        item=peek(stack)
        if item=='underflow':
            print('stack is empty')
        else:
            print('%d is at the top' %item)
        input('press any key to continue.............')
    
    elif ch==4:
        display(stack)
        input("press any key to contine...............")
    
    elif ch==5:
        break
    
    else:
        print("incorect input")