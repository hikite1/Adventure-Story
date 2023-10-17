import random

class Combat_Actions:
    d20 = [x + 1 for x in range(20)]

    def __init__(self, character=None, armor_class=None, hit_points=None, abilities=None, creatures=None):
        self.character = character
        self.armor_class = armor_class
        self.hit_points = hit_points
        self.abilities = abilities
        self.creatures = creatures

    def attack(self, target):
        print(f"Debug: self.character = {self.character}")
        atk_roll = random.choice(self.d20)
        melee_mod = self.character.calculate_tohit(self.character.equipment['bab'])
        armor_class = target.armor_class  # Use the target's armor class

        total_tohit = atk_roll + melee_mod

        print(f"{self.character.char_class} rolls a {atk_roll} for a total of {total_tohit} to hit")

        if atk_roll == 20 or total_tohit >= armor_class:
            print("You hit!")
            return True
        else:
            print("You missed!")
            return False

    def damage(self):
        dmg_roll = random.randint(1, 6)
        print(f"Type of self.character: {type(self.character)}")
        melee_mod = self.character.weapon_modifier  # Assuming weapon_modifier is the melee modifier
        damage = dmg_roll + melee_mod

        print(f"{self.character.char_class} rolls a {dmg_roll} for a total of {damage} for damage")

        if dmg_roll == 6:
            print("You hit for maximum damage!")
        elif dmg_roll == 1:
            print("My Yorkie hits harder than that!")

        return damage

    def show_enemies(self):
        print(f"\n\nThe {self.creatures} see you and attack")

        if not self.creatures:
            print("Currently there are no enemies.")
        else:
            for creature in self.creatures:
                print(creature)


    def is_alive(self):
        return self.hit_points > 0