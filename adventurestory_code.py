#imports random function from python library
import random
#imports custom modules
from adventure_pkg.story_functions import generate_strings, faerun_story, non_faerun_story, greeting, leave_game, faerun_hero, nonfaerun_hero, baldurs_gate, invalid, win_game

#initializing variables
toril = "Toril"
krynn = "Krynn"
ghelspad = "Ghelspad"
world = ""

cleric = "Cleric"
wizard = "Wizard"
sorcerer = "Sorcerer"
fighter = "Fighter"
rogue = "Rogue"
npc_1 = ""
npc_2 = ""
npc_3 = ""
creatures = ""
enemies = []
self = ""

exit = "Exit"
play_again = ""
enter = ""
exit_message = ""
dice_result = ""
world = ""
battle = ""
hero = ""
character = ""
my_hp = ""
my_damage = ""
home_town = ""

#main while loop shell containing nested while loops
while True:
    greeting()
    valid_world = False
    #beginning of the game prompt function in a nested while loop
    world = input("\nWhat home world would you like to be from?\nPlease choose a number:\n\n1) Ghelspad\n2) Krynn\n3) Toril\n\n")
    #if statement to give player a choice of starting world in a while loop to allow a reprompt from world input if incorrect input is given
    while not valid_world:
        if world == "Ghelspad" or world == "1":#else condition is making typing Ghelspad make that condition True
            cities = ["Bard's Gate", "Hedrad", "Mithril"]
            home_town = random.choice(cities)
            #initializing worlds and a stored variable to be accessed as the story progressess if this is returned True
            worlds = ghelspad
            #initializing _origin to allow access to the origin_story function from an imported module
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
        #initializing hero prompt. Player can choose hero and it will store variable in 'hero' to create hero object to be accessed as the story progressess.
        hero = input("\n\nChoose your Hero: \nPlease select a number.\n1) Fighter\n2) Rogue\n3) Sorcerer\n4) Wizard\n5) Exit\n\n")
        hero_chosen = False
        while not hero_chosen:           
            #if and elif conditons are setting the individual variables of each hero and referencing variables set in the beginning
            if hero == "Fighter" or hero == "1":
                #Object_Characters.actual_object_character(self, hero)
                #Dice_Rolls.attack(self, hero)
                character = fighter
                #initializing fate and _description to allow access to the generate_strings function from an imported module
                fate, hometown_description = generate_strings(character, my_hp, my_damage, home_town)
                print(fate)
                hero_chosen = True
            elif hero == "Rogue" or hero == "2":
                character = rogue
                fate, hometown_description = generate_strings(character, my_hp, my_damage, home_town)
                print(fate)
                hero_chosen = True
            elif hero == "Sorcerer" or hero == "3":
                character = sorcerer
                fate, hometown_description = generate_strings(character, my_hp, my_damage, home_town)
                print(fate)
                print(hometown_description)
                hero_chosen = True
            elif hero == "Wizard" or hero == "4":
                character = wizard
                fate, hometown_description = generate_strings(character, my_hp, my_damage, home_town)
                print(fate)
                hero_chosen = True
                #this allows player to leave the game
            elif hero == "Exit" or hero == "5":
                exit_message, npc1, npc_1, enemies, creatures = leave_game(npc_1, creatures, home_town, worlds)
                print(exit_message)
                hero_chosen = True
                quit()
            else: #reprompt hero input above and continue the code after correct input is given
                invalid_entry = invalid()
                print(invalid_entry)
                hero = input("\n\nChoose your Hero: \nPlease select a number.\n1) Fighter\n2) Rogue\n3) Sorcerer\n4) Wizard\n5) Exit\n\n")
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