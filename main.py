#main.py
#import sys
#print(sys.path)

#Imports random function from the Python library
import random
from colorama import init, Fore, Style
init(autoreset=True)
import textwrap
import shutil

#Imports custom modules
from adventure_pkg.story_functions import character_creation, faerun_story, non_faerun_story, greeting, leave_game, faerun_hero, nonfaerun_hero, baldurs_gate, invalid, win_game
from adventure_pkg.character_functions import Character

#Initializing variables
toril = "Toril"
krynn = "Krynn"
scarn = "Scarn"
cleric = "Cleric"
wizard = "Wizard"
sorcerer = "Sorcerer"
fighter = "Fighter"
rogue = "Rogue"
npc_1 = ""
npc_2 = ""
npc_3 = ""
exit_message = ""
monster_name = ""
chosen_race = None

character_abilities = {
    "Cleric": ["Wisdom", "Constitution", "Charisma", "Intelligence", "Strength", "Dexterity"],
    "Fighter": ["Strength", "Dexterity", "Constitution", "Wisdom", "Intelligence", "Charisma"],
    "Rogue": ["Dexterity", "Intelligence", "Wisdom", "Strength", "Charisma", "Constitution"],
    "Sorcerer": ["Charisma", "Constitution", "Dexterity", "Intelligence", "Wisdom", "Strength"],
    "Wizard": ["Intelligence", "Constitution", "Dexterity", "Wisdom", "Strength", "Charisma"],
} #Add more character classes as needed

racial_traits = {
    "Dwarf": ["Constitution", 2, "Charisma", -2],
    "Elf": ["Dexterity", 2, "Constitution", -2],
    "Human": [],
}

