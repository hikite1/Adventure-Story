import random
from colorama import init, Fore, Style
init(autoreset=True)
from adventure_pkg.battle_functions import Dice_Rolls

def greeting():
    greeting_message = print(Fore.YELLOW + Style.NORMAL +"         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
    Fore.YELLOW + Style.NORMAL +"         |   ",Fore.WHITE + Style.BRIGHT +"Welcome to Alaundo's Last Prophecy Heroes! An adventure for",Fore.YELLOW + Style.NORMAL+"             |\n",
    Fore.YELLOW + Style.NORMAL +"         |   ",Fore.WHITE + Style.BRIGHT +"the ages awaits you...",Fore.YELLOW + Style.NORMAL+"                                                  |\n",
    Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")  
    return greeting_message

def faerun_story():
    faerun_origin = print(Fore.YELLOW + Style.NORMAL +"         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
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
    input("Press Enter")
    return faerun_origin

def non_faerun_story():
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
    input("Press Enter")   
    return non_faerun_origin

def generate_strings(character, my_hp, my_damage, home_town):
    
    fate = print(Fore.YELLOW + Style.NORMAL +"         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
    Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"Your fate is intertwined with the {character}!",
    Fore.YELLOW + Style.NORMAL +"                            \n",
    Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"Health: {my_hp}",Fore.YELLOW + Style.NORMAL +"                                                            |\n",
    Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"Damage: {my_damage}",
    Fore.YELLOW + Style.NORMAL +"                                                             |\n", 
    Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    input("Press Enter\n\n")
    
    hometown_description = print(Fore.YELLOW + Style.NORMAL +"         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
    Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"You hale from a town called {home_town}.",
    Fore.YELLOW + Style.NORMAL +"                                  \n",
    Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +"You have spent the past few months under the mentorship",Fore.YELLOW + Style.NORMAL +"               |\n",
    Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"of a Master {character} and have been sensing",
    Fore.YELLOW + Style.NORMAL +"                              \n", 
    Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +"that it is time for you to go out into the world",
    Fore.YELLOW + Style.NORMAL +"                      |\n", 
    Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +"and test your new skills.",
    Fore.YELLOW + Style.NORMAL +"                                             |\n", 
    Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    input("Press Enter\n\n")  
    return fate, hometown_description 

def faerun_hero(character, home_town, worlds, exit_message):
    npc1 = ["Cleric", "Fighter", "Rogue", "Sorcerer", "Wizard"]
    npc_1 = random.choice(npc1)
    npc2 = ["Cleric", "Fighter", "Rogue", "Sorcerer", "Wizard"]
    npc_2 = random.choice(npc2)
    npc3 = ["Cleric", "Fighter", "Rogue", "Sorcerer", "Wizard"]
    npc_3 = random.choice(npc3)
    enemies = ["Dire Rats", "Goblins", "Skeletons"]
    creatures = random.choice(enemies) 

    begin_faerun_hero = print(Fore.YELLOW + Style.NORMAL +"         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
    Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"You decide to leave your {character} mentor in {home_town}",
    Fore.YELLOW + Style.NORMAL +"                                  \n",
    Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +"and travel to Baldur's Gate. There are plenty of",Fore.YELLOW + Style.NORMAL +"                      |\n",
    Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +"caravans headed to the event. You are able to find employment",
    Fore.YELLOW + Style.NORMAL +"         |\n", 
    Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +"easily enough and it is up to you if you think anyone",
    Fore.YELLOW + Style.NORMAL +"                 |\n", 
    Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"needs to know of your {character} abilities or not.",
    Fore.YELLOW + Style.NORMAL +"                                             \n", 
    Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    input("Press Enter")

    faerun_battle = print(Fore.YELLOW + Style.NORMAL +"         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
    Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"{character} of {worlds} you have been tasked to defend the caravan",
    Fore.YELLOW + Style.NORMAL +"         \n",
    Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"if necessary in return for room and board on the voyage to Baldur's",
    Fore.YELLOW + Style.NORMAL +"       |\n",
    Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"Gate. Each wagon has four mercenaries for it defense. Yours has you,",
    Fore.YELLOW + Style.NORMAL +"      |\n",
    Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +f"a {npc_1}, a {npc_2}, and a {npc_3}. A group of {creatures} is seen using ",
    Fore.YELLOW + Style.NORMAL +"         \n", 
    Fore.YELLOW + Style.NORMAL +"         |",Fore.WHITE + Style.BRIGHT,"the shadows from bushes clustered together ahead of your wagon. A ",
    Fore.YELLOW + Style.NORMAL +"        |\n",
    Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +f"{npc_1} sees these {creatures} and alerts the wagon to veer off and group",
    Fore.YELLOW + Style.NORMAL +"       \n",
    Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"with another wagon. Your group has discussed strategy prior and everyone",
    Fore.YELLOW + Style.NORMAL +"  |\n",
    Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"begins to move and execute the plan.",
    Fore.YELLOW + Style.NORMAL +"         \n", 
    Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    input("Press Enter")

    battle = input("Do you...\n1) Follow orders\n2) Go AWOL\n\n")           
    if battle == "1":
        actions = input(f"\nTwo of the {creatures} engage you in battle.\nDo you attack? (yes/no)\n\n").lower()
        if actions == "y" or actions == "yes": 
            object_hero = Dice_Rolls(character, armor_class=15, hit_points=6, strength=13, dexterity=13, constitution=0, intelligence=0, wisdom=10, charisma=1, saving_throws=0, roll_modifiers=0, bab=0, melee_mod=1)  
            object_creatures = Dice_Rolls(creatures, armor_class=15, hit_points=6, strength=13, dexterity=13, constitution=0, intelligence=0, wisdom=10, charisma=1, saving_throws=0, roll_modifiers=0, bab=0, melee_mod=1)         
        elif actions == "n" or actions == "no":
            runaway = input("Do you want to run away? (yes/no)").lower()
            if runaway == "n" or runaway == "no":
                actions = input(f"\nTwo of the {creatures} engage you in battle.\nDo you attack? (yes/no)").lower() 
            elif runaway == "y" or "yes":
                print(exit_message)
            else:                   
                invalid_entry = invalid()
                print(invalid_entry)
        else:
            invalid_entry = invalid()
            print(invalid_entry)
            actions = input(f"Two of the {creatures} engage you in battle.\nDo you attack? (yes/no)").lower()
        if object_hero.attack(character):
            object_hero.damage()
            input("Press Enter\n")
        if object_creatures.attack(creatures):
            object_creatures.damage()
            input("Press Enter")
    elif battle == "2":
        exit_message, npc1, npc_1, enemies, creatures = leave_game(npc_1, creatures, home_town, worlds)
        print(exit_message)
        quit()
    else:
        invalid_entry = invalid()
        print(invalid_entry)
        battle = input("Do you...\n1) Follow orders\n2) Go AWOL\n\n")  

    faerun_after_battle = print(Fore.YELLOW + Style.NORMAL +"         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
        Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"Your {character} abilities are amazing! Your group is fascinated by ",
        Fore.YELLOW + Style.NORMAL +"         \n",
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +f"the display of your skills. With only one of the {creatures} left, it runs",Fore.YELLOW + Style.NORMAL +"     \n",
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"away terrified at your decimation of its group. The rest of the journey",
        Fore.YELLOW + Style.NORMAL +"   |\n",
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"goes by rather easily. The legends of Faerun are no match for",
        Fore.YELLOW + Style.NORMAL +"             |\n", 
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"seeing these wonders first hand. Wether you are seeing the Dalelands",Fore.YELLOW + Style.NORMAL +"      |\n",
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"or the Swordcoast and the villages or iconic places of legend. You",
        Fore.YELLOW + Style.NORMAL +"        |\n",
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +f"are even more sure that leaving {home_town} was the right choice.",
        Fore.YELLOW + Style.NORMAL +"     \n", 
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"After you crest a hilltop you see your destination looms off",
        Fore.YELLOW + Style.NORMAL +"              |\n",
        Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"in the distance.",
        Fore.YELLOW + Style.NORMAL +"                                                          |\n",     
        Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
        Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
        Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    input("Press Enter")
    return begin_faerun_hero, faerun_battle, battle, faerun_after_battle
    
def nonfaerun_hero(worlds, character, home_town, exit_message):
    npc1 = ["Cleric", "Fighter", "Rogue", "Sorcerer", "Wizard"]
    npc_1 = random.choice(npc1)
    npc2 = ["Cleric", "Fighter", "Rogue", "Sorcerer", "Wizard"]
    npc_2 = random.choice(npc2)
    npc3 = ["Cleric", "Fighter", "Rogue", "Sorcerer", "Wizard"]
    npc_3 = random.choice(npc3)
    enemies = ["Dire Rats", "Goblins", "Skeletons"]
    creatures = random.choice(enemies) 

    begin_nonfaerun_hero = print(Fore.YELLOW + Style.NORMAL +"         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
    Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"Hero of {worlds} you have joined the ranks and have been used for ",
    Fore.YELLOW + Style.NORMAL +"                                  \n",
    Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +f"your {character} skill set. This day you are preparing for battle on a city",Fore.YELLOW + Style.NORMAL +"                      \n",
    Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +f"in {worlds} that is one of good people. The thought of waging war on this",
    Fore.YELLOW + Style.NORMAL +"         \n", 
    Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"symbol of truth and justice is just incomprehensible. Then suddenly you",
    Fore.YELLOW + Style.NORMAL +"   |\n", 
    Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"see buildings that were untouched become burnt to the ground, and within",
    Fore.YELLOW + Style.NORMAL +"  |\n", 
    Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"minutes the area is covered in bloody pulsating cocoons. The city was",
    Fore.YELLOW + Style.NORMAL +"     |\n", 
    Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"once displaying their flags, but then suddenly were displaying flayed",
    Fore.YELLOW + Style.NORMAL +"     |\n", 
    Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"humans, elves, tieflings, and more on poles instead. Fine crafted roads",
    Fore.YELLOW + Style.NORMAL +"   |\n", 
    Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"instantly turned into a lava flow erupting from hell itself. Over the",
    Fore.YELLOW + Style.NORMAL +"     |\n", 
    Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"course of the day demonic figures are seen flaying, and digesting",
    Fore.YELLOW + Style.NORMAL +"         |\n", 
    Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"the locals in primal mannerisms.",
    Fore.YELLOW + Style.NORMAL +"                                          |\n", 
    Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    input("Press Enter")

    non_faerun_battle = print(Fore.YELLOW + Style.NORMAL +"         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
    Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"{character} of {worlds} you have been tasked to police the army camp. ",
    Fore.YELLOW + Style.NORMAL +"         \n",
    Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"The resistance is trying to fight back against Orcus's occupation of",Fore.YELLOW + Style.NORMAL +"  |\n",
    Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"{home_town}. Your unit today is a {npc_1}, a {npc_2}, and a {npc_3}.",
    Fore.YELLOW + Style.NORMAL +"         \n",
    Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
    Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"Trying to sneak attack a sleeping regimine, you see a group of",
    Fore.YELLOW + Style.NORMAL +"        |\n", 
    Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"eight {creatures}. Your group quickly engages the enemy!                                                                        \n",
    Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    input("Press Enter")

    battle = input("Do you...\n1) Follow orders\n2) Go AWOL\n\n")           
    if battle == "1":
        actions = input(f"\nTwo of the {creatures} engage you in battle.\nDo you attack? (yes/no)\n\n").lower()
        if actions == "y" or actions == "yes": 
            object_hero = Dice_Rolls(character, armor_class=15, hit_points=6, strength=13, dexterity=13, constitution=0, intelligence=0, wisdom=10, charisma=1, saving_throws=0, roll_modifiers=0, bab=0, melee_mod=1)  
            object_creatures = Dice_Rolls(creatures, armor_class=15, hit_points=6, strength=13, dexterity=13, constitution=0, intelligence=0, wisdom=10, charisma=1, saving_throws=0, roll_modifiers=0, bab=0, melee_mod=1)         
        elif actions == "n" or actions == "no":
            runaway = input("Do you want to run away? (yes/no)").lower()
            if runaway == "n" or runaway == "no":
                actions = input(f"\nTwo of the {creatures} engage you in battle.\nDo you attack? (yes/no)").lower() 
            elif runaway == "y" or "yes":
                print(exit_message)
            else:                   
                invalid_entry = invalid()
                print(invalid_entry)
        else:
            invalid_entry = invalid()
            print(invalid_entry)
            actions = input(f"Two of the {creatures} engage you in battle.\nDo you attack? (yes/no)").lower()
        if object_hero.attack(character):
            object_hero.damage()
            input("Press Enter\n")
        if object_creatures.attack(creatures):
            object_creatures.damage()
            input("Press Enter")
    elif battle == "2":
        exit_message, npc1, npc_1, enemies, creatures = leave_game(npc_1, creatures, home_town, worlds)
        print(exit_message)
        quit()
    else:
        invalid_entry = invalid()
        print(invalid_entry)
        battle = input("Do you...\n1) Follow orders\n2) Go AWOL\n\n")

    non_faerun_afterbattle = print(Fore.YELLOW + Style.NORMAL +"         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
    Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"Your {character} abilities are amazing! Your group is fascinated by ",
    Fore.YELLOW + Style.NORMAL +"         \n",
    Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +f"the display of your skills. With only one of the {creatures} left. A tear",Fore.YELLOW + Style.NORMAL +"     \n",
    Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"in the fabrics of reality is not only in front of you, but a purplish",
    Fore.YELLOW + Style.NORMAL +"     |\n",
    Fore.YELLOW + Style.NORMAL +"         | ",Fore.WHITE + Style.BRIGHT +"globe with green tendrils as fingers claws an area around you. Instantly",
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
    input("Press Enter") 

    return begin_nonfaerun_hero, non_faerun_battle, battle, non_faerun_afterbattle

def baldurs_gate():
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
    input("Press Enter")

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
    input("Press Enter")
    return see_city, elminsters_challenge
    
def leave_game(npc_1, creatures, home_town, worlds):
    npc1 = ["Cleric", "Fighter", "Rogue", "Sorcerer", "Wizard"]
    npc_1 = random.choice(npc1)
    enemies = ["Dire Rats", "Goblins", "Skeletons"]
    creatures = random.choice(enemies) 

    exit_message = print(Fore.YELLOW + Style.NORMAL +"         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
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
    return exit_message, npc1, npc_1, enemies, creatures

def invalid():
    invalid_entry = print(Fore.YELLOW + Style.NORMAL +"         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
    Fore.YELLOW + Style.NORMAL +"         |     ",Fore.WHITE + Style.BRIGHT +f"You are chosing a path beyond the scope of this campaign!",
    Fore.YELLOW + Style.NORMAL +"             |\n",
    Fore.YELLOW + Style.NORMAL +"         |                                                                             |\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    Fore.YELLOW + Style.NORMAL +"       =O)                                                                            (O=\n",
    Fore.YELLOW + Style.NORMAL +"        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    input("Press Enter\n\n") 
    return invalid_entry



def win_game(worlds, home_town):
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

    you_win = input("Do you accept Elminster's challenge?   (yes/no)\n\n").lower()
    #if player restarts the adventure will reprompt from the beginning game prompt
    if you_win != "yes" and you_win != "y":
        quit()
    else:
        print(Fore.MAGENTA + Style.BRIGHT +"\nCongratulations! You have begun Alaundo's Prophecy campaign.",Fore.WHITE + Style.BRIGHT,"\nTake a screen shot and show your Dungeon Master.\nShe or he will give you:\n",
        Fore.YELLOW + Style.BRIGHT +"50 gold\n",
        Fore.CYAN + Style.BRIGHT +"500 experience\n\n"),
        input("Pressing enter will begin a new story")
    return congratulations, you_win