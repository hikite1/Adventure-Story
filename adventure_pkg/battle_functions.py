import random

class Attributes:
    def __init__(self, character=None, creatures=None, armor_class=None, hit_points=None, strength=None, dexterity=None, constitution=None, intelligence=None, wisdom=None, charisma=None, saving_throws=None, roll_modifiers=None, bab=None, melee_mod=None):
        self.character = character
        self.creatures = creatures
        self.armor_class = armor_class
        self.hit_points = hit_points
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.saving_throws = saving_throws
        self.roll_modifiers = roll_modifiers
        self.bab = bab
        self.melee_mod = melee_mod

class Object_Characters(Attributes):
    def __init__(self, character=None, creatures=None, armor_class=None, hit_points=None, strength=None, dexterity=None, constitution=None, intelligence=None, wisdom=None, charisma=None, saving_throws=None, roll_modifiers=None, bab=None, melee_mod=None):
        super().__init__(character, creatures, armor_class, hit_points, strength, dexterity, constitution, intelligence, wisdom, charisma, saving_throws, roll_modifiers, bab, melee_mod)
        self.hero = None
        self.world = None
        self.character = None
        self.creatures = None

    def set_hero(self, hero):
        self.hero = hero

    def set_creatures(self, creatures):
        self.creatures = creatures

    def actual_object_character(self, hero, creatures):
        if hero == "Fighter" or hero == "1":
            hero = Dice_Rolls(character="Fighter", armor_class=16, hit_points=9, strength=18, dexterity=10, constitution=14, intelligence=10, wisdom=10, charisma=10)
            print(hero)
        elif hero == "Rogue" or hero == "2":
            hero = Dice_Rolls(character="Rogue", armor_class=16, hit_points=9, strength=18, dexterity=10, constitution=14, intelligence=10, wisdom=10, charisma=10)
            print(hero)
        elif hero == "Sorcerer" or hero == "3":
            hero = Dice_Rolls(character="Sorcerer", armor_class=16, hit_points=9, strength=18, dexterity=10, constitution=14, intelligence=10, wisdom=10, charisma=10)
            print(hero) 
        elif hero == "Wizard" or hero == "4":
            hero = Dice_Rolls(character="Wizard", armor_class=16, hit_points=9, strength=18, dexterity=10, constitution=14, intelligence=10, wisdom=10, charisma=10)
            print(hero) 
        if creatures == "Skeleton":
            creatures = Dice_Rolls(creatures="Skeleton", armor_class=15, hit_points=6, strength=13, dexterity=13, constitution=0, intelligence=0, wisdom=10, charisma=1, saving_throws=0, roll_modifiers=0, bab=0, melee_mod=1)
            print(creatures)
        elif creatures == "Goblin":
            creatures = Dice_Rolls(creatures="Goblin", armor_class=15, hit_points=6, strength=13, dexterity=13, constitution=0, intelligence=0, wisdom=10, charisma=1, saving_throws=0, roll_modifiers=0, bab=0, melee_mod=1)
            print(creatures)
        elif creatures == "Dire Rat":
            creatures = Dice_Rolls(creatures="Dire Rat", armor_class=15, hit_points=6, strength=13, dexterity=13, constitution=0, intelligence=0, wisdom=10, charisma=1, saving_throws=0, roll_modifiers=0, bab=0, melee_mod=1)
            print(creatures)