#Main while loop shell containing nested while loops
while True:
    greeting()
    valid_world = False

    #Beginning of the game prompt
    world = input(f"\n{Fore.CYAN + Style.NORMAL}What home world would you like to be from?\nPlease choose a number:\n\n1) Scarn\n2) Krynn\n3) Toril\n\n")

    #choice of starting world
    while not valid_world:
        if world == "Scarn" or world == "1":
            cities = ["Bard's Gate", "Hedrad", "Mithril"]
            home_town = random.choice(cities)
            #Initializing worlds variable to be accessed as the story progresses if this is returned True
            worlds = scarn
            #Initializing _origin variable
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
            world = input(f"\n{Fore.CYAN + Style.NORMAL}What home world would you like to be from?\nPlease choose a number:\n\n1) Scarn\n2) Krynn\n3) Toril\n\n")
            valid_world = False
            continue

    while True:
        print(f"\n{Fore.CYAN + Style.NORMAL}Choose your Hero:")
        for i, hero_class in enumerate(character_abilities.keys(), 1):
            print(f"{Fore.CYAN + Style.NORMAL}{i}){Fore.CYAN + Style.NORMAL} {hero_class}")

        hero_choice = input(f"\n{Fore.CYAN + Style.NORMAL}Please select a number (or type 'Exit' to leave story): ")

        if hero_choice.lower() == "exit":
            # Handle exit
            leave_game(npc_1, monster_name, home_town, worlds)
            print(exit_message)
            quit()

        try:
            hero_index = int(hero_choice)
            if 1 <= hero_index <= len(character_abilities):
                hero = list(character_abilities.keys())[hero_index - 1]
            else:
                raise ValueError
        except ValueError:
            invalid_entry = invalid()
            print(invalid_entry)
            continue

        while chosen_race is None:
            # Now, let the user choose a race
            print(f"\n\n{Fore.CYAN + Style.NORMAL}Choose your Race:")
            for i, race in enumerate(racial_traits.keys(), 1):
                print(f"{Fore.CYAN + Style.NORMAL}{i}){Fore.CYAN + Style.NORMAL} {race}")

            race_choice = input(f"\n{Fore.CYAN + Style.NORMAL}Please select a number: ")

            try:
                race_index = int(race_choice)
                if 1 <= race_index <= len(racial_traits):
                    # Assign the value inside the try block
                    chosen_race = list(racial_traits.keys())[race_index - 1]
                else:
                    raise ValueError
            except ValueError:
                invalid_entry = invalid()
                print(invalid_entry)
                # Continue to the next iteration of the loop
                continue

        # Calculate racial modifiers
        chosen_race_traits = racial_traits.get(chosen_race, [])
        racial_modifiers = {chosen_race_traits[i]: chosen_race_traits[i + 1] for i in range(0, len(chosen_race_traits), 2)}

        # Create character and generate ability scores with racial modifiers
        player_character = Character(char_class=hero, character_abilities=character_abilities, racial_traits=racial_traits)

        # Set the chosen_race attribute after creating the character
        player_character.chosen_race = chosen_race

        # Apply racial modifiers
        player_character.apply_racial_modifiers()

        # Print equipment and modifiers
        columns, _ = shutil.get_terminal_size() 
        print(f"\n{Fore.GREEN + Style.NORMAL}Equipment and Spells:")
        print(Fore.GREEN + Style.NORMAL + textwrap.fill(f"Items: (Armor) {player_character.equipment['armor']} (Weapon) {player_character.equipment['weapon']} (Shield) {player_character.equipment['shield']}", width=columns))
        print("")
        print(Fore.GREEN + Style.NORMAL + textwrap.fill(f"Potions: {player_character.equipment['potions']}", width=columns))
        print("")
        print(Fore.GREEN + Style.NORMAL + textwrap.fill(f"Scrolls: {player_character.equipment['scrolls']}", width=columns))
        print("")
        print(Fore.GREEN + Style.NORMAL+ textwrap.fill(f"Spells: (Arcane) {player_character.equipment['arcane_spells']} (Divine) {player_character.equipment['divine_spells']}\n", width=columns))
        armor_modifier = player_character.calculate_armor_bonus(player_character.equipment['armor'], player_character.shield_modifier)
        weapon_modifier = player_character.calculate_tohit(player_character.equipment['bab'])
        initiative_modifier = player_character.calculate_init_bonus()

        #print tests
        #print(f"Armor Modifier: {armor_modifier}")
        #print(f"Weapon Modifier: {weapon_modifier}")

        #calls function to print player character
        character_creation(hero, player_character.abilities, player_character.hp, home_town, worlds, chosen_race, racial_modifiers, armor_modifier, weapon_modifier, initiative_modifier)

        if worlds == "Scarn":
            #monster dictionary
            monster_details_list = [
                {'name': 'Goblin', 'armor_class': 15, 'hit_points': 5, 'to_hit': 2, 'initiative': 1, 'damage': random.randint(1, 6)},
                {'name': 'Skeleton', 'armor_class': 15, 'hit_points': 6, 'to_hit': 1, 'initiative': 5, 'damage': random.randint(1, 6)+1},
                {'name': 'Dire Rat', 'armor_class': 15, 'hit_points': 5, 'to_hit': 4, 'initiative': 3, 'damage': random.randint(1, 4)}
            ]

            #Randomly choose a monster details dictionary
            chosen_monster_details = random.choice(monster_details_list)

            #information for object monster
            monster_name = chosen_monster_details['name']
            armor_class = chosen_monster_details['armor_class']
            hit_points = chosen_monster_details['hit_points']
            to_hit = chosen_monster_details['to_hit']
            initiative = chosen_monster_details['initiative']
            damage = chosen_monster_details['damage']

            nonfaerun_hero(hero, home_town, worlds, exit_message, player_character, monster_name, chosen_monster_details, armor_class, hit_points, damage, to_hit, initiative)

        elif worlds == "Krynn":
            #monster dictionary
            monster_details_list = [
                {'name': 'Goblin', 'armor_class': 15, 'hit_points': 5, 'to_hit': 2, 'initiative': 1, 'damage': random.randint(1, 6)},
                {'name': 'Skeleton', 'armor_class': 15, 'hit_points': 6, 'to_hit': 1, 'initiative': 5, 'damage': random.randint(1, 6)+1},
                {'name': 'Dire Rat', 'armor_class': 15, 'hit_points': 5, 'to_hit': 4, 'initiative': 3, 'damage': random.randint(1, 4)}
            ]

            #Randomly choose a monster details dictionary
            chosen_monster_details = random.choice(monster_details_list)

            #information for object monster
            monster_name = chosen_monster_details['name']
            armor_class = chosen_monster_details['armor_class']
            hit_points = chosen_monster_details['hit_points']
            to_hit = chosen_monster_details['to_hit']
            initiative = chosen_monster_details['initiative']
            damage = chosen_monster_details['damage']

            nonfaerun_hero(hero, home_town, worlds, exit_message, player_character, monster_name, chosen_monster_details, armor_class, hit_points, damage, to_hit, initiative)

        elif worlds == "Toril":
            #monster dictionary
            monster_details_list = [
                {'name': 'Goblin', 'armor_class': 15, 'hit_points': 5, 'to_hit': 2, 'initiative': 1, 'damage': random.randint(1, 6)},
                {'name': 'Skeleton', 'armor_class': 15, 'hit_points': 6, 'to_hit': 1, 'initiative': 5, 'damage': random.randint(1, 6)+1},
                {'name': 'Dire Rat', 'armor_class': 15, 'hit_points': 5, 'to_hit': 4, 'initiative': 3, 'damage': random.randint(1, 4)}
            ]

            #Randomly choose a monster details dictionary
            chosen_monster_details = random.choice(monster_details_list)

            #information for object monster
            monster_name = chosen_monster_details['name']
            armor_class = chosen_monster_details['armor_class']
            hit_points = chosen_monster_details['hit_points']
            to_hit = chosen_monster_details['to_hit']
            initiative = chosen_monster_details['initiative']
            damage = chosen_monster_details['damage']

            faerun_hero(hero, home_town, worlds, exit_message, player_character, monster_name, chosen_monster_details, armor_class, hit_points, damage, to_hit, initiative)