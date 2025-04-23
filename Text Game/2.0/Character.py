import random


range_veryhigh=random.randint(100, 190)
range_high=random.randint(90, 150)
range_med=random.randint(50, 120)
range_low=random.randint(10, 100)
range_verylow=random.randint(5, 50)

class perks:
    def __init__(self,health, strength, defence, speed, crit,weapon,armor):
        self.health = health
        self.strength = strength
        self.defence = defence
        self.speed = speed
        self.crit = crit
        self.weapon = weapon
        self.armor = armor



class Brute(perks):
    def __init__(self, health, strength, defence, speed, crit, weapon="Axe", armor="Heavy Plate"):
        super().__init__(health, strength, defence, speed, crit, weapon, armor)
        self.health = 120
        self.strength = range_high
        self.defence = range_med
        self.speed = range_verylow
        self.crit = range_veryhigh
        self.weapon = weapon
        self.armor = armor

class Archer(perks):
    def __init__(self, health, strength, defence, speed, crit, weapon="Bow", armor="Light Leather"):
        super().__init__(health, strength, defence, speed, crit, weapon, armor)
        self.health = 90
        self.strength = range_med
        self.defence = range_low
        self.speed = range_veryhigh
        self.crit = range_high
        self.weapon = weapon
        self.armor = armor

class Warrior(perks):
    def __init__(self, health, strength, defence, speed, crit, weapon="Sword", armor="Chain Mail"):
        super().__init__(health, strength, defence, speed, crit, weapon, armor)
        self.health = 100
        self.strength = range_med
        self.defence = range_veryhigh
        self.speed = range_med
        self.crit = range_low
        self.weapon = weapon
        self.armor = armor

class Assassin(perks):
    def __init__(self, health, strength, defence, speed, crit, weapon="Dagger", armor="Shadow Cloth"):
        super().__init__(health, strength, defence, speed, crit, weapon, armor)
        self.health = 90
        self.strength = range_low
        self.defence = range_med
        self.speed = range_veryhigh
        self.crit = range_high
        self.weapon = weapon
        self.armor = armor

class modifiers(Brute, Archer, Warrior, Assassin):
    def __init__(self, health, strength, defence, speed, crit, weapon, armor):
        super().__init__(health, strength, defence, speed, crit)
        self.health = health
        self.strength = strength
        self.defence = defence
        self.speed = speed
        self.crit = crit
        self.weapon = weapon
        self.armor = armor

class Player(modifiers):
    def __init__(self, health, strength, defence, speed, crit,inventory,weapon,shield):
        super().__init__(health, strength, defence, speed, crit)
        self.health = health
        self.strength = strength
        self.defence = defence
        self.speed = speed
        self.crit = crit
        self.inventory = inventory # Initialize inventory as an empty list
        self.weapon = weapon
        self.shield = shield

        
        self.inventory = []
