#battle_functons.py

import random
from colorama import init, Fore, Style
init(autoreset=True)

from adventure_pkg.character_functions import Character
from adventure_pkg.monster_battle_functions import Monster


class Combat_Actions:
    d20 = [x + 1 for x in range(20)]

    def __init__(self, character, armor_class, hit_points, abilities):
        self.character = character
        self.armor_class = armor_class
        self.hit_points = hit_points
        self.abilities = abilities

    def attack(self, target):
        print(f"\n{Fore.GREEN + Style.BRIGHT}Hero: {self.character}\n")
        atk_roll = random.choice(self.d20)
        total_tohit = atk_roll + self.character.calculate_tohit(self.character.equipment['bab'])
        total_damage = self.character.calculate_weapon_modifier
        print(f"{self.character.char_class} rolls a {atk_roll} for a total of {total_tohit} to hit")

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
            damage = self.character.calculate_weapon_modifier(self.character.equipment['weapon'])
            #print(f"You hit for {damage} damage!")
            return damage
        else:
            #print("You missed!")
            return 0  # Return 0 to indicate a miss

    def damage(self, target_details):
        melee_mod = 0
        dmg_roll = random.randint(1, 6)
        damage = dmg_roll + melee_mod
        print(f"{self.character.char_class} rolls a {dmg_roll} for a total of {damage} for damage")
        print(f"You dealt {damage} damage to {target_details['name']}!")

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
        self.hit_points -= damage
        if self.hit_points <= 0:
            print(f"{Fore.MAGENTA + Style.BRIGHT}{self.character.char_class} has been defeated!")

    def is_alive(self):
        return self.hit_points > 0