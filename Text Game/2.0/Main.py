import os
from Character import Brute, Archer, Warrior, Assassin
from GMap import Map

# Character selection
def select_character():
    classes = {
        1: ("Brute", 120, "High", "Med", "Low", "Low"),
        2: ("Archer", 90, "Med", "Low", "High", "High"),
        3: ("Warrior", 100, "Med", "High", "Med", "Med"),
        4: ("Assassin", 90, "Low", "Low", "High", "High")
    }
    while True:
        print("\nPick one of the following classes. Each has its own benefits, choose wisely!")
        for key, value in classes.items():
            print(f"{key}. {value[0]}: {value[1]}-HP, {value[2]} Damage, {value[3]} Defence, {value[4]} Speed, {value[5]} Crit")
        choice = input('Press the number 1-4 to select your character: ')
        if choice.isdigit() and int(choice) in classes:
            return classes[int(choice)][0], choice


# ----------------------------------------------------------


current_room = "start"

#room counts
forest_count = 0
cave_count = 0
mountain_count = 0



map= {"cabin" : Map("You are in a cabin. There is a door to the north.",        "forest1", -1, -1, -1, 0, forest_count),
"forest1" : Map("You are in a forest. There is a path to the south and east.",  "forest2", "cabin", "cave", -1, 0, forest_count),
"forest2" : Map("You are in a forest. There is a path to the south and east.",  "forest1", -1, "mountain", -1, 0.4, forest_count),
"cave": Map("You are in a cave. There is a path to the west.",                  -1, -1, -1, "forest1", 0.2, cave_count),
"mountain": Map("You are in a mountain. There is a path to the west.",          -1, -1, "forest2", -1, 0.3, mountain_count)
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_character(user_class, choice):
    # Create character instance based on class selection
    class_selection = [Brute(0, 0, 0, 0, 0), Archer(0, 0, 0, 0, 0), Warrior(0, 0, 0, 0, 0), Assassin(0, 0, 0, 0, 0)]
    return class_selection[int(choice)-1]

def story_continues(user_class, character):
    clear()
    print(f'\nAlrighty! You have chosen "{user_class}". Great choice! \n Your stats: \n Health: {character.health}\n Strength: {character.strength}\n Defence: {character.defence}\n Speed: {character.speed}\n Critical: {character.crit}')

def main():
    clear()
    user_class,choice = select_character()
    character = create_character(user_class,choice)
    story_continues( user_class, character)
    # Game can continue from here using the character object








if __name__ == "__main__":
    main()