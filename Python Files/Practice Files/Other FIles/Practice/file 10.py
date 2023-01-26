def test1():
    dict1={987:['1' , '2' , '3' , '4']}
    print(dict1)
    x =int((dict1[987])[3])
    
    ((dict1[987])[3]) = x - 5
    print(dict1)

def test2():
    x=1
    y=-1
    print(str(y).isdigit())

test1()