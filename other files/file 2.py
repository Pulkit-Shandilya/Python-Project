import random

#the small health
def user_powerup_smallhealth():
  global loop_variable

  loop_variable=1
  perk_health=91
  defined_health=90
  x=1
  while loop_variable==1:
    x += 1
    small_health_pack= random.randint(1, 150)
    if small_health_pack in range (100, 109):
        if perk_health<=defined_health:
          print('')
          print(perk_health)
          perk_health=perk_health+20
          print(perk_health)
          print('')
          exit()
        else:
          print('')
          print('Health is all good for now')
          print(perk_health)
          print('')
          exit()
    else:
      print('it didnt trigger but. . yeah')
    if x==10:
      exit()

#randomizer
def health_powerups():
  loop_variable=1
  x=1
  while loop_variable==1:
    x+=1
    random_number=random.randint(1,5000)
    if x==15:
      exit()
    if random_number in range(300, 400):
      return user_powerup_smallhealth()
    else:
      print('sad luck')
#trigger 
health_powerups()