#import stuff
import random
import time
def perks_information():
    global perk_health
    global perk_crit
    global perk_defence
    global perk_Speed
    global perk_strength
    from perks_02 import perk_health,perk_crit,perk_defence,perk_Speed,perk_strength


# Small Health Pack
def user_powerup_smallhealth():
    loop_variable=1
    while loop_variable==1:
        small_health_pack= random.randint(1, 150)
        if small_health_pack in range (100, 102):
            if (perk_health>=(perk_health-20)):
                perk_health=perk_health+20


# Bigger Health Pack


def user_powerup_smallhealth():
    loop_variable=1
    while loop_variable==1:
        big_health_pack= random.randint(1, 400)
        if big_health_pack in range (101, 105):
            if (perk_health>=(perk_health-50)):
                perk_health=perk_health+50


def user_powerup_powerboost():
    loop_variable=1

