import random

class Abilities:
    def __init__(self, Strength=0, Dexterity=0, Constitution=0, Intelligence=0, Wisdom=0, Charisma=0):
        self.Strength = Strength
        self.Dexterity = Dexterity
        self.Constitution = Constitution
        self.Intelligence = Intelligence
        self.Wisdom = Wisdom
        self.Charisma = Charisma

    @classmethod
    def generate_random(cls, priority):
        rolls = [[random.randint(1, 6) for _ in range(4)] for _ in range(6)]
        rolls = [sum(sorted(roll)[1:]) for roll in rolls]
        rolls.sort(reverse=True)

        abilities_dict = {}
        for ability, value in zip(priority, rolls):
            abilities_dict[ability] = int(value)  # Convert value to integer

        return cls(**abilities_dict)

    def calculate_modifier(self, ability_name):
        ability_score = getattr(self, ability_name.capitalize(), None)
        if ability_score is not None:
            # Convert ability_score to integer
            ability_score = int(ability_score)
            modifier = (ability_score - 10) // 2
            return max(-5, modifier)  # Ensure the modifier doesn't go below -5
        return None  # Return None for unknown attributes
    
    def apply_racial_modifiers(self, racial_modifiers):
        for ability, modifier in racial_modifiers.items():
            setattr(self, ability, getattr(self, ability, 0) + modifier)

    @property
    def ConstitutionModifier(self):
        return self.calculate_modifier(self.Constitution)

    def __str__(self):
        return f"Abilities: Str={self.Strength}, Dex={self.Dexterity}, Con={self.Constitution}, " \
               f"Int={self.Intelligence}, Wis={self.Wisdom}, Cha={self.Charisma}"

