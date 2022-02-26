def Q1():
    name = str(input("What is your name?:- "))
    color = input("what is your favorite color?:- ")
    birth_year = int(input("What Year were you born in?:- "))
    weight = int(input('What is your weight? (kg pls):- '))

    name_characters = len(name)
    age = 2021 - int(birth_year)
    weight_pounds = 2.20462 * int(weight)

    print(
        name + ' likes the colour ' + color + ' and his/her age is ' + str(age) + ' and they weigh ' + str(weight) + 'kg or ' + str(weight_pounds) + 'Pounds'
        ' and just sayin your name has ' + f'[{str(name_characters)}]' + ' number of characters'
    )

def Q2():
    print('')
    x=int(input('Please enter your No: '))
    y=1
    for i in range(1,x+1):
        y*=i
    print('')
    print('Factorial of {0} is {1}' .format(x,y))
    print('')
