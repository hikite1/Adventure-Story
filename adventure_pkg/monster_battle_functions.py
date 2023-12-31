#monster_battle_functions.py

import random
from colorama import init, Fore, Style
init(autoreset=True)
import textwrap
import shutil

columns, _ = shutil.get_terminal_size()

class Monster:
    d20 = [x + 1 for x in range(20)]

    def __init__(self, name, armor_class, hit_points, to_hit, initiative, damage):
        self.name = name
        self.armor_class = armor_class
        self.hit_points = hit_points
        self.to_hit = to_hit
        self.initiative = initiative
        self.damage = damage

    def attack(self, target):
        atk_roll = random.choice(self.d20)
        total_tohit = atk_roll + self.to_hit

        print(textwrap.fill(f"{Fore.YELLOW + Style.BRIGHT}{self.name} rolls a {atk_roll} for a total of {total_tohit} to hit", width=columns))

        if total_tohit >= target.armor_class:
            self.calculate_damage()
            print(textwrap.fill(f"{Fore.MAGENTA + Style.BRIGHT}{self.name} does for a total of {self.damage} damage", width=columns))
    
            if atk_roll == 20:
                print(f"{Fore.MAGENTA + Style.BRIGHT}{self.name} hits you extremely hard for {self.damage * 2} damage!")

                return self.damage *2
        else:
            print(f"{Fore.BLUE + Style.BRIGHT}{self.name} missed!")
            return 0  # Return 0 to indicate a miss
        
        return self.damage

    def calculate_damage(self):
        return self.damage
    
    def is_alive(self):
        return self.hit_points > 0
    
    def take_damage(self, amount):
        self.hit_points -= amount
        if self.hit_points <= 0:
            print(f"{Fore.BLUE + Style.BRIGHT}{self.name} has been defeated!")
