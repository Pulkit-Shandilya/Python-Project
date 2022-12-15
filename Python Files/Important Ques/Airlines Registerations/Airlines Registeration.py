import time , re , random 
from datetime import datetime , timedelta , date 
def start_menu():
    Select_menu=str(input("Select One of the Following options \n 1. Book a Ticket \n 2. View Ticket \n 3. Delete Ticket  \n \n Enter: "))

    if bool(re.match('[0-4]+$' , Select_menu)):
        if int(Select_menu)==1:
            Ticket_Book()
        elif int(Select_menu)==2:
            print('')
        elif int(Select_menu)==3:
            print('')
        else:
            print('\n  Please enter a valid option. . . \n ')
            start_menu()
    else:
        print('\n  Please enter a valid option. . . \n ')
        start_menu()



def  Ticket_Book():
    global Select_Airlines_menu

    def Airlines_Person_Name_Age():
        Ticket_name = str(input('\n Please Enter Your Name: '))
        Ticket_Age = str(input(' Please Enter Your Age: '))
        if bool(re.match('[a-zA-Z\s]+$' , Ticket_name)) == False:
            print('. . . checking ')
            print(' Please re-enter your Details')
            Airlines_Person_Name_Age()
        elif Ticket_Age.isdigit() == False:
            print('. . . checking ')
            print(' Please re-enter your Details')
            Airlines_Person_Name_Age()
        elif int(Ticket_Age)<18 or int(Ticket_Age)>100:
            print('. . . checking ')
            print(' Please re-enter your Details')
            Airlines_Person_Name_Age()
        else:
            return Ticket_name , Ticket_Age


    #--------------------------------------
    def Airlines_Select():
        Airlines_list=['Etihad' , 'Vistara' , 'Lufthansa' , 'Air India']
        Select_Airlines_menu=str(input("\n Select One of the Following Airlines \n 1. Etihad \n 2. Vistara \n 3. Lufthansa \n 4. Air India \n \n Enter: "))
        if Select_Airlines_menu.isdigit():
            if int(Select_Airlines_menu) in range (1,5):
                return Airlines_list[int(Select_Airlines_menu)-1]
            else:
                Airlines_Select()
        else:
            Airlines_Select()
        

    #--------------------------------------
    def Airline_travel_location_start():
        location_list_d=['Delhi' , 'Mumbai' , 'Kochin' , 'Chennai']
        Select_start_location_menu=str(input("Select One of the Following Airports for Departure \n 1. Delhi \n 2. Mumbai \n 3. Kochin \n 4. Chennai \n \n Enter: "))
        if Select_start_location_menu.isdigit():
            if int(Select_start_location_menu) in range (1,5):
                return location_list_d[int(Select_start_location_menu)-1]
            else:
                Airline_travel_location_start()
        else:
            Airline_travel_location_start()


    #--------------------------------------
    def Airline_travel_location_end():
        location_list_l=['Munich' , 'New York' , 'London' , 'Beijing']
        Select_end_location_menu=str(input("Select One of the Following Airports for Landing \n 1. Munich \n 2. New York \n 3. London \n 4. Beijing \n \n Enter: "))
        if Select_end_location_menu.isdigit():
            if int(Select_end_location_menu) in range (1,5):
                return location_list_l[int(Select_end_location_menu)-1]
            else:
                Airline_travel_location_end()
        else:
            Airline_travel_location_end()

    #--------------------------------------
    def Airline_Travel_Class():
        global Select_flight_class_menu

        flight_class_list=['Economy' , 'Buisness Class' , 'First Class' , 'Private']
        Select_flight_class_menu=str(input("Select One of the Class's for your travel \n 1. Economy \n 2. Buisness Class \n 3. First Class \n 4. 'Private' \n \n Enter: "))
        print(Select_flight_class_menu)
        if Select_flight_class_menu.isdigit():
            if int(Select_flight_class_menu) in range (1,5):
                return flight_class_list[int(Select_flight_class_menu)-1]
            else:
                Airline_Travel_Class()
        else:
            Airline_Travel_Class()

    #--------------------------------------
    def Airline_travel_Price():
        price = 0
        if Select_flight_class_menu == '1':
            price = random.randint(5000,10000)
        elif Select_flight_class_menu == '2':
            price = random.randint(10000,20000)
        elif Select_flight_class_menu =='3':
            price = random.randint(20000,30000)
        elif Select_flight_class_menu == '4':
            price = random.randint(40000,70000)

        return price

    #--------------------------------------
    def Flight_Date():
        num1 = random.randint(10,40)

        Date_Today = date.today()        
        # calculating end date by adding num1 days
        Flight_Date = Date_Today + timedelta(days=num1)
        
        return Date_Today , Flight_Date

    #--------------------------------------

    Person_Name , Person_Age = Airlines_Person_Name_Age()
    time.sleep(1.5)
    Airline_name=Airlines_Select() 
    time.sleep(1.5)
    print('')
    Departure_location=Airline_travel_location_start()
    time.sleep(1.5)
    print('')
    Landing_location = Airline_travel_location_end()
    time.sleep(1.5)
    print('')
    Flight_Class = Airline_Travel_Class()
    Flight_Price = Airline_travel_Price()
    Date_Today , Date_of_Flight = Flight_Date()

    Booking_Details =[Person_Name , Person_Age , Airline_name , Departure_location , Landing_location , Flight_Class , Flight_Price , Date_Today , Date_of_Flight]
    print(Booking_Details)

start_menu()