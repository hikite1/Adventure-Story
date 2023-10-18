#monster_battle_functions.py

import random

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

        print(f"{self.name} rolls a {atk_roll} for a total of {total_tohit} to hit")

        if total_tohit >= target.armor_class:
            return self.calculate_damage()
        else:
            print(f"{self.name} missed!")
            return 0  # Return 0 to indicate a miss

    def calculate_damage(self):
        return self.damage
    
    def is_alive(self):
        return self.hit_points > 0
    
    def take_damage(self, amount):
        self.hit_points -= amount
        if self.hit_points <= 0:
            print(f"{self.name} has been defeated!")
