import time
import random
from main import user_name
#story time
print('')
print('Pick one of the Following Classes. . .Each has its own Benefits, choose wisely!')
time.sleep(2.4)
print('')
print("Classes: \n 1. Brute : 120-HP High Damage, Med Defence, Low Speed, Low Crit \n 2. Archer: 90-HP Med Damage, Low Defence, High Speed, High Crit \n 3. Warrior: 100-HP Med Damage, High Defence, Med Speed, Med Crit \n 4. Assassin: 90-HP Low Damage, Low Defence, High Speed, High Crit")
print('')
#perks limits
perk_range_veryhigh=random.randint(100, 190)
perk_range_high=random.randint(90, 150)
perk_range_med=random.randint(50, 120)
perk_range_low=random.randint(10, 100)
perk_range_verylow=random.randint(5, 50)

"""
[Class Perk Ranges]:
Very High: 100=150
High: 90-150
Med: 50-120
Low: 10-100
Very Low: 5-50
"""

#character selection check
def charater_select_check():
    global user_Class
    global select_character
    global select_character_str
    global perk_health
    global perk_strength
    global perk_defence
    global perk_Speed
    global perk_crit

    select_character_str=str(input('Press the Number 1-4 to select your character. . .'))
    return character_digit_check()

#character selection
def character_select():
    global user_Class
    global select_character
    global perk_health
    global perk_strength
    global perk_defence
    global perk_Speed
    global perk_crit
    if select_character==1:
        user_Class=str('Brute')
        perk_health=120
        perk_strength=perk_range_veryhigh
        perk_defence=perk_range_med
        perk_Speed=perk_range_verylow
        perk_crit=perk_range_low
    elif select_character==2:
        user_Class=str('Archer')
        perk_health=90
        perk_strength=perk_range_med
        perk_defence=perk_range_low
        perk_Speed=perk_range_veryhigh
        perk_crit=perk_range_high
    elif select_character==3:
        user_Class=str('Warrior')
        perk_health=100
        perk_strength=perk_range_med
        perk_defence=perk_range_veryhigh
        perk_Speed=perk_range_med
        perk_crit=perk_range_med
    elif select_character==4:
        user_Class=str('Assassin')
        perk_health=90
        perk_strength=perk_range_verylow
        perk_defence=perk_range_low
        perk_Speed=perk_range_high
        perk_crit=perk_range_veryhigh
    return story_continues()

#conversion and checking
def character_digit_check():
    global select_character
    
    if select_character_str.isdigit():
        select_character=int(select_character_str)
        if select_character in range (1,5):
            return character_select()
        else:
            print('')
            print('Please Select a Valid Number From 1-4')
            charater_select_check()
    else:
        print('')
        print('Please Select a Valid Number From 1-4')
        charater_select_check()

#Story Continues
def story_continues():
    print('')
    time.sleep(2)
    print('Alrighty!!. . .from the above you have chosen "' , user_Class , '" Great Choice. . .from the RNG we have now given ur Character some perk values as shown Below')
    print('')
    print(user_name , "'s", user_Class, ": \n 1. Health: ", perk_health,"\n 2. Strength: ",  perk_strength, "\n 3. Defence: ",  perk_defence, "\n 4. Speed: ",  perk_Speed, "\n 5. Crit: ",  perk_crit,)
    import Powerups

#Function call
charater_select_check()