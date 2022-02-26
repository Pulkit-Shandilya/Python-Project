import math
import time

#taking user info
def User_info():
    # Solve the quadratic equation ax**2 + bx + c = 0
    #input the coeffiecients
    global a
    global b
    global c
    print('the standard form of a Quadratic eqation is ')
    print('')
    print('ax**2 + bx + c = 0')
    print('')
    print('Please enter the respective Coefficients below')
    a = input("Enter the coefficients of a: ")
    b= input("Enter the coefficients of b: ")
    c = input("Enter the coefficients of c: ")
User_info()


#Re-Enter
def User_info_check():
    global int_a
    global int_b
    global int_c
    if a.isnumeric and b.isnumeric() and c.isnumeric():
        int_b=int(b)
        int_a=int(a)
        int_c=int(c)
        if int_a<0:
            User_info_Reenter()
        else:
            Calculation_V01()
    elif (a.startswith("-") and a[1:].isdigit()) or (b.startswith("-") and b[1:].isdigit()) or (c.startswith("-") and c[1:].isdigit()):
        int_b=int(b)
        int_a=int(a)
        int_c=int(c)
        Calculation_V02()
    else:
        print('')
        print('We Have Found something Wrong in your Entered Information')
        print('')
        time.sleep(1)
        print('Analysing. . .')
        time.sleep(2)
        print('')
        User_info_Reenter()

#checking user info
def User_info_Reenter():
    global a
    global b
    global c
    if a!=float or a!=int:
        a=input("Please Re-ntera' : ")
    if b!=float or b!=int:
        b=input("Please Re-nterb' : ")
    if c!=float or c!=int:
        c=input("Please Re-nterc' : ")
    return User_info_check()


###### ACTUAL SOLVING PART ######

def Calculation_V01():
	# calculating discriminant using formula
	dis = (int_b * int_b - 4 * int_a * int_c)
	sqrt_val = math.sqrt(abs(dis))
	
	# checking condition for discriminant
	if dis > 0: 
		print(" real and different roots ")
		print((-int_b + sqrt_val)/(2 * int_a))
		print((-int_b - sqrt_val)/(2 * int_a))
	
	elif dis == 0:
		print(" real and same roots")
		print(-int_b / (2 * int_a))
	
	# when discriminant is less than 0
	else:
		print("Complex Roots")
		print(- int_b / (2 * int_a), " + i", sqrt_val)
		print(- int_b / (2 * int_a), " - i", sqrt_val)

def Calculation_V02():
    if a.startswith("-") and a[1:].isdigit():
        negint_a=-(int_a)
    else:
        negint_a=int_a
    if b.startswith("-") and b[1:].isdigit():
        negint_b=-(int_b)
    else:
        negint_b=int_b
    if c.startswith("-") and c[1:].isdigit():
        negint_c=-(int_c)
    else:
        negint_c=int_c
    # calculate the discriminant
    d = (negint_b**2) - (4*negint_a*negint_c)
    # find two solutions
    sol1 = (-negint_b-(d)**0.5)/(2*negint_a)
    sol2 = (-negint_b+(d)**0.5)/(2*negint_a)

    equation= (negint_a , '**2 + ' , negint_b , 'x + ',negint_c)

    print('The solution of the equationare {0} and {1} '.format(sol1,sol2))


User_info_check()