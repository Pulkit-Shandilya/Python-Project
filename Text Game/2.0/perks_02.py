import time
import random
from Main import user_name



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
    print(user_name , "'s", user_Class, ": \n 1. Health: ", perk_health,"\n 2. Strength: ",  perk_strength, "\n 3. Defence: ",  perk_defence, "\n 4. Speed: ",  perk_Speed, "\n 5. Crit: ",  perk_crit,)
    import Powerups

#Function call
charater_select_check()