# Imports random function from the Python library
import random

# Imports custom modules
from adventure_pkg.story_functions import generate_strings,faerun_story, non_faerun_story, greeting, leave_game, faerun_hero, nonfaerun_hero, baldurs_gate, invalid, win_game
from adventure_pkg.character_functions import Character

#print("Imports successful.")

# Initializing variables
toril = "Toril"
krynn = "Krynn"
ghelspad = "Ghelspad"
worlds = ""

cleric = "Cleric"
wizard = "Wizard"
sorcerer = "Sorcerer"
fighter = "Fighter"
rogue = "Rogue"
npc_1 = ""
npc_2 = ""
npc_3 = ""
creatures = ""
enemies = ""
self = ""

exit = "Exit"
play_again = ""
enter = ""
exit_message = ""
dice_result = ""
battle = ""
hero = ""
character = ""
my_hp = ""
my_damage = ""
home_town = ""

character_classes = {
    "Fighter": ["Strength", "Dexterity", "Constitution", "Wisdom", "Intelligence", "Charisma"],
    "Rogue": ["Dexterity", "Intelligence", "Wisdom", "Strength", "Charisma", "Constitution"],
    "Sorcerer": ["Charisma", "Constitution", "Dexterity", "Intelligence", "Wisdom", "Strength"],
    "Wizard": ["Intelligence", "Constitution", "Dexterity", "Wisdom", "Strength", "Charisma"],
}
    # Add more character classes as needed



# Main while loop shell containing nested while loops
while True:
    greeting()
    valid_world = False

    # Beginning of the game prompt function in a nested while loop
    world = input("\nWhat home world would you like to be from?\nPlease choose a number:\n\n1) Ghelspad\n2) Krynn\n3) Toril\n\n")

    # If statement to give the player a choice of starting world in a while loop to allow a reprompt from world input if incorrect input is given
    while not valid_world:
        if world == "Ghelspad" or world == "1":
            cities = ["Bard's Gate", "Hedrad", "Mithril"]
            home_town = random.choice(cities)
            # Initializing worlds and a stored variable to be accessed as the story progresses if this is returned True
            worlds = ghelspad
            # Initializing _origin to allow access to the origin_story function from an imported module
            non_faerun_origin = non_faerun_story()
            print(non_faerun_origin)
            valid_world = True
        elif world == "Krynn" or world == "2":
            cities = ["Gwynned", "Haven", "Yellowreach"]
            home_town = random.choice(cities)
            worlds = krynn
            non_faerun_origin = non_faerun_story()
            print(non_faerun_origin)
            valid_world = True
        elif world == "Toril" or world == "3":
            cities = ["Waterdeep", "Dagger Falls", "Shadowdale"]
            home_town = random.choice(cities)
            worlds = toril
            faerun_origin = faerun_story()
            print(faerun_origin)
            valid_world = True
        else:
            invalid_entry = invalid()
            print(invalid_entry)
            world = input("\nWhat home world would you like to be from?\nPlease choose a number:\n\n1) Ghelspad\n2) Krynn\n3) Toril\n\n")
            valid_world = False
            continue

    while True:
        print("\n\nChoose your Hero:")
        for i, hero_class in enumerate(character_classes.keys(), 1):
            print(f"{i}) {hero_class}")

        hero_choice = input("\nPlease select a number (or type 'Exit' to exit): ")

        if hero_choice.lower() == "exit":
            # Handle exit
            exit_message, npc1, npc_1, enemies, creatures = leave_game(npc_1, creatures, home_town, worlds)
            print(exit_message)
            quit()

        try:
            hero_index = int(hero_choice)
            if 1 <= hero_index <= len(character_classes):
                hero = list(character_classes.keys())[hero_index - 1]
            else:
                raise ValueError
        except ValueError:
            invalid_entry = invalid()
            print(invalid_entry)
            continue

        # Create character and generate ability scores
        player_character = Character(char_class=hero, character_classes=character_classes)

        # Print ability scores
        generate_strings(hero, player_character.abilities, player_character.hp)


        if worlds == "Ghelspad":
            begin_nonfaerun_hero, non_faerun_battle, battle, non_faerun_afterbattle = nonfaerun_hero(worlds, character, home_town, exit_message)
            print(begin_nonfaerun_hero)
        elif worlds == "Krynn":
            begin_nonfaerun_hero, non_faerun_battle, battle = nonfaerun_hero(worlds, character, home_town, exit_message)
            print(begin_nonfaerun_hero)
        elif worlds == "Toril":
            begin_faerun_hero, faerun_battle, battle = faerun_hero(character, home_town, worlds, exit_message)
            print(begin_faerun_hero)
        break

    see_city, elminsters_challenge = baldurs_gate()
    print(see_city)

    congratulations, you_win = win_game(worlds, home_town)
    print(congratulations)