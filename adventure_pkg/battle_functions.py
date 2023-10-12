import random

class Dice_Rolls:
    d20 = [x + 1 for x in range(20)]

    def __init__(self, character=None, creatures=None):
        self.character = character
        self.creatures = creatures

    def attack(self, advantage=False, disadvantage=False):
        atk_roll = random.choice(self.d20)
        melee_mod = self.character.calculate_tohit(self.character.equipment['bab'])
        armor_class = self.character.calculate_armor_bonus(
            self.character.equipment['armor'],  # Assuming armor is stored in the 'armor' slot
            self.character.equipment['shield']  # Assuming shield bonus is stored in the 'shield' slot
        )

        total = atk_roll + melee_mod

        if advantage:
            print(f"\n{self.character.char_class} rolls a {atk_roll} for a total of {max(total)} to hit")
        elif disadvantage:
            print(f"{self.character.char_class} rolls a {atk_roll} for a total of {min(total)} to hit")
        else:
            print(f"{self.character.char_class} rolls a {atk_roll} for a total of {total} to hit")

        if atk_roll == 20:
            print("Nat 20")
        elif total < armor_class:
            print("You missed!")
            return False
        else:
            print("You hit!")
            return True

    def damage(self):
        dmg_roll = random.randint(1, 6)
        melee_mod = self.character.weapon_modifier  # Assuming weapon_modifier is the melee modifier
        damage = dmg_roll + melee_mod

        print(f"{self.character.char_class} rolls a {dmg_roll} for a total of {damage} for damage")

        if dmg_roll == 6:
            print("You hit for maximum damage!")
        elif dmg_roll == 1:
            print("My Yorkie hits harder than that!")

    def show_enemies(self):
        print(f"\n\nThe {self.creatures} see you and attack")

        if not self.creatures:
            print("Currently there are no enemies.")
        else:
            for creature in self.creatures:
                print(creature)