import time
import random
from Main import user_name



def charater_select_check():
    
    global perk_range_veryhigh,perk_range_high,perk_range_med,perk_range_low,perk_range_verylow
    global select_character , select_character_str

    print('\nPick one of the Following Classes. . .Each has its own Benefits, choose wisely!')
    time.sleep(2.4)
    print("\nClasses: \n 1. Brute : 120-HP High Damage, Med Defence, Low Speed, Low Crit \n 2. Archer: 90-HP Med Damage, Low Defence, High Speed, High Crit \n 3. Warrior: 100-HP Med Damage, High Defence, Med Speed, Med Crit \n 4. Assassin: 90-HP Low Damage, Low Defence, High Speed, High Crit\n")
    
    #perks limits
    perk_range_veryhigh=random.randint(100, 190)
    perk_range_high=random.randint(90, 150)
    perk_range_med=random.randint(50, 120)
    perk_range_low=random.randint(10, 100)
    perk_range_verylow=random.randint(5, 50)



    select_character_str=str(input('Press the Number 1-4 to select your character. . .'))
    #--------------------------------
    return perks.character_select()



#----------------------------------------------------------------------------------------------------------------------
class perks:
    def __init__(self , health ,strength , defence , speed , crit) -> None:
        self.perk_health = health
        self.perk_strength = strength
        self.perk_defence = defence
        self.perk_speed = speed
        self.perk_health = crit

    

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