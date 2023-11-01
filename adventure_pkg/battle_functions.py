#battle_functons.py

import random
from colorama import init, Fore, Style
init(autoreset=True)
import textwrap
import shutil

from adventure_pkg.character_functions import Character
from adventure_pkg.monster_battle_functions import Monster

columns, _ = shutil.get_terminal_size()

class Combat_Actions:
    d20 = [x + 1 for x in range(20)]

    def __init__(self, character, armor_class, hit_points, abilities):
        self.character = character
        self.armor_class = armor_class
        self.total_hp = hit_points
        self.abilities = abilities

    def attack(self, target):
        print("")
        print(Fore.GREEN + Style.BRIGHT + textwrap.fill(f"Hero: {self.character.char_class}", width=columns))
        print(Fore.GREEN + Style.BRIGHT + textwrap.fill(f"{self.character.abilities}", width=columns))
        print(Fore.GREEN + Style.BRIGHT + textwrap.fill(f"HP: {self.character.total_hp}", width=columns))
        print("")

        atk_roll = random.choice(self.d20)
        weapon_damage = self.character.calculate_weapon_modifier(self.character.equipment['weapon'])
        total_tohit = atk_roll + self.character.calculate_tohit(self.character.equipment['bab'])
        damage_roll = self.character.calculate_weapon_modifier(self.character.equipment['weapon'])
        strength_modifier = self.character.calculate_modifier(self.character.abilities.Strength)
        total_damage = max(1, damage_roll) + strength_modifier  # Ensure total_damage is at least 1 plus strength modifier


        print(textwrap.fill(f"{Fore.YELLOW + Style.BRIGHT}{self.character.char_class} attacks using a {self.character.equipment['weapon']} and rolls a {atk_roll} for a total of {total_tohit} to hit", width=columns))

        # Check if the target is a Character or Combat_Actions instance
        if isinstance(target, Combat_Actions):
            armor_class = target.character.calculate_armor_bonus(target.character.equipment['armor'], target.character.equipment['shield'])
        elif isinstance(target, Character):
            armor_class = target.calculate_armor_bonus(target.equipment['armor'], target.equipment['shield'])
        elif isinstance(target, Monster):
            armor_class = target.armor_class
        else:
            print("Invalid target type. Expected a Character, Combat_Actions, or Monster object.")
            return 0  # Return 0 to indicate a miss

        if total_tohit >= armor_class: 
            print(f"{Fore.BLUE + Style.NORMAL}You hit {target.name} and roll weapon damage of {damage_roll}, for a total of {total_damage} damage")

            if weapon_damage > 0:
                damage_roll = max(1, min(damage_roll, 6))
                strength_modifier = self.character.calculate_modifier(self.character.abilities.Strength)

                if atk_roll == 20:
                    print(Fore.GREEN + Style.BRIGHT + textwrap.fill(f"Wow! You Critically Hit the {target.name} for {total_damage * 2}!", width=columns))
                    return total_damage * 2

            return total_damage

        else:
            print(textwrap.fill(f"{Fore.MAGENTA + Style.BRIGHT}You missed the attack on the {target.name}!", width=columns))
            if atk_roll == 1:
                print(Fore.GREEN + Style.BRIGHT + textwrap.fill(f"A baby {target.name} is more threatening than that!!!!", width=columns))
            return 0  # Return 0 to indicate a miss

    def damage(self, target_details):
        melee_mod = 0
        dmg_roll = random.randint(1, 6)
        damage = dmg_roll + melee_mod
        print(textwrap.fill(f"{self.character.char_class} rolls a {dmg_roll} for a total of {damage} for damage", width=columns))
        print(textwrap.fill(f"You dealt {damage} damage to {target_details['name']}!", width=columns))

        if isinstance(target_details, Monster):
            melee_mod = target_details.damage
        elif isinstance(target_details, dict) and 'damage' in target_details:
            melee_mod = target_details['damage']

        if dmg_roll == 6:
            print("You hit for maximum damage!")
        elif dmg_roll == 1:
            print("My Yorkie hits harder than that!")

        return damage
    
    def take_damage(self, damage):
        self.total_hp -= damage
        if self.total_hp <= 0:
            print(f"{Fore.MAGENTA + Style.BRIGHT}{self.character.char_class} has been defeated!")
        return self.damage

    def is_alive(self):
        return self.total_hp > 0