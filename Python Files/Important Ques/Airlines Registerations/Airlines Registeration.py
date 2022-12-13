import pickle
import time

def start_menu():
    Select_menu=str(input("Select One of the Following options \n 1. Book a Ticket \n 2. View Ticket \n 3. Cancel Ticket  \n \n Enter: "))

    if int(Select_menu)==1:
        Ticket_Book()
    elif int(Select_menu)==2:
        print('')
    elif int(Select_menu)==3:
        print('')
    else:
        start_menu()


def  Ticket_Book():
    global Select_Airlines_menu

    def Airlines_Select():
            Airlines_list=['Etihad' , 'Vistara' , 'Lufthansa' , 'Air India']
            Select_Airlines_menu=str(input("\n Select One of the Following Airlines \n 1. Etihad \n 2. Vistara \n 3. Lufthansa \n 4. Air India \n \n Enter: "))
            if Select_Airlines_menu.isdigit():
                if int(Select_Airlines_menu) in range (1,5):
                    return Airlines_list[int(Select_Airlines_menu)]
                else:
                    Airlines_Select()
            else:
                Airlines_Select()
        


    def Airline_travel_location_start():
                    location_list_d=['Delhi' , 'Mumbai' , 'Kochin' , 'Chennai']
                    Select_start_location_menu=str(input("Select One of the Following Airports for Departure \n 1. Delhi \n 2. Mumbai \n 3. Kochin \n 4. Chennai \n \n Enter: "))
                    if Select_start_location_menu.isdigit():
                        if int(Select_start_location_menu) in range (1,5):
                            return location_list_d[int(Select_start_location_menu)]
                        else:
                            Airline_travel_location_start()
                    else:
                        Airline_travel_location_start()

    def Airline_travel_location_end():
                    location_list_l=['Munich' , 'New York' , 'London' , 'Beijing']
                    Select_end_location_menu=str(input("Select One of the Following Airports for Landing \n 1. Munich \n 2. New York \n 3. London \n 4. Beijing \n \n Enter: "))
                    if Select_end_location_menu.isdigit():
                        if int(Select_end_location_menu) in range (1,5):
                            return location_list_l[int(Select_end_location_menu)]
                        else:
                            Airline_travel_location_start()
                    else:
                        Airline_travel_location_start()

    Airline_name=Airlines_Select() 
    time.sleep(1.5)
    print('')
    Departure_location=Airline_travel_location_start()
    time.sleep(1.5)
    print('')
    Landing_location=Airline_travel_location_end()



start_menu()