class Dice_Rolls(Attributes):
    #define the range of values for dice
    d20 = [x + 1 for x in range(20)]
        
    def __init__(self, character=None, creatures=None, armor_class=None, hit_points=None, strength=None, dexterity=None, constitution=None, intelligence=None, wisdom=None, charisma=None, saving_throws=None, roll_modifiers=None, bab=None, melee_mod=None):
        super().__init__(character, creatures, armor_class, hit_points, strength, dexterity, constitution, intelligence, wisdom, charisma, saving_throws, roll_modifiers, bab, melee_mod)

    def attack(self, atk_roll=1, bab=0, advantage=False, disadvantage=False, melee_mod=0, armor_class=0):
        #current total for attack roll
        total = 0
        #list of outcomes for advantage/disadvantage
        totals = []               
        #roll d20
        atk_roll = random.randint(1, 20)      
        #add ability modifiers to a roll
        attack = atk_roll + melee_mod + bab
        #update roll total
        total += attack
        #update list of totals
        totals.append(attack)
        if advantage == True:
            print(totals)
            print(f"\n{self.character} rolls a {atk_roll} for a total of {max(totals)} to hit")
        elif disadvantage == True:
            print(totals)
            print(f"{self.character} rolls a {atk_roll} for a total of {min(totals)} to hit")
        else:
            print(f"{self.character} rolls a {atk_roll} for a total of {totals} to hit")
        if atk_roll == 20:
                print("Nat 20")
            #modified 20 on a roll
        elif (attack == 20) and (melee_mod != 0):
                print("Modified 20") 
        elif atk_roll == 1:
                print("You rolled a bullet! No further actions.") 
                return  
        if total < int(armor_class):
            print("You missed!")
            return False
        else:
            print("You hit!")
            return True  

    def damage(self, dmg_roll=1, melee_mod=0):
        #current total for damage roll
        total = 0
        #list of outcomes for damage
        totals = []               
        #roll d6
        dmg_roll = random.randint(1, 6)
        damage = dmg_roll + melee_mod
        #update roll total
        total += damage
        #update list of totals
        totals.append(damage)
        print(f"{self.character} rolls a {dmg_roll} for a total of {totals} for damage")
        if dmg_roll == 6:
            print("You hit for maximum damage!")
        elif dmg_roll == 1:
            print("My Yorkie hits harder than that!")

    def show_enemies(self, creatures):
        print(f"\n\nThe {self.creatures} see you and attack")
        
        #checks to see if the variable enemies is an empty list
        if creatures == []:
            print("Currently there are no enemies.")
        else:
            #creates a creatures variable to be used with the variable enemies
            for creature in creatures:
                print(creature)

    
"""
def __repr__(self):
        return f"Character: {self.character}, HP: {self.hit_points}, AC: {self.armor_class}"

hero1= Dice_Rolls(character="", armor_class=15, hit_points=6, strength=13, dexterity=13, constitution=0, intelligence=0, wisdom=10, charisma=1, saving_throws={}, roll_modifiers={}, bab=0, melee_mod=1)
skeleton1 = Dice_Rolls(character="skeleton", armor_class=15, hit_points=6, strength=13, dexterity=13, constitution=0, intelligence=0, wisdom=10, charisma=1, saving_throws={}, roll_modifiers={}, bab=0, melee_mod=1)

skeleton1.roll_modifiers = {"str" : 1, "dex" : 1, "con" : 0, "int" : 0, "wis" : 0, "cha": -4}
print("Skeleton's Modifiers: ", skeleton1.roll_modifiers)
if skeleton1.attack(melee_mod=skeleton1.melee_mod):
    skeleton1.damage(melee_mod=skeleton1.melee_mod)
"""





"""
    cleric_hp = 12
    wizard_hp = 9
    sorcerer_hp = 12
    fighter_hp = 15
    rogue_hp = 12

    cleric_damage = 3
    wizard_damage = 5
    sorcerer_damage = 4
    monster_damage = 3
    fighter_damage = 4
    rogue_damage = 5


    name = 0
    damage = 1
    health, usage = 2, 2
    # get a random player and weapon
    weapon = weapons.get(randint(1,len(weapons)))
    weaponName = weapon[name]
    playerDamage = weapon[damage]

    # get a random creature
    creature = creatures.get(randint(8,len(creatures)))
    creatureName = creature[name]
    creatureDamage = creature[damage]
    print(f"{player[name]} has {weaponName} and will be fighting a {creatureName}")
    return creatureName"""





"""
    cleric_hp = 12
    wizard_hp = 9
    sorcerer_hp = 12
    fighter_hp = 15
    rogue_hp = 12

    cleric_damage = 3
    wizard_damage = 5
    sorcerer_damage = 4
    monster_damage = 3
    fighter_damage = 4
    rogue_damage = 5


    name = 0
    damage = 1
    health, usage = 2, 2
    # get a random player and weapon
    weapon = weapons.get(randint(1,len(weapons)))
    weaponName = weapon[name]
    playerDamage = weapon[damage]

    # get a random creature
    creature = creatures.get(randint(8,len(creatures)))
    creatureName = creature[name]
    creatureDamage = creature[damage]
    print(f"{player[name]} has {weaponName} and will be fighting a {creatureName}")
    return creatureName
"""