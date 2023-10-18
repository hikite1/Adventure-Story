#battle_functons.py

import random

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
        print(f"Debug: self.character = {self.character}")
        atk_roll = random.choice(self.d20)

        # Check if the target is a Character or Combat_Actions instance
        if isinstance(target, Combat_Actions):
            armor_class = target.character.calculate_armor_bonus(target.character.equipment['armor'], target.character.equipment['shield'])
        elif isinstance(target, Character):
            armor_class = target.calculate_armor_bonus(target.equipment['armor'], target.equipment['shield'])
        else:
            print("Invalid target type. Expected a Character or Combat_Actions object.")
            return 0  # Return 0 to indicate a miss

        total_tohit = atk_roll + self.character.calculate_tohit(self.character.equipment['bab'])

        print(f"{self.character.char_class} rolls a {atk_roll} for a total of {total_tohit} to hit")

        if total_tohit >= armor_class:
            damage = self.character.calculate_weapon_modifier(self.character.equipment['weapon'])
            print(f"You hit for {damage} damage!")
            return damage
        else:
            print("You missed!")
            return 0  # Return 0 to indicate a miss

    def damage(self, target_details):
        dmg_roll = random.randint(1, 6)

        if isinstance(target_details, Monster):
            melee_mod = target_details.damage
        elif isinstance(target_details, dict) and 'damage' in target_details:
            melee_mod = target_details['damage']
        else:
            melee_mod = 0  # Default value if target doesn't have damage attribute

        damage = dmg_roll + melee_mod

        print(f"{self.character.char_class} rolls a {dmg_roll} for a total of {damage} for damage")

        if dmg_roll == 6:
            print("You hit for maximum damage!")
        elif dmg_roll == 1:
            print("My Yorkie hits harder than that!")

        print(f"You dealt {damage} damage to {target_details['name']}!")

        return damage
    
    def take_damage(self, damage):
        self.hit_points -= damage
        if self.hit_points <= 0:
            print(f"{self.character.char_class} has been defeated!")

    def is_alive(self):
        return self.hit_points > 0