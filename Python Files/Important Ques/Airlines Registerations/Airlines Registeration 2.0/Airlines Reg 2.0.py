import time , re , random 
from datetime import datetime , timedelta , date 
import pickle
import mysql.connector


ID_List=[]

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mypassword123",
    database="airline"
)
mycursor=mydb.cursor()




def start_menu():
    
    Select_menu=str(input("Select One of the Following options \n 1. Book a Ticket \n 2. View Ticket \n 3.End  \n \n Enter: "))

    if bool(re.match('[0-4]+$' , Select_menu)):
        if int(Select_menu)==1:
            Ticket_Book()
        elif int(Select_menu)==2:
            Ticket_View()
        elif int(Select_menu)==3:
            print('\n Code has been Stopped. . . .')
        else:
            print('\n  Please enter a valid option. . . \n ')
            start_menu()
    else:
        print('\n  Please enter a valid option. . . \n ')
        start_menu()


#-----------------Ticket Book-------------

def Ticket_Book():


    def Flight_Booking_Id():
        x=random.randrange(100000 , 999999)

        if x in ID_List:
            Flight_Booking_Id()
        else: 
            ID_List.append(x)
            return x
        


#-----------------Ticket Upload-------------

def Ticket_View():

    Enter_Booking_Id= str(input('Enter the registered Booking Id: '))

    if Enter_Booking_Id.isdigit():
        if int(Enter_Booking_Id) in ID_List:

            sql= "SELECT * FROM ticket where Booking_ID= %s"
            Booking_ID_tup=[int(Enter_Booking_Id)]
            mycursor.execute(sql , Booking_ID_tup)
            myresult = mycursor.fetchall()
            print('---------------------------------------------------------------------------------------------------')
            print('Booking Id | Name \t | Age |  Departure | Landing | Class | Airlines\t| Booking Date | Price |' )

            for i in myresult:
                for p in i:
                    print(p , '   ', end='')
            print('\n ---------------------------------------------------------------------------------------------------')
            start_menu()
        else:
            print('\n not a valid ID please re-enter. . .')
            start_menu()
    else:
        print('\n not a valid ID please re-enter. . .')
        start_menu()
