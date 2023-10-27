#story_functions.py

import random
from colorama import init, Fore, Style
init(autoreset=True)
import shutil
import textwrap

from  adventure_pkg.battle_functions import Combat_Actions
from adventure_pkg.character_functions import Abilities, Character
from adventure_pkg.monster_battle_functions import Monster

#print("story_functions is being imported.")

def greeting():
    #get terminal size
    columns, _ = shutil.get_terminal_size() 

    print("Columns:", columns)

    # Check if screen size is smaller than a threshold
    if columns < 80:
        #Adjusted ASCII art for smaller screens
        closing_parenthesis = ")"
        zero = "(O"
        offset = 1
        terminal_width = shutil.get_terminal_size().columns
        formatted_text = f"{Fore.YELLOW + Style.NORMAL + closing_parenthesis.ljust(1)}{zero.rjust(terminal_width - offset)}"

        print("")
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(formatted_text)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(Fore.WHITE + Style.BRIGHT +
        textwrap.fill("Welcome to Alaundo's Last Prophecy Heroes! An adventure for the ages awaits you...", width=columns))
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(formatted_text)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print("")
        
    elif columns >= 80:
        #print statement
        greeting_message = print(Fore.YELLOW + Style.NORMAL +"\n         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
        Fore.YELLOW + Style.NORMAL +"         |   ",Fore.WHITE + Style.BRIGHT +"Welcome to Alaundo's Last Prophecy Heroes! An adventure for",Fore.YELLOW + Style.NORMAL+"             |\n",
        Fore.YELLOW + Style.NORMAL +"         |   ",Fore.WHITE + Style.BRIGHT +"the ages awaits you...",Fore.YELLOW + Style.NORMAL+"                                                  |\n",
        Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n") 

    print(f'{Fore.WHITE + Style.BRIGHT}Link to "In the Beginning" video: {Fore.BLUE + Style.BRIGHT}\033[4mhttps://drive.google.com/file/d/1XjsnztqL1XEUXs5FCsQUyjtY45OKWhfB/view?usp=sharing\033[0m')

    return ""

def faerun_story():
    #get terminal size
    columns, _ = shutil.get_terminal_size() 

    # Check if screen size is smaller than a threshold
    if columns < 80:
        # Adjusted ASCII art for smaller screens
        closing_parenthesis = ")"
        zero = "(O"
        offset = 1
        terminal_width = shutil.get_terminal_size().columns
        formatted_text = f"{Fore.YELLOW + Style.NORMAL + closing_parenthesis.ljust(1)}{zero.rjust(terminal_width - offset)}"

        print("")
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(formatted_text)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(Fore.WHITE + Style.BRIGHT + 
              textwrap.fill("Over the past few years undead and demonic attacks have been destroying random civilizations. So far it has been in undomesticated areas, but fearexists that soon all will be at war. The feeling is that Demon Lords are stirring in the dark recesses  of the unknown corners of the world.", width=columns))
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(formatted_text)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print("")

        input(f"{Fore.CYAN + Style.NORMAL}Press Enter")
        print(f'\n{Fore.WHITE + Style.BRIGHT}Link to "Faerun Greeting" video: {Fore.BLUE + Style.BRIGHT}\033[4mhttps://drive.google.com/file/d/1UcdWvvmPz3ijb94NlK7zLrZlPeAofuZQ/view?usp=drive_link\033[0m')

        return ""

    elif columns >= 80:
        #print statement 
        faerun_origin = print(Fore.YELLOW + Style.NORMAL +"\n         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
        Fore.YELLOW + Style.NORMAL +"         |   ",Fore.WHITE + Style.BRIGHT +"Over the past few years undead and demonic attacks have been destroying",Fore.YELLOW + Style.NORMAL+" |\n",
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"random civilizations. So far it has been in undomesticated areas, but fear",Fore.YELLOW + Style.NORMAL+"|\n",
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"exists that soon all will be at war. The feeling is that Demon Lords are",Fore.YELLOW + Style.NORMAL+"  |\n",
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"stirring in the dark recesses  of the unknown corners of the world.",Fore.YELLOW + Style.NORMAL+"       |\n",
        Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        input(f"{Fore.CYAN + Style.NORMAL}Press Enter")
        print(f'\n{Fore.WHITE + Style.BRIGHT}Link to "Faerun Greeting" video: {Fore.BLUE + Style.BRIGHT}\033[4mhttps://drive.google.com/file/d/1UcdWvvmPz3ijb94NlK7zLrZlPeAofuZQ/view?usp=drive_link\033[0m')

        return ""

def non_faerun_story():
    #get terminal size
    columns, _ = shutil.get_terminal_size() 

    # Check if screen size is smaller than a threshold
    if columns < 80:
        # Adjusted ASCII art for smaller screens
        closing_parenthesis = ")"
        zero = "(O"
        offset = 1
        terminal_width = shutil.get_terminal_size().columns
        formatted_text = f"{Fore.YELLOW + Style.NORMAL + closing_parenthesis.ljust(1)}{zero.rjust(terminal_width - offset)}"

        print("")
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(formatted_text)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(Fore.WHITE + Style.BRIGHT + 
              textwrap.fill("About ten years ago a force of undead started razing cities, assault, then it was demons and abyssal war machines. They would slowly transform the city to be undead in their ranks. Over time you fought your sister, your mother, friend, cousin. The list goes on. They have dominated your world, and now you are old enough to join the resistance ranks.", width=columns))
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(formatted_text)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print("")

        input(f"{Fore.CYAN + Style.NORMAL}Press Enter") 
        print(f'{Fore.WHITE + Style.BRIGHT}Link to "Scarn Greeting" video: {Fore.BLUE + Style.BRIGHT}\033[4mhttps://drive.google.com/file/d/1StmNwHW-2OelQTpHJkfhUP_04fWWwLU8/view?usp=sharing\033[0m')
        print("")
        print(f'{Fore.WHITE + Style.BRIGHT}Link to "Krynn Greeting" video: {Fore.BLUE + Style.BRIGHT}\033[4mhttps://drive.google.com/file/d/1wijGJ6sYpPIxul_TsHkHusRMdLMVZXFi/view?usp=drive_link\033[0m')

        return ""

    elif columns >= 80:
        #print statement
        non_faerun_origin = print(Fore.YELLOW + Style.NORMAL +"         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
        Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +"About ten years ago a force of undead started razing cities,",Fore.YELLOW + Style.NORMAL+"          |\n",
        Fore.YELLOW + Style.NORMAL +"         |  ",Fore.WHITE + Style.BRIGHT +"assault, then it was demons and abyssal war machines. They would",Fore.YELLOW + Style.NORMAL+"         |\n", 
        Fore.YELLOW + Style.NORMAL +"         |  ",Fore.WHITE + Style.BRIGHT +"slowly transform the city to be undead in their ranks. Over time you",Fore.YELLOW + Style.NORMAL+"     |\n", 
        Fore.YELLOW + Style.NORMAL +"         |  ",Fore.WHITE + Style.BRIGHT +"fought your sister, your mother, friend, cousin. The list goes on.",Fore.YELLOW + Style.NORMAL+"       |\n", 
        Fore.YELLOW + Style.NORMAL +"         |  ",Fore.WHITE + Style.BRIGHT +"They have dominated your world, and now you are old enough",Fore.YELLOW + Style.NORMAL+"               |\n",
        Fore.YELLOW + Style.NORMAL +"         |  ",Fore.WHITE + Style.BRIGHT +"to join the resistance ranks.",Fore.YELLOW + Style.NORMAL+"                                            |\n",
        Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n", 
        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        input(f"{Fore.CYAN + Style.NORMAL}Press Enter") 
        print(f'{Fore.WHITE + Style.BRIGHT}Link to "Scarn Greeting" video: {Fore.BLUE + Style.BRIGHT}\033[4mhttps://drive.google.com/file/d/1StmNwHW-2OelQTpHJkfhUP_04fWWwLU8/view?usp=sharing\033[0m')
        print("")
        print(f'{Fore.WHITE + Style.BRIGHT}Link to "Krynn Greeting" video: {Fore.BLUE + Style.BRIGHT}\033[4mhttps://drive.google.com/file/d/1wijGJ6sYpPIxul_TsHkHusRMdLMVZXFi/view?usp=drive_link\033[0m')

        return ""

def character_creation(hero_class, ability_scores, hp, home_town, worlds, chosen_race, racial_modifiers, armor_modifier, weapon_modifier, initiative_modifier):
    #get terminal size
    columns, _ = shutil.get_terminal_size() 

    # Display the ability scores with modifiers
    ability_scores_description = [
        f"{attribute}: {value} ({ability_scores.calculate_modifier(attribute.lower())})"
        for attribute, value in vars(ability_scores).items()
    ]
    ability_scores_string = '\n'.join(ability_scores_description)

    # Set the hero name
    hero_name = f"{Fore.WHITE + Style.BRIGHT}{hero_class}"

    # Set the race name
    race_name = f"{Fore.WHITE + Style.BRIGHT}{chosen_race}"

    # Calculate the remaining space for the side border
    total_width = 46
    side_border_width = total_width - len(hero_name) - 1  # Subtract 1 for the space after hero name

    # Calculate the indentation for ability scores
    top_ability_indentation = ' ' * 5  # Initial indentation for the top ability
    other_ability_indentation = ' ' * 5  # Initial indentation for other abilities

    # Add piping symbols to the left and right of each ability score line
    indented_ability_scores_piped = [
        Fore.YELLOW + Style.NORMAL + f"{' ' * (9 + i)}|{Fore.WHITE + Style.BRIGHT}{top_ability_indentation}{line.strip()}{' ' * (72 - len(line.strip()))}"+ Fore.YELLOW + Style.NORMAL + "|"
        if i == 0
        else Fore.YELLOW + Style.NORMAL + f"{' ' * 10}|{Fore.WHITE + Style.BRIGHT}{other_ability_indentation}{line.strip()}{' ' * (72 - len(line.strip()))}"+ Fore.YELLOW + Style.NORMAL + "|"
        for i, line in enumerate(ability_scores_string.split('\n'))
    ]

    character_name = input(f"\n{Fore.CYAN + Style.NORMAL}Type in the name of your character: ")
    print('')

    # Check if screen size is smaller than a threshold
    if columns < 80:
        # Adjusted ASCII art for smaller screens
        closing_parenthesis = ")"
        zero = "(O"
        offset = 1
        terminal_width = shutil.get_terminal_size().columns
        formatted_text = f"{Fore.YELLOW + Style.NORMAL + closing_parenthesis.ljust(1)}{zero.rjust(terminal_width - offset)}"

        print("")
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(formatted_text)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(Fore.WHITE + Style.BRIGHT + textwrap.fill("Your fate is intertwined with the:", width=columns))
        print(Fore.WHITE + Style.BRIGHT + (f"{race_name} {hero_name}"))
        print("")
        print(f"{Fore.WHITE + Style.BRIGHT}Racial Traits:")
        print("\n".join([f"{Fore.WHITE + Style.BRIGHT}{trait} {modifier}" for trait, modifier in racial_modifiers.items()]))
        print("")
        print(f"{Fore.WHITE + Style.BRIGHT}Character Name: {character_name.ljust(10)}\n")
        print(f"{Fore.WHITE + Style.BRIGHT}Location: \nWorld - {worlds.ljust(10)} \nArea - {home_town.ljust(15)}\n")
        print(Fore.WHITE + Style.BRIGHT + ability_scores_string)
        print(f"{Fore.WHITE + Style.BRIGHT}HP: {str(hp).rjust(3)}")
        print(f"{Fore.WHITE + Style.BRIGHT}AC: {str(armor_modifier).rjust(3)}")
        print(f"{Fore.WHITE + Style.BRIGHT}Attack: +{str(weapon_modifier).ljust(3)}")
        print(f"{Fore.WHITE + Style.BRIGHT}Initiative: +{str(initiative_modifier).ljust(3)}")
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(formatted_text)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print("")

        input(f"{Fore.CYAN + Style.NORMAL}Press Enter\n\n") 

        print("")
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(formatted_text)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(Fore.WHITE + Style.BRIGHT + 
              textwrap.fill(f"You hale from a town called {home_town}. You have spent the past few months under the mentorship of a Master {hero_name} and have been sensing that it is time for you to go out into the world and test your new skills.", width=columns) 
              + Fore.YELLOW + Style.NORMAL)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(formatted_text)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print("")

        input(f"{Fore.CYAN + Style.NORMAL}Press Enter") 

        return ""

    elif columns >= 80:
        #print statement 
        fate = print(
            Fore.YELLOW + Style.NORMAL + "         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
            Fore.YELLOW + Style.NORMAL + "       =O)                                                                            (O=\n",
            Fore.YELLOW + Style.NORMAL + "        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
            Fore.YELLOW + Style.NORMAL + "         |                                                                             |\n",
            Fore.YELLOW + Style.NORMAL + f"         |     {Fore.WHITE + Style.BRIGHT}Your fate is intertwined with the {race_name.ljust(10)} {hero_name.ljust(10)}"+ Fore.YELLOW + Style.NORMAL + "                             \n",
            Fore.YELLOW + Style.NORMAL + f"         |     {Fore.WHITE + Style.BRIGHT}Racial Traits: {', '.join([f'{trait} {modifier}' for trait, modifier in racial_modifiers.items()])}"+ Fore.YELLOW + Style.NORMAL + "                             \n",
            Fore.YELLOW + Style.NORMAL + "         |                                                                             |",
            Fore.YELLOW + Style.NORMAL + f"\n{' ' * 10}|{Fore.WHITE + Style.BRIGHT}     Character Name: {character_name.ljust(10)}{' ' * 46}"+ Fore.YELLOW + Style.NORMAL + "|\n",
            Fore.YELLOW + Style.NORMAL + f"         |     {Fore.WHITE + Style.BRIGHT}Location: World - {worlds.ljust(10)}, Area - {home_town.ljust(15)}"+ Fore.YELLOW + Style.NORMAL + "                    |\n",
            Fore.WHITE + Style.BRIGHT + '\n'.join(indented_ability_scores_piped),
            Fore.YELLOW + Style.NORMAL + f"\n{' ' * 10}|{Fore.WHITE + Style.BRIGHT}     HP: {str(hp).rjust(3)}{' ' * 59}"+ Fore.YELLOW + Style.NORMAL + "      |\n",
            Fore.YELLOW + Style.NORMAL + f"{' ' * 9}|{Fore.WHITE + Style.BRIGHT}     AC: {str(armor_modifier).rjust(3)}{' ' * 59}"+ Fore.YELLOW + Style.NORMAL + "      |\n",
            Fore.YELLOW + Style.NORMAL + f"{' ' * 9}|{Fore.WHITE + Style.BRIGHT}     Attack: +{str(weapon_modifier).ljust(3)}{' ' * 59}"+ Fore.YELLOW + Style.NORMAL + " |\n",
            Fore.YELLOW + Style.NORMAL + f"{' ' * 9}|{Fore.WHITE + Style.BRIGHT}     Initiative: +{str(initiative_modifier).ljust(3)}{' ' * 56}"+ Fore.YELLOW + Style.NORMAL + "|\n",
            Fore.YELLOW + Style.NORMAL + "         |                                                                             |\n",
            Fore.YELLOW + Style.NORMAL + "        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
            Fore.YELLOW + Style.NORMAL + "       =O)                                                                            (O=\n",
            Fore.YELLOW + Style.NORMAL + "        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        )
        input(f"{Fore.CYAN + Style.NORMAL}Press Enter\n\n") 

        #print statement
        hometown_description = print(Fore.YELLOW + Style.NORMAL + "         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
                                    Fore.YELLOW + Style.NORMAL + "       =O)                                                                            (O=\n",
                                    Fore.YELLOW + Style.NORMAL + "        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
                                    Fore.YELLOW + Style.NORMAL + "         |                                                                             |\n",
                                    Fore.YELLOW + Style.NORMAL + f"         |     {Fore.WHITE + Style.BRIGHT}You hale from a town called {home_town}.",
                                    Fore.YELLOW + Style.NORMAL + "                                  \n",
                                    Fore.YELLOW + Style.NORMAL + "         |    ", Fore.WHITE + Style.BRIGHT + "You have spent the past few months under the mentorship",
                                    Fore.YELLOW + Style.NORMAL + "                |\n",
                                    Fore.YELLOW + Style.NORMAL + f"         |     {Fore.WHITE + Style.BRIGHT}of a Master {hero_name} and have been sensing",
                                    Fore.YELLOW + Style.NORMAL + "                              \n",
                                    Fore.YELLOW + Style.NORMAL + "         |    ", Fore.WHITE + Style.BRIGHT + "that it is time for you to go out into the world",
                                    Fore.YELLOW + Style.NORMAL + "                       |\n",
                                    Fore.YELLOW + Style.NORMAL + f"         |     {Fore.WHITE + Style.BRIGHT}and test your new skills.",
                                    Fore.YELLOW + Style.NORMAL + "                                              |\n",
                                    Fore.YELLOW + Style.NORMAL + "         |                                                                             |\n",
                                    Fore.YELLOW + Style.NORMAL + "        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
                                    Fore.YELLOW + Style.NORMAL + "       =O)                                                                            (O=\n",
                                    Fore.YELLOW + Style.NORMAL + "        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        input(f"{Fore.CYAN + Style.NORMAL}Press Enter\n\n") 

        return ""

def faerun_hero(hero_class, home_town, worlds, exit_message, player_character, monster_name, chosen_monster_details, armor_class, hit_points, damage, to_hit, initiative):
    #random npc selection
    npc1 = ["Cleric", "Fighter", "Rogue", "Sorcerer", "Wizard"]
    npc_1 = random.choice(npc1)
    npc2 = ["Cleric", "Fighter", "Rogue", "Sorcerer", "Wizard"]
    npc_2 = random.choice(npc2)
    npc3 = ["Cleric", "Fighter", "Rogue", "Sorcerer", "Wizard"]
    npc_3 = random.choice(npc3)
    
    armor_modifier = player_character.calculate_armor_bonus(player_character.equipment['armor'],
                                                            player_character.shield_modifier)

    #Define hero abilities
    hero_abilities = Abilities(
        Strength=player_character.abilities.Strength,
        Dexterity=player_character.abilities.Dexterity,
        Constitution=player_character.abilities.Constitution,
        Intelligence=player_character.abilities.Intelligence,
        Wisdom=player_character.abilities.Wisdom,
        Charisma=player_character.abilities.Charisma
    )

    #Create a Combat_Actions object for the hero
    hero_object = Combat_Actions(
        character=player_character,
        armor_class=armor_modifier,
        hit_points=player_character.hp,
        abilities=hero_abilities
    )

    #Create Monster object based on chosen_monster_details dictionary
    chosen_monster_object = Monster(
        name=chosen_monster_details['name'],
        armor_class=chosen_monster_details['armor_class'],
        hit_points=chosen_monster_details['hit_points'],
        to_hit=chosen_monster_details['to_hit'],
        initiative=chosen_monster_details['initiative'],
        damage=chosen_monster_details['damage']
    )

    #get terminal size
    columns, _ = shutil.get_terminal_size() 

    if columns < 80:
        # Adjusted ASCII art for smaller screens
        closing_parenthesis = ")"
        zero = "(O"
        offset = 2
        terminal_width = shutil.get_terminal_size().columns
        formatted_text = f"{Fore.YELLOW + Style.NORMAL + closing_parenthesis.ljust(1)}{zero.rjust(terminal_width - offset)}"

        begin_faerun_hero = print(
            f"\n{Fore.YELLOW + Style.NORMAL}{'~' * columns}"
            f"{formatted_text}"
            f"{Fore.YELLOW + Style.NORMAL}{'~' * columns}"
            f"{Fore.WHITE + Style.BRIGHT}{textwrap.fill(f'You decide to leave your {hero_class} mentor in {home_town} and travel to Baldurs Gate. There are plenty of caravans headed to the event. You are able to find employment easily enough and it is up to you if you think anyone needs to know of your {hero_class} abilities or not.', width=columns)}"
            f"\n{Fore.YELLOW + Style.NORMAL}{'~' * columns}"
            f"{formatted_text}"
            f"{Fore.YELLOW + Style.NORMAL}{'~' * columns}"
            "\n"
        )

        input(f"{Fore.CYAN + Style.NORMAL}Press Enter")

        print("")
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(formatted_text)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(Fore.WHITE + Style.BRIGHT + 
            textwrap.fill(f"{hero_class} of {worlds} you have been tasked to defend the caravan if necessary in return for room and board on the voyage to Baldur's Gate. Each wagon has four mercenaries for it defense. Yours has you, a {npc_1}, a {npc_2}, and a {npc_3}. A group of {monster_name}s is seen using the shadows from bushes clustered together ahead of your wagon. A {npc_1} sees these {monster_name}s and alerts the wagon to veer off and group with another wagon. Your group has discussed strategy prior and everyone egins to move and execute the plan.", width=columns))
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(formatted_text)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print("")

        input(f"{Fore.CYAN + Style.NORMAL}Press Enter")

    elif columns >= 80:
        #print statement
        begin_faerun_hero = print(
            Fore.YELLOW + Style.NORMAL + "         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
            Fore.YELLOW + Style.NORMAL + "       =O)                                                                            (O=\n",
            Fore.YELLOW + Style.NORMAL + "        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
            Fore.YELLOW + Style.NORMAL + "         |                                                                             |\n",
            Fore.YELLOW + Style.NORMAL + "         |     ", Fore.WHITE + Style.BRIGHT + f"You decide to leave your {hero_class} mentor in {home_town}",
            Fore.YELLOW + Style.NORMAL + "                                  \n",
            Fore.YELLOW + Style.NORMAL + "         |     ", Fore.WHITE + Style.BRIGHT + "and travel to Baldur's Gate. There are plenty of",
            Fore.YELLOW + Style.NORMAL + "                      |\n",
            Fore.YELLOW + Style.NORMAL + "         |     ", Fore.WHITE + Style.BRIGHT + "caravans headed to the event. You are able to find employment",
            Fore.YELLOW + Style.NORMAL + "         |\n",
            Fore.YELLOW + Style.NORMAL + "         |     ", Fore.WHITE + Style.BRIGHT + "easily enough and it is up to you if you think anyone",
            Fore.YELLOW + Style.NORMAL + "                 |\n",
            Fore.YELLOW + Style.NORMAL + "         |     ", Fore.WHITE + Style.BRIGHT + f"needs to know of your {hero_class} abilities or not.",
            Fore.YELLOW + Style.NORMAL + "                                             \n",
            Fore.YELLOW + Style.NORMAL + "         |                                                                             |\n",
            Fore.YELLOW + Style.NORMAL + "        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
            Fore.YELLOW + Style.NORMAL + "       =O)                                                                            (O=\n",
            Fore.YELLOW + Style.NORMAL + "        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        
        input(f"{Fore.CYAN + Style.NORMAL}Press Enter")

        #print statement
        faerun_battle = print(
            Fore.YELLOW + Style.NORMAL + "         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
            Fore.YELLOW + Style.NORMAL + "       =O)                                                                            (O=\n",
            Fore.YELLOW + Style.NORMAL + "        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
            Fore.YELLOW + Style.NORMAL + "         |                                                                             |\n",
            Fore.YELLOW + Style.NORMAL + "         |     ", Fore.WHITE + Style.BRIGHT + f"{hero_class} of {worlds} you have been tasked to defend the caravan",
            Fore.YELLOW + Style.NORMAL + "         \n",
            Fore.YELLOW + Style.NORMAL + "         | ", Fore.WHITE + Style.BRIGHT + "if necessary in return for room and board on the voyage to Baldur's",
            Fore.YELLOW + Style.NORMAL + "       |\n",
            Fore.YELLOW + Style.NORMAL + "         | ", Fore.WHITE + Style.BRIGHT + "Gate. Each wagon has four mercenaries for it defense. Yours has you,",
            Fore.YELLOW + Style.NORMAL + "      |\n",
            Fore.YELLOW + Style.NORMAL + "         | ", Fore.WHITE + Style.BRIGHT + f"a {npc_1}, a {npc_2}, and a {npc_3}. A group of {monster_name}s is seen using ",
            Fore.YELLOW + Style.NORMAL + "         \n",
            Fore.YELLOW + Style.NORMAL + "         |", Fore.WHITE + Style.BRIGHT, "the shadows from bushes clustered together ahead of your wagon. A ",
            Fore.YELLOW + Style.NORMAL + "        |\n",
            Fore.YELLOW + Style.NORMAL + "         | ", Fore.WHITE + Style.BRIGHT + f"{npc_1} sees these {monster_name}s and alerts the wagon to veer off and group",
            Fore.YELLOW + Style.NORMAL + "       \n",
            Fore.YELLOW + Style.NORMAL + "         | ", Fore.WHITE + Style.BRIGHT + "with another wagon. Your group has discussed strategy prior and everyone",
            Fore.YELLOW + Style.NORMAL + "  |\n",
            Fore.YELLOW + Style.NORMAL + "         | ", Fore.WHITE + Style.BRIGHT + "begins to move and execute the plan.",
            Fore.YELLOW + Style.NORMAL + "         \n",
            Fore.YELLOW + Style.NORMAL + "         |                                                                             |\n",
            Fore.YELLOW + Style.NORMAL + "        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
            Fore.YELLOW + Style.NORMAL + "       =O)                                                                            (O=\n",
            Fore.YELLOW + Style.NORMAL + "        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        
        input(f"{Fore.CYAN + Style.NORMAL}Press Enter")

    #print(f"Chosen monster: {monster_name}")
    #print(f"Armor Class: {armor_class}")
    #print(f"Hit Points: {hit_points}")
    #print(f"To Hit: {to_hit}")
    #print(f"Initiative: {initiative}")
    #print(f"Damage: {damage}")

    #COMBAT BEGINS HERE

    battle = input(f"{Fore.CYAN + Style.NORMAL}Do you...\n1) Follow orders\n2) Go AWOL(Quit the story)\n\n")

    if battle == "1":
        print(begin_faerun_hero)
        while hero_object.is_alive() and chosen_monster_object.is_alive():
            print(f"\n{Fore.GREEN + Style.BRIGHT}==== Battle ====")
            print(f"{Fore.GREEN + Style.BRIGHT}{hero_class} HP: {hero_object.hit_points}")
            print(f"{Fore.GREEN + Style.BRIGHT}{monster_name} HP: {chosen_monster_object.hit_points}")

            actions = input(f"\n{Fore.CYAN + Style.NORMAL}Do you...\n1) Attack\n2) Run away(Quit the story)\n\n").lower()

            #print(f'\nMonster: {chosen_monster_details}\n')

            if actions == "1":
                #Hero attacks
                total_damage = hero_object.attack(chosen_monster_object)

                #weapon_damage = hero_object.character.calculate_weapon_modifier(hero_object.character.equipment['weapon'])
                #print(f"Debug: Total Damage: {total_damage} (Weapon Damage: {weapon_damage}).")

                if total_damage > 0:
                    chosen_monster_object.take_damage(total_damage)
                    print(f"{Fore.BLUE + Style.BRIGHT}You dealt {total_damage} damage to {monster_name}!")
                else:
                    print(f"{Fore.MAGENTA + Style.BRIGHT}You missed the attack on {monster_name}!")

                #Creature attacks
                if chosen_monster_object.is_alive():
                    monster_damage = chosen_monster_object.attack(hero_object)

                    #print(f"Debug: Monster Damage: {monster_damage}")

                    if monster_damage > 0:
                        hero_object.take_damage(monster_damage)
                        print(f"{Fore.MAGENTA + Style.BRIGHT}{monster_name} dealt {monster_damage} damage to the {hero_class}!")
                    else:
                        print(f"{Fore.BLUE + Style.BRIGHT}{monster_name} missed the attack on {hero_class}!")

                #Print the result of the battle
                if hero_object.is_alive() and not chosen_monster_object.is_alive():
                    #print statement
                    print(f"{Fore.BLUE + Style.BRIGHT}{hero_class} won the battle!")
                    print("")

                    if columns < 80:
                        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
                        print(formatted_text)
                        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
                        print(Fore.WHITE + Style.BRIGHT + textwrap.fill(f"Your {hero_class} abilities are amazing! Your group is fascinated by the display of your skills. With only one {monster_name} left, it runs away terrified at your decimation of its group. The rest of the journey goes by rather easily. The legends of Faerun are no match for seeing these wonders first hand. Whether you are seeing the Dalelands or the Swordcoast and the villages or iconic places of legend. You are even more sure that leaving {home_town} was the right choice. After you crest a hilltop you see your destination looms off in the distance.", width=columns))
                        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
                        print(formatted_text)
                        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
                        print("")

                        input(f"{Fore.CYAN + Style.NORMAL}Press Enter")

                        see_city= baldurs_gate()
                        print(see_city)

                        congratulations = win_game(worlds, home_town)
                        print(congratulations)

                    elif columns >= 80:
                        print(
                            Fore.YELLOW + Style.NORMAL + "         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
                            Fore.YELLOW + Style.NORMAL + "       =O)                                                                            (O=\n",
                            Fore.YELLOW + Style.NORMAL + "        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
                            Fore.YELLOW + Style.NORMAL + "         |                                                                             |\n",
                            Fore.YELLOW + Style.NORMAL + "         |     ", Fore.WHITE + Style.BRIGHT + f"Your {hero_class} abilities are amazing! Your group is fascinated by ",
                            Fore.YELLOW + Style.NORMAL + "         \n",
                            Fore.YELLOW + Style.NORMAL + "         | ", Fore.WHITE + Style.BRIGHT + f"the display of your skills. With only one {monster_name} left, it runs", Fore.YELLOW + Style.NORMAL + "     \n",
                            Fore.YELLOW + Style.NORMAL + "         | ", Fore.WHITE + Style.BRIGHT + "away terrified at your decimation of its group. The rest of the journey",
                            Fore.YELLOW + Style.NORMAL + "   |\n",
                            Fore.YELLOW + Style.NORMAL + "         | ", Fore.WHITE + Style.BRIGHT + "goes by rather easily. The legends of Faerun are no match for",
                            Fore.YELLOW + Style.NORMAL + "             |\n",
                            Fore.YELLOW + Style.NORMAL + "         | ", Fore.WHITE + Style.BRIGHT + "seeing these wonders first hand. Whether you are seeing the Dalelands", Fore.YELLOW + Style.NORMAL + "      |\n",
                            Fore.YELLOW + Style.NORMAL + "         | ", Fore.WHITE + Style.BRIGHT + "or the Swordcoast and the villages or iconic places of legend. You",
                            Fore.YELLOW + Style.NORMAL + "        |\n",
                            Fore.YELLOW + Style.NORMAL + "         | ", Fore.WHITE + Style.BRIGHT + f"are even more sure that leaving {home_town} was the right choice.",
                            Fore.YELLOW + Style.NORMAL + "     \n",
                            Fore.YELLOW + Style.NORMAL + "         | ", Fore.WHITE + Style.BRIGHT + "After you crest a hilltop you see your destination looms off",
                            Fore.YELLOW + Style.NORMAL + "              |\n",
                            Fore.YELLOW + Style.NORMAL + "         | ", Fore.WHITE + Style.BRIGHT + "in the distance.",
                            Fore.YELLOW + Style.NORMAL + "                                                          |\n",
                            Fore.YELLOW + Style.NORMAL + "         |                                                                             |\n",
                            Fore.YELLOW + Style.NORMAL + "        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
                            Fore.YELLOW + Style.NORMAL + "       =O)                                                                            (O=\n",
                            Fore.YELLOW + Style.NORMAL + "        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                    
                    input(f"{Fore.CYAN + Style.NORMAL}Press Enter")

                    see_city= baldurs_gate()
                    print(see_city)

                    congratulations = win_game(worlds, home_town)
                    print(congratulations)

                elif not hero_object.is_alive() and chosen_monster_object.is_alive():
                    #print statement
                    print(f"{Fore.MAGENTA + Style.BRIGHT}{monster_name} defeated {hero_class}. Game over.") 

                    if columns < 80:
                        print("")
                        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
                        print(formatted_text)
                        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
                        print(Fore.WHITE + Style.BRIGHT +
                        textwrap.fill(f"You now feel the rush of life leaving as the {monster_name} injured you fatally and your storied tale of heroism as a {hero_class} is over", width=columns))
                        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
                        print(formatted_text)
                        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
                        print("")
                        # Ask the player if they want to restart or exit
                        restart_option = input(f"{Fore.CYAN + Style.NORMAL}Do you want to restart? (yes/no): ").lower()
                        if restart_option == 'yes' or restart_option == 'y':
                            greeting()
                        elif restart_option == 'no' or restart_option == 'n':
                            quit()  # Exit the loop if the player doesn't want to restart  

                    elif columns >= 80: 
                        print(Fore.YELLOW + Style.NORMAL +"         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
                        Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
                        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
                        Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
                        Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"You now feel the rush of life leaving as the {monster_name}",
                        Fore.YELLOW + Style.NORMAL +"  \n",
                        Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"injured you fatally and your storied tale of heroism",
                        Fore.YELLOW + Style.NORMAL +"                  |\n",
                        Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"as a {hero_class} is over!",
                        Fore.YELLOW + Style.NORMAL +"                           \n",
                        Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
                        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
                        Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
                        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

                        # Ask the player if they want to restart or exit
                        restart_option = input(f"{Fore.CYAN + Style.NORMAL}Do you want to restart? (yes/no): ").lower()
                        if restart_option == 'yes' or restart_option == 'y':
                            greeting()
                        elif restart_option == 'no' or restart_option == 'n':
                            quit()  # Exit the loop if the player doesn't want to restart  

            elif actions == "2":
                quit_option = input(f"{Fore.CYAN + Style.NORMAL}Are you sure you want to quit the game? (y/n)")
                if quit_option == 'yes' or quit_option == 'y':
                    print(exit_message)
                    quit()  #Exit the loop if the player doesn't want to restart
                elif quit_option == 'no' or quit_option == 'n':
                    continue
            else:
                print(f"{Fore.CYAN + Style.NORMAL}Invalid option. Please choose again.")              

    elif battle == "2":
        npc1 = ["Cleric", "Fighter", "Rogue", "Sorcerer", "Wizard"]
        npc_1 = random.choice(npc1)
        enemies = ["Dire Rats", "Goblins", "Skeletons"]
        creatures = random.choice(enemies) 
        leave_game(npc_1, creatures, home_town, worlds)
        print(exit_message)
        quit()
    else:
        invalid_entry = invalid()
        print(invalid_entry)
        battle = input(f"{Fore.CYAN + Style.NORMAL}Do you...\n1) Follow orders\n2) Go AWOL(Quit the story)\n\n")

    return ""

    
def nonfaerun_hero(hero_class, home_town, worlds, exit_message, player_character, monster_name, chosen_monster_details, armor_class, hit_points, damage, to_hit, initiative):
    #random NPC selection
    npc1 = ["Cleric", "Fighter", "Rogue", "Sorcerer", "Wizard"]
    npc_1 = random.choice(npc1)
    npc2 = ["Cleric", "Fighter", "Rogue", "Sorcerer", "Wizard"]
    npc_2 = random.choice(npc2)
    npc3 = ["Cleric", "Fighter", "Rogue", "Sorcerer", "Wizard"]
    npc_3 = random.choice(npc3)
    
    armor_modifier = player_character.calculate_armor_bonus(player_character.equipment['armor'],
                                                            player_character.shield_modifier)

    #Define hero abilities
    hero_abilities = Abilities(
        Strength=player_character.abilities.Strength,
        Dexterity=player_character.abilities.Dexterity,
        Constitution=player_character.abilities.Constitution,
        Intelligence=player_character.abilities.Intelligence,
        Wisdom=player_character.abilities.Wisdom,
        Charisma=player_character.abilities.Charisma
    )

    #Create a Combat_Actions object for the hero
    hero_object = Combat_Actions(
        character=player_character,
        armor_class=armor_modifier,
        hit_points=player_character.hp,
        abilities=hero_abilities
    )

    #Create Monster object based on chosen_monster_details dictionary
    chosen_monster_object = Monster(
        name=chosen_monster_details['name'],
        armor_class=chosen_monster_details['armor_class'],
        hit_points=chosen_monster_details['hit_points'],
        to_hit=chosen_monster_details['to_hit'],
        initiative=chosen_monster_details['initiative'],
        damage=chosen_monster_details['damage']
    )

    #get terminal size
    columns, _ = shutil.get_terminal_size() 

    if columns < 80:
        # Adjusted ASCII art for smaller screens
        closing_parenthesis = ")"
        zero = "(O"
        offset = 2
        terminal_width = shutil.get_terminal_size().columns
        formatted_text = f"{Fore.YELLOW + Style.NORMAL + closing_parenthesis.ljust(1)}{zero.rjust(terminal_width - offset)}"

        begin_nonfaerun_hero = print(
            f"\n{Fore.YELLOW + Style.NORMAL}{'~' * columns}",
            f"{formatted_text}",
            f"{Fore.YELLOW + Style.NORMAL}{'~' * columns}",
            f"{Fore.WHITE + Style.BRIGHT}{textwrap.fill(f'Hero of {worlds} you have joined the ranks and have been used for your {hero_class} skill set. This day you are preparing for battle on a city in {worlds} that is one of good people. The thought of waging war on this symbol of truth and justice is just incomprehensible. Then suddenly you see buildings that were untouched become burnt to the ground, and within minutes the area is covered in bloody pulsating cocoons. The city was once displaying their flags, but then suddenly were displaying flayed humans, elves, tieflings, and more on poles instead. Fine crafted roads instantly turned into a lava flow erupting from hell itself. Over the course of the day demonic figures are seen flaying, and digesting the locals in primal mannerisms', width=columns)}\n",
            f"\n{Fore.YELLOW + Style.NORMAL}{'~' * columns}",
            f"{formatted_text}\n",
            f"{Fore.YELLOW + Style.NORMAL}{'~' * columns}\n",
            "\n"
        )

        input(f"{Fore.CYAN + Style.NORMAL}Press Enter")

        print("")
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(formatted_text)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(Fore.WHITE + Style.BRIGHT + 
              textwrap.fill(f"{hero_class} of {worlds} you have been tasked to police the army camp. The resistance is trying to fight back against Orcus's occupation of {home_town}. Your unit today is a {npc_1}, a {npc_2}, and a {npc_3}. Trying to sneak attack a sleeping regimen, you see a group of eight {monster_name}s. Your group quickly engages the enemy!", width=columns))
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(formatted_text)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print("")

        input(f"{Fore.CYAN + Style.NORMAL}Press Enter")

    if columns >= 80:
        #print statement
        begin_nonfaerun_hero = print(Fore.YELLOW + Style.NORMAL + "         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
                                    Fore.YELLOW + Style.NORMAL + "       =O)                                                                            (O=\n",
                                    Fore.YELLOW + Style.NORMAL + "        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
                                    Fore.YELLOW + Style.NORMAL + "         |                                                                             |\n",
                                    Fore.YELLOW + Style.NORMAL + "         |     ", Fore.WHITE + Style.BRIGHT + f"Hero of {worlds} you have joined the ranks and have been used for \n",
                                    Fore.YELLOW + Style.NORMAL + "         | ", Fore.WHITE + Style.BRIGHT + f"your {hero_class} skill set. This day you are preparing for battle on a city",
                                    Fore.YELLOW + Style.NORMAL + "                      \n",
                                    Fore.YELLOW + Style.NORMAL + "         | ", Fore.WHITE + Style.BRIGHT + f"in {worlds} that is one of good people. The thought of waging war on this",
                                    Fore.YELLOW + Style.NORMAL + "         \n",
                                    Fore.YELLOW + Style.NORMAL + "         | ", Fore.WHITE + Style.BRIGHT + "symbol of truth and justice is just incomprehensible. Then suddenly you",
                                    Fore.YELLOW + Style.NORMAL + "   |\n",
                                    Fore.YELLOW + Style.NORMAL + "         | ", Fore.WHITE + Style.BRIGHT + "see buildings that were untouched become burnt to the ground, and within",
                                    Fore.YELLOW + Style.NORMAL + "  |\n",
                                    Fore.YELLOW + Style.NORMAL + "         | ", Fore.WHITE + Style.BRIGHT + "minutes the area is covered in bloody pulsating cocoons. The city was",
                                    Fore.YELLOW + Style.NORMAL + "     |\n",
                                    Fore.YELLOW + Style.NORMAL + "         | ", Fore.WHITE + Style.BRIGHT + "once displaying their flags, but then suddenly were displaying flayed",
                                    Fore.YELLOW + Style.NORMAL + "     |\n",
                                    Fore.YELLOW + Style.NORMAL + "         | ", Fore.WHITE + Style.BRIGHT + "humans, elves, tieflings, and more on poles instead. Fine crafted roads",
                                    Fore.YELLOW + Style.NORMAL + "   |\n",
                                    Fore.YELLOW + Style.NORMAL + "         | ", Fore.WHITE + Style.BRIGHT + "instantly turned into a lava flow erupting from hell itself. Over the",
                                    Fore.YELLOW + Style.NORMAL + "     |\n",
                                    Fore.YELLOW + Style.NORMAL + "         | ", Fore.WHITE + Style.BRIGHT + "course of the day demonic figures are seen flaying, and digesting",
                                    Fore.YELLOW + Style.NORMAL + "         |\n",
                                    Fore.YELLOW + Style.NORMAL + "         | ", Fore.WHITE + Style.BRIGHT + "the locals in primal mannerisms.",
                                    Fore.YELLOW + Style.NORMAL + "                                          |\n",
                                    Fore.YELLOW + Style.NORMAL + "         |                                                                             |\n",
                                    Fore.YELLOW + Style.NORMAL + "        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
                                    Fore.YELLOW + Style.NORMAL + "       =O)                                                                            (O=\n",
                                    Fore.YELLOW + Style.NORMAL + "        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        
        input(f"{Fore.CYAN + Style.NORMAL}Press Enter") 

        #print statement
        non_faerun_battle = print(Fore.YELLOW + Style.NORMAL + "         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
                                Fore.YELLOW + Style.NORMAL + "       =O)                                                                            (O=\n",
                                Fore.YELLOW + Style.NORMAL + "        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
                                Fore.YELLOW + Style.NORMAL + "         |                                                                             |\n",
                                Fore.YELLOW + Style.NORMAL + "         |     ", Fore.WHITE + Style.BRIGHT + f"{hero_class} of {worlds} you have been tasked to police the army camp. ",
                                Fore.YELLOW + Style.NORMAL + "         \n",
                                Fore.YELLOW + Style.NORMAL + "         |     ", Fore.WHITE + Style.BRIGHT + f"The resistance is trying to fight back against Orcus's occupation of",
                                Fore.YELLOW + Style.NORMAL + "  |\n",
                                Fore.YELLOW + Style.NORMAL + "         |     ", Fore.WHITE + Style.BRIGHT + f"{home_town}. Your unit today is a {npc_1}, a {npc_2}, and a {npc_3}.",
                                Fore.YELLOW + Style.NORMAL + "         \n",
                                Fore.YELLOW + Style.NORMAL + "         |                                                                             |\n",
                                Fore.YELLOW + Style.NORMAL + "         |     ", Fore.WHITE + Style.BRIGHT + f"Trying to sneak attack a sleeping regimen, you see a group of",
                                Fore.YELLOW + Style.NORMAL + "         |\n",
                                Fore.YELLOW + Style.NORMAL + "         |     ", Fore.WHITE + Style.BRIGHT + f"eight {monster_name}s. Your group quickly engages the enemy!\n",
                                Fore.YELLOW + Style.NORMAL + "         |                                                                             |\n",
                                Fore.YELLOW + Style.NORMAL + "        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
                                Fore.YELLOW + Style.NORMAL + "       =O)                                                                            (O=\n",
                                Fore.YELLOW + Style.NORMAL + "        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        
        input(f"{Fore.CYAN + Style.NORMAL}Press Enter") 

    #print(f"Chosen monster: {monster_name}")
    #print(f"Armor Class: {armor_class}")
    #print(f"Hit Points: {hit_points}")
    #print(f"To Hit: {to_hit}")
    #print(f"Initiative: {initiative}")
    #print(f"Damage: {damage}")

    #COMBAT BEGINS HERE

    battle = input("Do you...\n1) Follow orders\n2) Go AWOL(Quit the story)\n\n")

    if battle == "1":
        print(begin_nonfaerun_hero)
        while hero_object.is_alive() and chosen_monster_object.is_alive():
            print(f"\n{Fore.GREEN + Style.BRIGHT}==== Battle ====")
            print(f"{Fore.GREEN + Style.BRIGHT}{hero_class} HP: {hero_object.hit_points}")
            print(f"{Fore.GREEN + Style.BRIGHT}{monster_name} HP: {chosen_monster_object.hit_points}")

            actions = input(f"\n{Fore.CYAN + Style.NORMAL}Do you...\n1) Attack\n2) Run away(Quit the story)\n\n").lower()

            #print(f'\nMonster: {chosen_monster_details}\n')

            if actions == "1":
                #Hero attacks
                total_damage = hero_object.attack(chosen_monster_object)

                #weapon_damage = hero_object.character.calculate_weapon_modifier(hero_object.character.equipment['weapon'])
                #print(f"Debug: Total Damage: {total_damage} (Weapon Damage: {weapon_damage}).")

                if total_damage > 0:
                    chosen_monster_object.take_damage(total_damage)
                    print(f"{Fore.BLUE + Style.BRIGHT}You dealt {total_damage} damage to {monster_name}!")
                else:
                    print(f"{Fore.MAGENTA + Style.BRIGHT}You missed the attack on {monster_name}!")

                #Creature attacks
                if chosen_monster_object.is_alive():
                    monster_damage = chosen_monster_object.attack(hero_object)

                    #print(f"Debug: Monster Damage: {monster_damage}")

                    if monster_damage > 0:
                        hero_object.take_damage(monster_damage)
                        print(f"{Fore.MAGENTA + Style.BRIGHT}{monster_name} dealt {monster_damage} damage to the {hero_class}!")
                    else:
                        print(f"{Fore.BLUE + Style.BRIGHT}{monster_name} missed the attack on {hero_class}!")

                #Print the result of the battle
                if hero_object.is_alive() and not chosen_monster_object.is_alive():
                    #print statement
                    print(f"{Fore.BLUE + Style.BRIGHT}{hero_class} won the battle!")
                    print("")

                    if columns < 80:
                        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
                        print(formatted_text)
                        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
                        print(Fore.WHITE + Style.BRIGHT + 
                            textwrap.fill(f"Your {hero_class} abilities are amazing! Your group is fascinated by the display of your skills. With only one {monster_name} left. A tear in the fabrics of reality is not only in front of you, but a purplish globe with green tendrils as fingers claw an area around you. Instantly you are swallowed up and now being pulled through a wormhole of lights, stars, and worlds that are flying by you faster than what you can conceive. It seems as if it is billions of shooting stars flying by you faster than light. Then it suddenly stops and you now see a different world lying before you.", width=columns))
                        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
                        print(formatted_text)
                        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
                        print("")

                        print(f'{Fore.WHITE + Style.BRIGHT}Link to "Spellplague Portal" video: {Fore.BLUE + Style.BRIGHT}\033[4mhttps://drive.google.com/file/d/1XV-WYUpx0wID5LsXzIHPNw7i7-cqRZ0j/view?usp=drive_link\033[0m')

                        input(f"\n{Fore.CYAN + Style.NORMAL}Press Enter") 
                
                        see_city = baldurs_gate()
                        print(see_city)

                        congratulations = win_game(worlds, home_town)
                        print(congratulations) 


                    elif columns >= 80:
                        #print statemtnt
                        print(Fore.YELLOW + Style.NORMAL +"         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
                        Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
                        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
                        Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
                        Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"Your {hero_class} abilities are amazing! Your group is fascinated by ",
                        Fore.YELLOW + Style.NORMAL +"         \n",
                        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +f"the display of your skills. With only one {monster_name} left. A tear",Fore.YELLOW + Style.NORMAL +"     \n",
                        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"in the fabrics of reality is not only in front of you, but a purplish",
                        Fore.YELLOW + Style.NORMAL +"     |\n",
                        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"globe with green tendrils as fingers claw an area around you. Instantly",
                        Fore.YELLOW + Style.NORMAL +"   \n", 
                        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"you are swallowed up and now being pulled through a wormhole of lights,",Fore.YELLOW + Style.NORMAL +"   |\n",
                        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"stars, and worlds that are flying by you faster than what you can",
                        Fore.YELLOW + Style.NORMAL +"         |\n",
                        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"conceive. It seems as if it is billions of shooting stars flying by",
                        Fore.YELLOW + Style.NORMAL +"       |\n", 
                        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"you faster than light. Then it suddenly stops and you now see a",
                        Fore.YELLOW + Style.NORMAL +"           |\n",
                        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"different world lying before you.",
                        Fore.YELLOW + Style.NORMAL +"                                         |\n",     
                        Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
                        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
                        Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
                        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

                        print(f'{Fore.WHITE + Style.BRIGHT}Link to "Spellplague Portal" video: {Fore.BLUE + Style.BRIGHT}\033[4mhttps://drive.google.com/file/d/1XV-WYUpx0wID5LsXzIHPNw7i7-cqRZ0j/view?usp=drive_link\033[0m')

                        input(f"\n{Fore.CYAN + Style.NORMAL}Press Enter") 
                
                        see_city = baldurs_gate()
                        print(see_city)

                        congratulations = win_game(worlds, home_town)
                        print(congratulations)                  

                    elif not hero_object.is_alive() and chosen_monster_object.is_alive():
                        #print statement
                        print(f"{Fore.MAGENTA + Style.BRIGHT}{monster_name} defeated {hero_class}. Game over.") 

                        if columns < 80:
                            print("")
                            print(Fore.YELLOW + Style.NORMAL + "~" * columns)
                            print(formatted_text)
                            print(Fore.YELLOW + Style.NORMAL + "~" * columns)
                            print(Fore.WHITE + Style.BRIGHT +
                            textwrap.fill(f"You now feel the rush of life leaving as the {monster_name} injured you fatally and your storied tale of heroism as a {hero_class} is over", width=columns))
                            print(Fore.YELLOW + Style.NORMAL + "~" * columns)
                            print(formatted_text)
                            print(Fore.YELLOW + Style.NORMAL + "~" * columns)
                            print("")
                            # Ask the player if they want to restart or exit
                            restart_option = input(f"{Fore.CYAN + Style.NORMAL}Do you want to restart? (yes/no): ").lower()
                            if restart_option == 'yes' or restart_option == 'y':
                                greeting()
                            elif restart_option == 'no' or restart_option == 'n':
                                quit()  # Exit the loop if the player doesn't want to restart  

                        elif columns >= 80: 
                            print(Fore.YELLOW + Style.NORMAL +"         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
                            Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
                            Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
                            Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
                            Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"You now feel the rush of life leaving as the {monster_name}",
                            Fore.YELLOW + Style.NORMAL +"  \n",
                            Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"injured you fatally and your storied tale of heroism",
                            Fore.YELLOW + Style.NORMAL +"                  |\n",
                            Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"as a {hero_class} is over!",
                            Fore.YELLOW + Style.NORMAL +"                           \n",
                            Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
                            Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
                            Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
                            Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

                            # Ask the player if they want to restart or exit
                            restart_option = input(f"{Fore.CYAN + Style.NORMAL}Do you want to restart? (yes/no): ").lower()
                            if restart_option == 'yes' or restart_option == 'y':
                                greeting()
                            elif restart_option == 'no' or restart_option == 'n':
                                quit()  # Exit the loop if the player doesn't want to restart   

            elif actions == "2":
                quit_option = input(f"{Fore.CYAN + Style.NORMAL}Are you sure you want to quit the game? (y/n)")
                if quit_option == 'yes' or quit_option == 'y':
                    print(exit_message)
                    quit()  #Exit the loop if the player doesn't want to restart
                elif quit_option == 'no' or quit_option == 'n':
                    continue
            else:
                print(f"{Fore.CYAN + Style.NORMAL}Invalid option. Please choose again.")                

    elif battle == "2":
        npc1 = ["Cleric", "Fighter", "Rogue", "Sorcerer", "Wizard"]
        npc_1 = random.choice(npc1)
        enemies = ["Dire Rats", "Goblins", "Skeletons"]
        creatures = random.choice(enemies) 
        leave_game(npc_1, creatures, home_town, worlds)
        print(exit_message)
        quit()
    else:
        invalid_entry = invalid()
        print(invalid_entry)
        battle = input("Do you...\n1) Follow orders\n2) Go AWOL(Quit the story)\n\n")

    return ""

def baldurs_gate():
    #get terminal size
    columns, _ = shutil.get_terminal_size() 

    # Check if screen size is smaller than a threshold
    if columns < 80:
        #Adjusted ASCII art for smaller screens
        closing_parenthesis = ")"
        zero = "(O"
        offset = 1
        terminal_width = shutil.get_terminal_size().columns
        formatted_text = f"{Fore.YELLOW + Style.NORMAL + closing_parenthesis.ljust(1)}{zero.rjust(terminal_width - offset)}"

        print("")
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(formatted_text)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(Fore.WHITE + Style.BRIGHT +
        textwrap.fill(f"In the distance is what appears to be the end of the continent. A majestic city more beautiful than anything you have yet to see in your early adventuring career. You approach Baldur's Gate and The city is alive. It is just before midday and the weather is perfect. A breeze is blowing in from the sea and there are scattered clouds that keep the sun from being too hot. Streamers and balloons for the circus, the marketplace, crafts, parades, magic, games, theater all line the streets of Baldur's Gate.", width=columns))
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(formatted_text)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print("")
        print(f'{Fore.WHITE + Style.BRIGHT}Link to "Baldur\'s Gate" image: {Fore.BLUE + Style.BRIGHT}\033[4mhttps://drive.google.com/file/d/1bxXd8CvLRBb7hs8NCwT2mK-6J8Ro_Vad/view?usp=drive_link\033[0m')
        print("")
        print(f'{Fore.WHITE + Style.BRIGHT}Link to "Marketplace" video: {Fore.BLUE + Style.BRIGHT}\033[4mhttps://drive.google.com/file/d/1tYdVlhKRlLEWwWQyStcH0c8fgeDn-rji/view?usp=drive_link\033[0m')
        print("")
        print(f'{Fore.WHITE + Style.BRIGHT}Link to "Circus" video: {Fore.BLUE + Style.BRIGHT}\033[4mhttps://drive.google.com/file/d/1j_WlZ04YNxkKOdjEKFAANpARBTDx2v88/view?usp=drive_link\033[0m')
        print("")
        print(f'{Fore.WHITE + Style.BRIGHT}Link to "Parade" video: {Fore.BLUE + Style.BRIGHT}\033[4mhttps://drive.google.com/file/d/1HXi6s55r8oeBqQ1T7PHrLq8gV5yU-C_x/view?usp=drive_link\033[0m')

        input(f"\n{Fore.CYAN + Style.NORMAL}Press Enter")

        print("")
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(formatted_text)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(Fore.WHITE + Style.BRIGHT +
        textwrap.fill(f"Approaching the city you notice some flyers with an announcement! A famous wizard named Elminster Aumar from Faerun has issued a challenge for any who want to accept...\"Faerun faces new, rising dooms now that I cannot face alone. Our homelands stand in worse peril now than ever before. Old evils stir, or return unlooked-for, looming like storm clouds over the darkened hills. Strife and change tear asunder nations and cities. Who can see who shall rise over all? Even the monks of far Candlekeep who guard well the words of the prophet Alaundo who is never wrong, cannot know. It might just be ye, if your swords and spells are ready and your heart bold. Faerun needs ye, lest we fall unguarded to the dangers all around. Adventurer, I am Elminster, and I say to ye that these forgotten realms are yours to discover, reforge, and defend, yours to make anew in winning your own crown. Go forth and take up arms against the perils that beset us!", width=columns))
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(formatted_text)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print("")
        print(f'{Fore.WHITE + Style.BRIGHT}Link to "Baldur\'s Gate City" video: {Fore.BLUE + Style.BRIGHT}\033[4mhttps://drive.google.com/file/d/1OVfZ3j8dBAstR4Ti1VJmeF5G5WNGRGPh/view?usp=drive_link\033[0m')
        print("")
        print(f'{Fore.WHITE + Style.BRIGHT}Link to "Baldur\'s Gate - Lore" video: {Fore.BLUE + Style.BRIGHT}\033[4mhttps://drive.google.com/file/d/1p5cVv5bIbigQZta5fHrapF0xBCcJ9qBz/view?usp=drive_link\033[0m')
        print("")
        print(f'{Fore.WHITE + Style.BRIGHT}Link to "Candlekeep - Lore" video: {Fore.BLUE + Style.BRIGHT}\033[4mhttps://drive.google.com/file/d/1YKTDXWeVWqWVSD4k9JhcdbRw1cvsK4eA/view?usp=drive_link\033[0m\n')
        
        input(f"{Fore.CYAN + Style.NORMAL}Press Enter\n") 
        
        return ""

    elif columns >= 80:
        #print statement
        see_city = print(Fore.YELLOW + Style.NORMAL +"         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
        Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +"In the distance is what appears to be the end of the continent.",
        Fore.YELLOW + Style.NORMAL +"       |\n",
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"A majestic city more beautiful than anything you have yet to see in",Fore.YELLOW + Style.NORMAL +"       |\n",
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"your early adventuring career. You approach Baldur's Gate and The city is",
        Fore.YELLOW + Style.NORMAL +" |\n",
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"alive. It is just before midday and the weather is perfect. A breeze is",
        Fore.YELLOW + Style.NORMAL +"   |\n", 
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"blowing in from the sea and there are scattered clouds that keep the",Fore.YELLOW + Style.NORMAL +"      |\n",
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"sun from being too hot. Streamers and balloons for the circus, the",
        Fore.YELLOW + Style.NORMAL +"        |\n",
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"marketplace, crafts, parades, magic, games, theater all line",
        Fore.YELLOW + Style.NORMAL +"              |\n", 
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"the streets of Baldur's Gate.",
        Fore.YELLOW + Style.NORMAL +"                                             |\n",       
        Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        print(f'{Fore.WHITE + Style.BRIGHT}Link to "Baldur\'s Gate" image: {Fore.BLUE + Style.BRIGHT}\033[4mhttps://drive.google.com/file/d/1bxXd8CvLRBb7hs8NCwT2mK-6J8Ro_Vad/view?usp=drive_link\033[0m')
        print("")
        print(f'{Fore.WHITE + Style.BRIGHT}Link to "Marketplace" video: {Fore.BLUE + Style.BRIGHT}\033[4mhttps://drive.google.com/file/d/1tYdVlhKRlLEWwWQyStcH0c8fgeDn-rji/view?usp=drive_link\033[0m')
        print("")
        print(f'{Fore.WHITE + Style.BRIGHT}Link to "Circus" video: {Fore.BLUE + Style.BRIGHT}\033[4mhttps://drive.google.com/file/d/1j_WlZ04YNxkKOdjEKFAANpARBTDx2v88/view?usp=drive_link\033[0m')
        print("")
        print(f'{Fore.WHITE + Style.BRIGHT}Link to "Parade" video: {Fore.BLUE + Style.BRIGHT}\033[4mhttps://drive.google.com/file/d/1HXi6s55r8oeBqQ1T7PHrLq8gV5yU-C_x/view?usp=drive_link\033[0m')

        input(f"\n{Fore.CYAN + Style.NORMAL}Press Enter")

        #print statement
        elminsters_challenge = print(Fore.YELLOW + Style.NORMAL +"         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
        Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +"Approaching the city you notice some flyers with an announcement!",
        Fore.YELLOW + Style.NORMAL +"     |\n",
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"A famous wizard named Elminster Aumar from Faerun has issued a challenge",Fore.YELLOW + Style.NORMAL +"  |\n",
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"for any who want to accept...\"Faerun faces new, rising dooms now that I",
        Fore.YELLOW + Style.NORMAL +"   |\n",
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"cannot face alone. Our homelands stand in worse peril now than ever",
        Fore.YELLOW + Style.NORMAL +"       |\n", 
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"before. Old evils stir, or return unlooked-for, looming like storm clouds",Fore.YELLOW + Style.NORMAL +" |\n",
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"over the darkened hills. Strife and change tear asunder nations and",
        Fore.YELLOW + Style.NORMAL +"       |\n",
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"cities. Who can see who shall rise over all? Even the monks of far",
        Fore.YELLOW + Style.NORMAL +"        |\n", 
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"Candlekeep who guard well the words of the prophet Alaundo who is",
        Fore.YELLOW + Style.NORMAL +"         |\n", 
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"never wrong, cannot know. It might just be ye, if your swords and",
        Fore.YELLOW + Style.NORMAL +"         |\n",
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"spells are ready and your heart bold. Faerun needs ye, lest we fall",
        Fore.YELLOW + Style.NORMAL +"       |\n",
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"unguarded to the dangers all around. Adventurer, I am Elminster,and I say",
        Fore.YELLOW + Style.NORMAL +" |\n",
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"to ye that these forgotten realms are yours to discover, reforge,",
        Fore.YELLOW + Style.NORMAL +"         |\n",
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"and defend, yours to make anew in winning your own crown. Go forth and",
        Fore.YELLOW + Style.NORMAL +"    |\n",
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"take up arms against the perils that beset us!\"",
        Fore.YELLOW + Style.NORMAL +"                           |\n",
        Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        print(f'{Fore.WHITE + Style.BRIGHT}Link to "Baldur\'s Gate City" video: {Fore.BLUE + Style.BRIGHT}\033[4mhttps://drive.google.com/file/d/1OVfZ3j8dBAstR4Ti1VJmeF5G5WNGRGPh/view?usp=drive_link\033[0m')
        print("")
        print(f'{Fore.WHITE + Style.BRIGHT}Link to "Baldur\'s Gate - Lore" video: {Fore.BLUE + Style.BRIGHT}\033[4mhttps://drive.google.com/file/d/1p5cVv5bIbigQZta5fHrapF0xBCcJ9qBz/view?usp=drive_link\033[0m')
        print("")
        print(f'{Fore.WHITE + Style.BRIGHT}Link to "Candlekeep - Lore" video: {Fore.BLUE + Style.BRIGHT}\033[4mhttps://drive.google.com/file/d/1YKTDXWeVWqWVSD4k9JhcdbRw1cvsK4eA/view?usp=drive_link\033[0m\n')

        input(f"{Fore.CYAN + Style.NORMAL}Press Enter\n") 
        
        return ""
    
def leave_game(npc_1, creatures, home_town, worlds):
    npc1 = ["Cleric", "Fighter", "Rogue", "Sorcerer", "Wizard"]
    npc_1 = random.choice(npc1)
    enemies = ["Dire Rats", "Goblins", "Skeletons"]
    creatures = random.choice(enemies) 

    #get terminal size
    columns, _ = shutil.get_terminal_size() 

    # Check if screen size is smaller than a threshold
    if columns < 80:
        #Adjusted ASCII art for smaller screens
        closing_parenthesis = ")"
        zero = "(O"
        offset = 1
        terminal_width = shutil.get_terminal_size().columns
        formatted_text = f"{Fore.YELLOW + Style.NORMAL + closing_parenthesis.ljust(1)}{zero.rjust(terminal_width - offset)}"

        print("")
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(formatted_text)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(Fore.WHITE + Style.BRIGHT +
        textwrap.fill(f"You decide that the matters of the world do not interest you and plan to stay home. You will never meet a {npc_1} from {home_town} in {worlds} to fight and slay {creatures}!", width=columns))
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(formatted_text)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print("")

        return ""

    elif columns >= 80:
        #print statement
        exit_message = print(Fore.YELLOW + Style.NORMAL +"\n         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
        Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +"You decide that the matters of the world do not interest you and",
        Fore.YELLOW + Style.NORMAL +"      |\n",
        Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"plan to stay home. You will never meet a {npc_1} from {home_town} ",
        Fore.YELLOW + Style.NORMAL +"             \n",
        Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"in {worlds} to fight and slay {creatures}!",
        Fore.YELLOW + Style.NORMAL +"             \n",
        Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        return ""

def invalid():
    #get terminal size
    columns, _ = shutil.get_terminal_size() 

    # Check if screen size is smaller than a threshold
    if columns < 80:
        #Adjusted ASCII art for smaller screens
        closing_parenthesis = ")"
        zero = "(O"
        offset = 1
        terminal_width = shutil.get_terminal_size().columns
        formatted_text = f"{Fore.YELLOW + Style.NORMAL + closing_parenthesis.ljust(1)}{zero.rjust(terminal_width - offset)}"

        print("")
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(formatted_text)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(Fore.WHITE + Style.BRIGHT +
        textwrap.fill(f"You are chosing a path beyond the scope of this campaign!", width=columns))
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(formatted_text)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print("")
        input(f"{Fore.CYAN + Style.NORMAL}Press Enter\n\n")
    
        return ""
    
    elif columns >= 80:
        #print statement
        invalid_entry = print(Fore.YELLOW + Style.NORMAL +"\n         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
        Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"You are chosing a path beyond the scope of this campaign!",
        Fore.YELLOW + Style.NORMAL +"             |\n",
        Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        input(f"{Fore.CYAN + Style.NORMAL}Press Enter\n\n")

        return ""

def win_game(worlds, home_town):
    #get terminal size
    columns, _ = shutil.get_terminal_size() 

    # Check if screen size is smaller than a threshold
    if columns < 80:
        #Adjusted ASCII art for smaller screens
        closing_parenthesis = ")"
        zero = "(O"
        offset = 1
        terminal_width = shutil.get_terminal_size().columns
        formatted_text = f"{Fore.YELLOW + Style.NORMAL + closing_parenthesis.ljust(1)}{zero.rjust(terminal_width - offset)}"

        print("")
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(formatted_text)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(Fore.WHITE + Style.BRIGHT +
        textwrap.fill(f"You now feel the rush of excitement as you can decide to be a famous adventurer from {home_town} in {worlds} and fight to slay Faerun's Evil! Or whatever dangers lie ahead of you.", width=columns))
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print(formatted_text)
        print(Fore.YELLOW + Style.NORMAL + "~" * columns)
        print("")
        you_win = input(f"{Fore.CYAN + Style.NORMAL}Do you accept Elminster's challenge?   (yes/no)\n\n").lower()
        #if player restarts the adventure will reprompt from the beginning game prompt
        if you_win != "yes" and you_win != "y":
            npc1 = ["Cleric", "Fighter", "Rogue", "Sorcerer", "Wizard"]
            npc_1 = random.choice(npc1)
            enemies = ["Dire Rats", "Goblins", "Skeletons"]
            creatures = random.choice(enemies) 
            print("")
            print(Fore.YELLOW + Style.NORMAL + "~" * columns)
            print(formatted_text)
            print(Fore.YELLOW + Style.NORMAL + "~" * columns)
            print(Fore.WHITE + Style.BRIGHT +
            textwrap.fill(f"You decide that the matters of the world do not interest you and don't enter the city. You leave your {npc_1} friend from {home_town} in {worlds} and hope not to fight and slay any more {creatures}!", width=columns))
            print(Fore.YELLOW + Style.NORMAL + "~" * columns)
            print(formatted_text)
            print(Fore.YELLOW + Style.NORMAL + "~" * columns)
            print("")
                # Ask the player if they want to restart or exit
            restart_option = input(f"{Fore.CYAN + Style.NORMAL}Do you want to restart? (yes/no): ").lower()
            if restart_option == 'yes' or restart_option == 'y':
                greeting()
            elif restart_option == 'no' or restart_option == 'n':
                quit()  # Exit the loop if the player doesn't want to restart
        else:
            print(Fore.MAGENTA + Style.BRIGHT +"\nCongratulations! You have begun Alaundo's Prophecy campaign.",Fore.WHITE + Style.BRIGHT,"\nTake a screen shot and show your Dungeon Master.\nShe or he will give you:\n",
            Fore.YELLOW + Style.BRIGHT +"50 gold\n",
            Fore.CYAN + Style.BRIGHT +"500 experience\n\n"),
            input("Pressing enter will begin a new story")

        return ""

    elif columns >= 80:
        #print statement
        congratulations = print(Fore.YELLOW + Style.NORMAL +"         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
            Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
            Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
            Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
            Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +"You now feel the rush of excitement as you can decide to be a famous",
            Fore.YELLOW + Style.NORMAL +"  |\n",
            Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"adventurer from {home_town} in {worlds} and fight to slay Faerun's",
            Fore.YELLOW + Style.NORMAL +"             \n",
            Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"Evil! Or whatever dangers lie ahead of you.",
            Fore.YELLOW + Style.NORMAL +"                           |\n",
            Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
            Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
            Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
            Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        
        you_win = input(f"{Fore.CYAN + Style.NORMAL}Do you accept Elminster's challenge?   (yes/no)\n\n").lower()
        #if player restarts the adventure will reprompt from the beginning game prompt
        if you_win != "yes" and you_win != "y":
            npc1 = ["Cleric", "Fighter", "Rogue", "Sorcerer", "Wizard"]
            npc_1 = random.choice(npc1)
            enemies = ["Dire Rats", "Goblins", "Skeletons"]
            creatures = random.choice(enemies) 

            #print statement
            print(Fore.YELLOW + Style.NORMAL +"         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
            Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
            Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
            Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
            Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +"You decide that the matters of the world do not interest you and",
            Fore.YELLOW + Style.NORMAL +"      |\n",
            Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"don't enter the city. You leave your {npc_1} friend from {home_town} ",
            Fore.YELLOW + Style.NORMAL +"             \n",
            Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"in {worlds} and hope not to fight and slay any more {creatures}!",
            Fore.YELLOW + Style.NORMAL +"             \n",
            Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
            Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
            Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
            Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

            # Ask the player if they want to restart or exit
            restart_option = input(f"{Fore.CYAN + Style.NORMAL}Do you want to restart? (yes/no): ").lower()
            if restart_option == 'yes' or restart_option == 'y':
                greeting()
            elif restart_option == 'no' or restart_option == 'n':
                quit()  # Exit the loop if the player doesn't want to restart
        else:
            print(Fore.MAGENTA + Style.BRIGHT +"\nCongratulations! You have begun Alaundo's Prophecy campaign.",Fore.WHITE + Style.BRIGHT,"\nTake a screen shot and show your Dungeon Master.\nShe or he will give you:\n",
            Fore.YELLOW + Style.BRIGHT +"50 gold\n",
            Fore.CYAN + Style.BRIGHT +"500 experience\n\n"),
            input("Pressing enter will begin a new story")

        return ""