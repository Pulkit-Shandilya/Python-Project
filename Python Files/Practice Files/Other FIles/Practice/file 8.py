'''import time
import random
for i in range (1,100):
    x=random.randint(1,500)
    if x<=250 and x>=240:
        print('switch')
    time.sleep(1)'''

'''    # calculate the discriminant
    d = (int_b**2) - (4*int_a*int_c)
    # find two solutions
    sol1 = (-int_b-(d)**0.5)/(2*int_a)
    sol2 = (-int_b+(d)**0.5)/(2*int_a)

    print('The solution are {0} and {1}'.format(sol1,sol2))


'''
#---------------------------------
'''a=str(-12)
print(a[1:]) '''

'''x=str(-1)
print(x.isnumeric())'''
#-------------------------------------
import itertools



list1=[1,2,3,4,2]
list3=[1,2,3,4,5,6,7,8,9]
'''
list2=[5,6,7,8,9,7,9]

x=list1[:2]
y=list2[:2]
print(list1[-1])
print(list2.index(7))
print(x, y)
'''
#---------------
'''answer=[]

true=2

print(list1.index(4))
list1.remove(2)

print(list1)'''
x=[]
for i in itertools.permutations(list3,3):
    x.append(i)
print(x)
print(len(x))