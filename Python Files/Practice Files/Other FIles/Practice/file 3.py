n = 435
rev = 0
while(n > 0):
    a = n % 10
    print(a)
    rev = rev * 10 + a
    print('.' , rev)
    n = n // 10
    print(',' , n)