class Character:
    def __init__(self, char_class, character_abilities, racial_traits):
        self.char_class = char_class
        self.character_abilities = character_abilities
        self.racial_traits = racial_traits
        self.priority = self.get_priority()
        self.chosen_race = None  # Initialize chosen_race attribute
        self.abilities = Abilities.generate_random(self.priority)
        self.apply_racial_modifiers()
        self.level = 1
        self.hp = self.calculate_max_hp()
        # Initialize equipment attribute
        self.equipment = {
            'armor': None,
            'shield': None,
            'weapon': None,
            'potions': [],
            'spells': [],
            'scrolls': [],
        }

        # Initialize modifiers for armor, weapon, and potion
        self.armor_modifier = 0
        self.weapon_modifier = 0
        self.potion_modifier = 0
        self.arcane_spell_modifier = 0
        self.shield_modifier = 0
        self.divine_spell_modifier = 0

        # Equip items based on character class
        self.equip_items()

    def equip_items(self):
        # General equipment dictionary with default values
        general_equipment_dict = {
            'armor': None,
            'shield': None,
            'weapon': None,
            'potions': [],
            'spells': [],
            'scrolls': [],
        }

        # Get equipment for the character's class
        class_equipment = self.get_class_equipment()

        # Set default equipment
        self.equipment = general_equipment_dict

        for item_type, item in class_equipment.items():
            self.equipment[item_type] = item  # Use square bracket notation to set the value
            # Calculate class-specific modifiers
            self.calculate_class_specific_modifiers(item_type)


    def calculate_armor_modifier(self, armor):
        if armor == 'Chainmail':
            return 5
        elif armor == 'Chain Shirt':
            return 4
        elif armor == 'Robe':
            return 0
        # Add similar logic for other armor types
        else:
            return 0
        
    def calculate_shield_modifier(self, shield_bonus):        
        if shield_bonus == 'Wooden Shield':
            return 1

        
    def calculate_weapon_modifier(self, weapon):
        base_damage = 0
        strength_mod = self.abilities.calculate_modifier('Strength')
        
        if weapon == 'Longsword':
            base_damage = random.randint(1, 8)
        elif weapon == 'Light Mace':
            base_damage = random.randint(1, 6)
        elif weapon == 'Sling':
            base_damage = random.randint(1, 4)
        elif weapon == 'Throwing Dagger':
            base_damage = random.randint(1, 4)
        # Add similar logic for other weapon types

        total_damage = base_damage + strength_mod

        # Print statement to check the calculated damage
        print(f"Weapon: {weapon}, Base Damage: {base_damage}, Strength Modifier: {strength_mod}, Total Damage: {total_damage}")

        return max(1, total_damage)  # Ensure the damage is not negative
        
    def calculate_heal_modifier(self, cure):
        if cure == 'Cure Light Wounds':
            return random.randint(1, 8) + 1
        else:
            return 0
        
    def calculate_arcane_spell_modifier(self, arcane):
        if arcane == 'Magic Missile':
            return random.randint(1, 4) + 1
        else:
            return 0
        
    def calculate_potion_modifier(self, potion):
        if potion == 'Potion - Cure Light Wounds':
            return random.randint(1, 8) + 1
        # Add similar logic for other potion types
        else:
            return 0
        
    def calculate_armor_bonus(self, armor, shield_bonus):
        dexterity_mod = self.abilities.calculate_modifier('Dexterity')
        return 10 + self.calculate_armor_modifier(armor) + shield_bonus + dexterity_mod

    def calculate_class_specific_modifiers(self, item_type):
        if self.char_class == "Cleric":
            # Add cleric-specific logic
            if item_type == 'armor':
                self.armor_modifier += self.calculate_armor_modifier(self.equipment['armor'])
            elif item_type == 'potions':
                self.potion_modifier += self.calculate_potion_modifier(self.equipment['potions'][0])
            elif item_type == 'shield':
                self.shield_modifier += self.calculate_shield_modifier(self.equipment['shield'])
            elif item_type == 'divine_spell':
                self.divine_spell_modifier += self.calculate_heal_modifier(self.equipment['divine_spells'])
            elif item_type == 'weapon':
                self.weapon_modifier += self.calculate_weapon_modifier(self.equipment['weapon'])
        elif self.char_class == "Fighter":
            # Add fighter-specific logic
            if item_type == 'armor':
                self.armor_modifier += self.calculate_armor_modifier(self.equipment['armor'])
            elif item_type == 'potions':
                self.potion_modifier += self.calculate_potion_modifier(self.equipment['potions'][0])
            elif item_type == 'shield':
                self.shield_modifier += self.calculate_shield_modifier(self.equipment['shield'])
            elif item_type == 'weapon':
                self.weapon_modifier += self.calculate_weapon_modifier(self.equipment['weapon'])
        elif self.char_class == "Rogue":
            # Add rogue-specific logic
            if item_type == 'armor':
                self.armor_modifier += self.calculate_armor_modifier(self.equipment['armor'])
            elif item_type == 'potions':
                self.potion_modifier += self.calculate_potion_modifier(self.equipment['potions'][0])
            elif item_type == 'weapon':
                self.weapon_modifier += self.calculate_weapon_modifier(self.equipment['weapon'])
        elif self.char_class == "Sorcerer":
            # Add sorcerer-specific logic
            if item_type == 'armor':
                self.armor_modifier += self.calculate_armor_modifier(self.equipment['armor'])
            elif item_type == 'potions':
                self.potion_modifier += self.calculate_potion_modifier(self.equipment['potions'][0])
            elif item_type == 'arcane_spell':
                self.arcane_spell_modifier += self.calculate_arcane_spell_modifier(self.equipment['arcane_spells'])
            elif item_type == 'weapon':
                self.weapon_modifier += self.calculate_weapon_modifier(self.equipment['weapon'])
        elif self.char_class == "Wizard":
            # Add wizard-specific logic
            if item_type == 'armor':
                self.armor_modifier += self.calculate_armor_modifier(self.equipment['armor'])
            elif item_type == 'potions':
                self.potion_modifier += self.calculate_potion_modifier(self.equipment['potions'][0])
            elif item_type == 'arcane_spell':
                self.arcane_spell_modifier += self.calculate_arcane_spell_modifier(self.equipment['arcane_spells'])
            elif item_type == 'weapon':
                self.weapon_modifier += self.calculate_weapon_modifier(self.equipment['weapon'])
            # Add similar logic for other item types
        # Add more elif blocks for other classes

    def get_class_equipment(self):
        # General equipment for all classes
        equipment_dict = {
            'Cleric': {
                'armor': 'Chain Shirt',
                'shield': 'Wooden Shield',
                'weapon': 'Light Mace',
                'potions': ['Potion - Cure Light Wounds'],
                'scrolls': [],
                'divine_spells': [],
            },
            'Fighter': {
                'armor': 'Chainmail',
                'shield': 'Wooden Shield',
                'weapon': 'Longsword',
                'potions': ['Potion - Cure Light Wounds'],
            },
            'Rogue': {
                'armor': 'Leather',
                'weapon': 'Throwing Dagger',
                'potions': ['Potion - Cure Light Wounds'],
                'scrolls': [],
            },
            'Sorcerer': {
                'armor': 'Robe',
                'weapon': 'Sling',
                'potions': ['Potion - Cure Light Wounds'],
                'scrolls': [],
                'arcane_spells': [],
            },
            'Wizard': {
                'armor': 'Robe',
                'weapon': 'Sling',
                'potions': ['Potion - Cure Light Wounds'],
                'scrolls': [],
                'arcane_spells': [],
            },
            # Add more classes and their respective equipment
        }

        # Get equipment for the character's class
        return equipment_dict.get(self.char_class, {})


    def apply_racial_modifiers(self):
        chosen_race_traits = self.racial_traits.get(self.chosen_race, [])
        racial_modifiers = {chosen_race_traits[i]: chosen_race_traits[i + 1] for i in range(0, len(chosen_race_traits), 2)}
        self.abilities.apply_racial_modifiers(racial_modifiers)

    def get_priority(self):
        priority_list = self.character_abilities.get(self.char_class, [])
        return [ability.capitalize() for ability in priority_list]

    def __str__(self):
        equipment_str = f"Armor: {self.equipment['armor']}, Weapon: {self.equipment['weapon']}, " \
                        f"Potions: {', '.join(self.equipment['potions'])}, Spells: {', '.join(self.equipment['spells'])}"
        return f"{self.char_class} - {self.abilities} - Level {self.level} - HP: {self.hp}\n{equipment_str}"
    
    def generate_ability_scores(self, priority):
        self.abilities = Abilities.generate_random(priority)
        # Recalculate HP after generating new ability scores
        self.hp = self.calculate_max_hp()

    def calculate_max_hp(self):
        # Assuming hit_die is a dictionary mapping character classes to hit dice
        hit_die = {
            "Fighter": 10,
            "Rogue": 6,
            "Sorcerer": 4,
            "Wizard": 4,
            # Add more classes and their respective hit dice
        }
        max_hit_die = hit_die.get(self.char_class, 8)
        constitution_modifier = self.abilities.calculate_modifier('Constitution')
        max_hp = max_hit_die + constitution_modifier
        return max_hp

    def level_up(self):
        # Increase level and roll a random hit points gain based on character class hit die
        self.level += 1
        hit_die = {
            "Fighter": 10,
            "Rogue": 6,
            "Sorcerer": 4,
            "Wizard": 4,
            # Add more classes and their respective hit dice
        }

        # Increase level and roll a random hit points gain based on character class hit die
        hit_die_value = hit_die.get(self.char_class, 8)

        # Retrieve the Constitution modifier
        constitution_modifier = self.abilities.calculate_modifier('Constitution')

        # Calculate hit points gain, considering positive Constitution modifiers
        if constitution_modifier > 0:
            hp_gain = max(hit_die_value, constitution_modifier)
        else:
            hp_gain = 0  # Negative or zero modifier, no additional hit points gained

        # Subtract 1 at the end if the calculated hit points gain is still negative
        self.hp += max(0, hp_gain - 1)




"""
class Dice_Rolls(Attributes):
    #define the range of values for dice
    d20 = [x + 1 for x in range(20)]
        
    def __init__(self, character=None, creatures=None, armor_class=None, hit_points=None, Strength=None, Dexterity=None, Constitution=None, Intelligence=None, Wisdom=None, Charisma=None, saving_throws=None, roll_modifiers=None, bab=None, melee_mod=None):
        super().__init__(character, creatures, armor_class, hit_points, Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma, saving_throws, roll_modifiers, bab, melee_mod)

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

    

def __repr__(self):
        return f"Character: {self.character}, HP: {self.hit_points}, AC: {self.armor_class}"

hero1= Dice_Rolls(character="", armor_class=15, hit_points=6, Strength=13, Dexterity=13, Constitution=0, Intelligence=0, Wisdom=10, Charisma=1, saving_throws={}, roll_modifiers={}, bab=0, melee_mod=1)
skeleton1 = Dice_Rolls(character="skeleton", armor_class=15, hit_points=6, Strength=13, Dexterity=13, Constitution=0, Intelligence=0, Wisdom=10, Charisma=1, saving_throws={}, roll_modifiers={}, bab=0, melee_mod=1)

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