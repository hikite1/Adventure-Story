# Imports random function from the Python library
import random
from colorama import init, Fore, Style
init(autoreset=True)
# Imports custom modules
from adventure_pkg.story_functions import character_creation, faerun_story, non_faerun_story, greeting, leave_game, faerun_hero, nonfaerun_hero, baldurs_gate, invalid, win_game
from adventure_pkg.character_functions import Character

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
chosen_race = ""
racial_modifiers = ""
total_to_hit = ""
bab = ""
strength_mod = ""

character_abilities = {
    "Cleric": ["Wisdom", "Constitution", "Charisma", "Intelligence", "Strength", "Dexterity"],
    "Fighter": ["Strength", "Dexterity", "Constitution", "Wisdom", "Intelligence", "Charisma"],
    "Rogue": ["Dexterity", "Intelligence", "Wisdom", "Strength", "Charisma", "Constitution"],
    "Sorcerer": ["Charisma", "Constitution", "Dexterity", "Intelligence", "Wisdom", "Strength"],
    "Wizard": ["Intelligence", "Constitution", "Dexterity", "Wisdom", "Strength", "Charisma"],
}

# Add more character classes as needed

racial_traits = {
    "Dwarf": ["Constitution", 2, "Charisma", -2],
    "Elf": ["Dexterity", 2, "Constitution", -2],
    "Human": [],
}

# Main while loop shell containing nested while loops
while True:
    greeting()
    valid_world = False

    # Beginning of the game prompt function in a nested while loop
    world = input(f"\n{Fore.CYAN + Style.NORMAL}What home world would you like to be from?\nPlease choose a number:\n\n1) Ghelspad\n2) Krynn\n3) Toril\n\n")

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
        print(f"\n\n{Fore.CYAN + Style.NORMAL}Choose your Hero:")
        for i, hero_class in enumerate(character_abilities.keys(), 1):
            print(f"{Fore.CYAN + Style.NORMAL}{i}){Fore.CYAN + Style.NORMAL} {hero_class}")

        hero_choice = input(f"\n{Fore.CYAN + Style.NORMAL}Please select a number (or type 'Exit' to exit): ")

        if hero_choice.lower() == "exit":
            # Handle exit
            exit_message, npc1, npc_1, enemies, creatures = leave_game(npc_1, creatures, home_town, worlds)
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

        # Now, let the user choose a race
        print(f"\n\n{Fore.CYAN + Style.NORMAL}Choose your Race:")
        for i, race in enumerate(racial_traits.keys(), 1):
            print(f"{Fore.CYAN + Style.NORMAL}{i}){Fore.CYAN + Style.NORMAL} {race}")

        race_choice = input(f"\n{Fore.CYAN + Style.NORMAL}Please select a number: ")

        try:
            race_index = int(race_choice)
            if 1 <= race_index <= len(racial_traits):
                chosen_race = list(racial_traits.keys())[race_index - 1]
            else:
                raise ValueError
        except ValueError:
            invalid_entry = invalid()
            print(invalid_entry)
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
        print("\nEquipment and Modifiers:")
        print(f"Armor: {player_character.equipment['armor']}")
        print(f"Weapon: {player_character.equipment['weapon']}")
        armor_modifier = player_character.calculate_armor_bonus(player_character.equipment['armor'], player_character.shield_modifier)
        weapon_modifier = player_character.weapon_modifier
        print(f"Armor Modifier: {armor_modifier}")
        print(f"Weapon Modifier: {weapon_modifier}")
        # Call the method to calculate total_to_hit
        #total_to_hit = player_character.calculate_to_hit()
        #print(f"Total To-Hit Bonus outside method: {total_to_hit}")
        
        # Print ability scores
        print(f"\nAbility Scores:")
        print(player_character.abilities)

        # Print ability scores
        fate, hometown_description = character_creation(hero, player_character.abilities, player_character.hp, home_town, worlds, chosen_race, racial_modifiers, armor_modifier, total_to_hit)

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
