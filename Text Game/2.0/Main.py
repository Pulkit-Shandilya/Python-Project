import time
import random


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
    User_info_check()


#checking user info
def User_info_check():
    if user_age.isdigit():
        user_age_int=int(user_age)
    else:
        time.sleep(1)
        print('\nAs we have Found your Information to be Invalid pls enter it again. . . \n')
        User_info_Reenter()
    #trolling
    user_age_int=int(user_age)
    if user_name.isalpha():
        if user_age.isdigit():
            if user_age_int<10:
                time.sleep(1)
                print("\nAren't your a bit to young?. . .come back when ur a little older lol.\n")
                User_info_Reenter()
            elif user_age_int>=60:
                print("Why is a old boozer playin this . .go read a history book or somethin lol.")
                User_info_Reenter()
            else:
                print('\n Welcome Oh ,' , user_name , 'the great. . we had been waiting for your arival')
                time.sleep(3)
                print('\nYou have many great adventures on your life ahead. . .')
                time.sleep(3)
                print('\nNow you we will be picking your Perks. . Please Select the Character you want to be')
                time.sleep(3)
                str(user_age)
                charater_select_check()
                #calling the file
        else:
            time.sleep(1)
            print('\nAs we have Found your Information to be Invalid pls enter it again. . . \n')
            User_info_Reenter()
    else:
            time.sleep(1)
            print('\nAs we have Found your Information to be Invalid pls enter it again. . . \n')
            User_info_Reenter()






def charater_select_check():
    
    global perk_range_veryhigh,perk_range_high,perk_range_med,perk_range_low,perk_range_verylow
    global select_character , select_character_str

    print('\nPick one of the Following Classes. . .Each has its own Benefits, choose wisely!')
    time.sleep(2.4)
    print("\nClasses: \n 1. Brute : 120-HP High Damage, Med Defence, Low Speed, Low Crit \n 2. Archer: 90-HP Med Damage, Low Defence, High Speed, High Crit \n 3. Warrior: 100-HP Med Damage, High Defence, Med Speed, Med Crit \n 4. Assassin: 90-HP Low Damage, Low Defence, High Speed, High Crit\n")
    
    #perks limits
    perk_range_veryhigh=random.randint(145, 200)
    perk_range_high=random.randint(115, 150)
    perk_range_med=random.randint(80, 120)
    perk_range_low=random.randint(45, 85)
    perk_range_verylow=random.randint(10, 45)



    select_character_str=str(input('Press the Number 1-4 to select your character. . .'))
    #--------------------------------
    return character_select()



#----------------------------------------------------------------------------------------------------------------------
class perks:
    def __init__(self , health ,strength , defence , speed , crit) -> None:
        self.perk_health = health
        self.perk_strength = strength
        self.perk_defence = defence
        self.perk_speed = speed
        self.perk_crit = crit

    

def character_select():
    global user_Class
    global perk_health , perk_strength , perk_defence , perk_Speed , perk_crit , player_select
    


    if select_character_str.isdigit():
        select_character=int(select_character_str)
        if select_character in range (1,5):
                if select_character==1:

                    user_Class = str('Brute')
                    player_select = perks(120,perk_range_veryhigh,perk_range_med,perk_range_verylow,perk_range_veryhigh)

                elif select_character==2:
                
                    user_Class = str('Archer')
                    player_select = perks(90,perk_range_med,perk_range_low,perk_range_veryhigh,perk_range_high)
                
                elif select_character==3:

                    user_Class = str('Warrior')
                    player_select = perks(100,perk_range_med,perk_range_veryhigh,perk_range_med,perk_range_low)
                
                elif select_character==4:

                    user_Class = str('Assassin')
                    player_select = perks(90,perk_range_low,perk_range_verylow,perk_range_veryhigh,perk_range_veryhigh)
                else:
                    print("-------------------\nerror . . \n-------------------")
                

        else:
            print('')
            print('Please Select a Valid Number From 1-4')
            perks.charater_select_check()
    else:
        print('')
        print('Please Select a Valid Number From 1-4')
        perks.charater_select_check() 
    #---------------------------------------------------------------
    return story_continues()







#--------------------------------Story Continues--------------------------------
def story_continues():
    time.sleep(2)
    print('\nAlrighty!!. . .from the above you have chosen "' , user_Class , '" Great Choice. . .from the RNG we have now given ur Character some perk values as shown Below \n')
    print(user_name , "'s", user_Class, ": \n 1. Health: ", player_select.perk_health,"\n 2. Strength: ",  player_select.perk_strength, "\n 3. Defence: ",  player_select.perk_defence, "\n 4. Speed: ",  player_select.perk_speed, "\n 5. Crit: ",  player_select.perk_crit)
    import Powerups

#Function call





































User_info_check()