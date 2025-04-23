from Character import modifiers
import random


class Powerup:
    def __init__(self, name, description):
        self.name = name
        self.description = description


#Weapons and Armor 
class Weapons(Powerup):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage

    def use(self, character):
        character.strength += self.damage
        print(f"{character.name} equipped {self.name} and gained {self.damage} strength!")
        print(f"{character.name}'s current strength: {character.strength}")


class Armor(Powerup):
    def __init__(self, name, description, defence):
        super().__init__(name, description)
        self.defence = defence

    def use(self, character):
        character.defence += self.defence
        print(f"{character.name} equipped {self.name} and gained {self.defence} defence!")
        print(f"{character.name}'s current defence: {character.defence}")





#Potions
class smallHealthPotion(Powerup):
    def __init__(self, health_increase):
        health_increase = random.randint(10, 20)
        super().__init__("Health Potion", "Restores health.")
        self.health_increase = health_increase

    def use(self, character):
        character.health += self.health_increase
        print(f"{character.name} used a Health Potion and restored {self.health_increase} health!")
        if character.health > character.max_health:
            character.health = character.max_health
            print(f"{character.name}'s health is now at maximum!")
        else:
            print(f"{character.name}'s current health: {character.health}")
    

class largeHealthPotion(Powerup):
    def __init__(self, health_increase):
        health_increase = random.randint(40, 60)
        super().__init__("Health Potion", "Restores health.")
        self.health_increase = health_increase

    def use(self, character):
        character.health += self.health_increase
        print(f"{character.name} used a Health Potion and restored {self.health_increase} health!")
        if character.health > character.max_health:
            character.health = character.max_health
            print(f"{character.name}'s health is now at maximum!")
        else:
            print(f"{character.name}'s current health: {character.health}")