import time

#taking user info
def User_info():
    global user_name
    global user_age
    user_name=str(input('Please Enter Your Name Fellow Travelar: '))
    user_age=str(input('Please Enter Your Age Fellow Travelar: '))
User_info()


#Re-Enter
def User_info_Reenter():
    global user_name
    global user_age
    user_name=str(input('Please Enter Your Name Fellow Travelar: '))
    user_age=str(input('Please Enter Your Age Fellow Travelar: '))
    return User_info_check()


#checking user info
def User_info_check():
    if user_age.isdigit():
        user_age_int=int(user_age)
    else:
        print('')
        time.sleep(1)
        print('As we have Found your Information to be Invalid pls enter it again. . . ')
        print('')
        User_info_Reenter()
    #trolling
    user_age_int=int(user_age)
    if user_name.isalpha():
        if user_age.isdigit():
            if user_age_int<10:
                time.sleep(1)
                print('')
                print("Aren't your a bit to young?. . .come back when ur a little older lol.")
                print('')
                User_info_Reenter()
            elif user_age_int>=60:
                print('')
                print("Why is a old boozer playin this . .go read a history book or somethin lol.")
                print('')
                User_info_Reenter()
            else:
                print('')
                print('Welcome Oh ,' , user_name , 'the great. . we had been waiting for your arival')
                time.sleep(3)
                print('')
                print('You have many great adventures on your life ahead. . .')
                time.sleep(3)
                print('')
                print('Now you we will be picking your Perks. . Please Select the Character you want to be')
                time.sleep(3)
                str(user_age)
                import perks
                #calling the file
        else:
            print('')
            time.sleep(1)
            print('As we have Found your Information to be Invalid pls enter it again. . . ')
            print('')
            User_info_Reenter()
    else:
            print('')
            time.sleep(1)
            print('As we have Found your Information to be Invalid pls enter it again. . . ')
            print('')
            User_info_Reenter()

#trolling



User_info_check()