# ok= " helo how are you doing"

# hello=ok.split()
# kk=''
# for i in hello:
#     kk +=hello
#     print(kk)


list1=[4,5,6,7,8,9,213,4,523,643]

for (i,count) in enumerate(list1):
    print(i)
    print(count , ' \n')



import math

def sum_of_squares(n):
    
    x,y=n,[]
    if (int(math.sqrt(x//2))**2)*2 == int(x):
        return 2
    while x>0:
        y.append(math.trunc(math.sqrt(x)))
        x-=(y[-1])**2
    return len(y)

print(sum_of_squares(18))