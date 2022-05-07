from operator import contains
import random 

def random_hex():
    x=10
    while x>=0:
        print('#{:06x}' .format(random.randint(0,0xFFFFFF)))
        x-=1

def indented_dictionary():
    dict1={"a":1, "b":2, 'c':{"cc":3 , 'cd': 4 , 'ce':{'ced' : 5}}}
    print(dict1['a'])
    print(dict1['c'])
    print(dict1['c']['cc'])
    print(dict1['c']['ce']['ced'])


def test101():
    list1=[1,2,3,4,5,6]
    x=3
    if x in list1:
        print(1)

test101()



'''dict1={'lamp':'bulb', 'pen':'refil'}
dict2={1:123 , 2:'apple' , 'test':1234}


print(dict1)

x=dict2[2]
dict1['switch']=dict2['test']

print(dict1)


'''
dict2={1:123 , 2:'apple' , 'test':1234}
for i in dict2.values():
    print(i)
