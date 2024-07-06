

def morse_code_decoder(morse_code):
    morse_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
        '-----': '0', '--..--': ',', '.-.-.-': '.', '..--..': '?', '.----.': "'",
        '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
        '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-',
        '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', ' ': ' '
    }
    
    words = morse_code.strip().split("  ")
    print(words)
    decoded_message = []
        
    for word in words:

        letters = word.split()
        decoded_word = ''
        for letter in letters:
            decoded_word += morse_dict[letter]
        decoded_message.append(decoded_word)

    return ' '.join(decoded_message)

# Example usage:
'''morse_string = ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
decoded_message = morse_code_decoder(morse_string)
print("Decoded message: ", decoded_message)'''

#---------------------------------------------------------------------------------------------



# product of consecutive fibonacci numbers should equal '_prod' 

def product_fib(_prod):
    x,y,z=1,0,0
    if _prod==0 : return [0,1,True]
    if _prod==1 : return [1,1,True]
    if _prod==2 : return [1,2,True]
    
    while z<(_prod/2):
        if x*z==_prod:
            return [x, z, True]
        z=x+y
        x=y
        y=z
        if x*z==_prod:
            return [x, z, True]
    x,y,z=1,0 ,0
    while True:
        z=x+y
        if z*y>_prod:
            break
        x=y
        y=z
    return [y, z, False]



# print(product_fib(800))


#-------------------------------------------------------------------------------------------



'''Your task is to write a function which returns the n-th term of the following series, which is
the sum of the first n terms of the sequence (n is the input parameter)



Series: 1+ 1/4 + 1/7 + 1/10 + 1/13 + 1/16 + 1/19. . . .



'''
def series_sum(n):
    if n==0:
        return 0.00
    solution,z = 0.00,1

    while n>0:
        n-=1
        solution += 1/(1+(z-1)*3)
        z+=1
        #1/(1 + (z-1)3)
    if solution==1.0:
        return f"{solution:.2f}"
    return str(round(solution,2))

#print(series_sum(1))

#---------------------------------------------------------------------------------


def last_digit(lst):
    lst.reverse()
    
    div={0:1,1:1 , 2:4 , 3:4 , 4:4, 5:1, 6:1,7:4,8:4,9:2}
    rmndr=lst[-1]%10
    if rmndr in [0,1,5,6]:
        return rmndr
    
    for i in lst:
        print('')



#https://www.youtube.com/watch?v=4DJt6RBxJKI

#print(last_digit([1007,124534]))    



#-------------------------------------------------------------------------------------

#dice points
''' 
 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
 '''


def score_1(dice):
    n1,n2,n3,n4,n5,n6,sum_=0,0,0,0,0,0,0
    for i in dice:
        if i==1:
            n1 += 1
        elif i==2:
            n2 += 1
        elif i==3:
            n3 +=1
        elif i==4:
            n4 += 1
        elif i==5:
            n5 += 1
        elif i==6:
            n6 +=1

        if n1 >=3:
            sum_ += (n1//3)*1000
            n1-=3
        elif n2 >=3:
            sum_ += (n2//3)*200
            n2-=3
        elif n3 >=3:
            sum_ += (n3//3)*300
            n3-=3
        elif n4 >=3:
            sum_ += (n4//3)*400
            n4-=3
        elif n5 >=3:
            sum_ += (n5//3)*500
            n5-=3
        elif n6 >=3:
            sum_ += (n6//3)*600
            n6-=3
    sum_+= (n1*100) + (n5*50)
    return sum_
    

def score_1(dice):
    n1,n2,n3,n4,n5,n6,sum_=0,0,0,0,0,0,0
    points_=[1000,200,300,400,500,600]
    extra_=[100,0,0,0,50,0]
    for i in dice:
        if i==1:
            n1 += 1
        elif i==2:
            n2 += 1
        elif i==3:
            n3 +=1
        elif i==4:
            n4 += 1
        elif i==5:
            n5 += 1
        elif i==6:
            n6 +=1

    counter=[n1,n2,n3,n4,n5,n6]
    for (i,count) in enumerate(counter):
        sum_+= (points_[i] if count >=3 else 0) + extra_[i]* (count%3)
    return sum_
    



def score_top(dice): 
    sum = 0
    counter = [0,0,0,0,0,0]
    points = [1000, 200, 300, 400, 500, 600]
    extra = [100,0,0,0,50,0]
    for die in dice: 
        counter[die-1] += 1

    for (i, count) in enumerate(counter):
        sum += (points[i] if count >= 3 else 0) + extra[i] * (count%3)

    return sum 


print(score_1([6,6,6,3,3]))































#dont consider HRMS and email 