#character_functions.py

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
    def __init__(self, char_class, character_abilities=None, racial_traits=None):
        self.char_class = char_class
        self.character_abilities = character_abilities or {}
        self.racial_traits = racial_traits or {}
        self.priority = self.get_priority()
        self.chosen_race = None  # Initialize chosen_race attribute
        self.abilities = Abilities.generate_random(self.priority)
        self.apply_racial_modifiers()
        self.level = 1
        self.hp = self.calculate_max_hp()

        # Initialize modifiers
        self.armor_modifier = 0
        self.weapon_modifier = 0
        self.potion_modifier = 0
        self.arcane_spell_modifier = 0
        self.shield_modifier = 0
        self.divine_spell_modifier = 0

        # Equip items based on character class
        self.equip_items()

    def equip_items(self):
        # Get equipment for the character's class
        class_equipment = self.get_class_equipment()

        # General equipment dictionary with default values
        self.equipment = {
            'armor': None,
            'shield': None,
            'weapon': None,
            'potions': [],
            'arcane_spells': [],
            'divine_spells': [],
            'scrolls': [],
            'bab': 0
        }

        # Handle the shield separately
        shield_item = class_equipment.get('shield')
        if isinstance(shield_item, str):
            #print(f"Item Type: shield, Item: {shield_item}, Type: {type(shield_item)}")
            shield_bonus = int(''.join(filter(str.isdigit, str(shield_item)))) if any(char.isdigit() for char in str(shield_item)) else 0
            self.equipment['shield'] = shield_item
            self.equipment['shield_bonus'] = self.calculate_shield_modifier(shield_item)

        # Set other equipment
        for item_type, item in class_equipment.items():
            if item_type != 'shield':
                self.equipment[item_type] = item

        # Print equipped items
        #for item_type, value in self.equipment.items():
            #print(f"Equipped {item_type}: {value}")

        # Calculate class-specific modifiers
        for item_type in class_equipment:
            self.calculate_class_specific_modifiers(item_type)


    def calculate_armor_modifier(self, armor):
        if armor == 'Chainmail':
            return 5
        elif armor == 'Chain Shirt':
            return 4
        elif armor == 'Leather':
            return 2
        elif armor == 'Robe':
            return 0
        # Add similar logic for other armor types
        else:
            return 0
        
    def calculate_shield_modifier(self, shield_item):        
        if shield_item == 'Wooden Shield':
            return 1
        else:
            return 0

        
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
        #print(f"Weapon: {weapon}, Base Damage: {base_damage}, Strength Modifier: {strength_mod}, Total Damage: {total_damage}")

        return max(1, total_damage)  # Ensure the damage is not negative
    
    def calculate_tohit(self, attack):
        base_tohit = 0
        strength_mod = self.abilities.calculate_modifier('Strength')
        
        if attack == 'poor':
            base_tohit = 0
        elif attack == 'average':
            base_tohit = 0
        elif attack == 'good':
            base_tohit = 1

        total_tohit = base_tohit + strength_mod

        # Print statement to check the calculated to hit total
        #print(f"Attack: {attack}, BaB: {base_tohit}, Strength Modifier: {strength_mod}, To Hit Total: {total_tohit}")

        return total_tohit 
        
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

        armor_modifier = self.calculate_armor_modifier(armor) if armor else 0
        shield_bonus = int(shield_bonus) if shield_bonus else 0  # Convert shield_bonus to an integer if it's a string

        return 10 + armor_modifier + shield_bonus + dexterity_mod
    
    def calculate_init_bonus(self):
        dexterity_mod = self.abilities.calculate_modifier('Dexterity')
        return dexterity_mod
    
    def calculate_class_specific_modifiers(self, item_type):
        class_specific_logic = {
            "Cleric": ['armor', 'tohit_modifier', 'potion', 'shield', 'divine_spell', 'weapon'],
            "Fighter": ['armor', 'tohit_modifier', 'potion', 'shield', 'weapon'],
            "Rogue": ['armor', 'tohit_modifier', 'potion', 'weapon'],
            "Sorcerer": ['armor', 'tohit_modifier', 'potion', 'arcane_spell', 'weapon'],
            "Wizard": ['armor', 'tohit_modifier', 'potion', 'arcane_spell', 'weapon']
            # Add more classes and their specific logic
        }

        if self.char_class in class_specific_logic:
            for specific_item_type in class_specific_logic[self.char_class]:
                if item_type == specific_item_type:
                    modifier_method = f"calculate_{item_type}_modifier"
                    setattr(self, f"{item_type}_modifier", getattr(self, modifier_method)(self.equipment.get(item_type, 0)))
                    break


    def get_class_equipment(self):
        # General equipment for all classes
        equipment_dict = {
            'Cleric': {
                'armor': 'Chain Shirt',
                'shield': 'Wooden Shield',
                'weapon': 'Light Mace',
                'potions': ['Potion - Cure Light Wounds'],
                'scrolls': [],
                'arcane_spells': [None],
                'divine_spells': ['Cure Light Wounds'],
                'bab': 'average'
            },
            'Fighter': {
                'armor': 'Chainmail',
                'shield': 'Wooden Shield',
                'weapon': 'Longsword',
                'potions': ['Potion - Cure Light Wounds'],
                'scrolls': [None],
                'arcane_spells': [None],
                'divine_spells': [None],
                'bab': 'good'
            },
            'Rogue': {
                'armor': 'Leather',
                'shield': None,
                'weapon': 'Throwing Dagger',
                'potions': ['Potion - Cure Light Wounds'],
                'scrolls': [],
                'arcane_spells': [None],
                'divine_spells': [None],
                'bab': 'average'
            },
            'Sorcerer': {
                'armor': 'Robe',
                'weapon': 'Sling',
                'potions': ['Potion - Cure Light Wounds'],
                'scrolls': [],
                'arcane_spells': ['Magic Missile'],
                'divine_spells': [None],
                'bab': 'poor'
            },
            'Wizard': {
                'armor': 'Robe',
                'weapon': 'Sling',
                'potions': ['Potion - Cure Light Wounds'],
                'scrolls': [],
                'arcane_spells': ['Magic Missile'],
                'divine_spells': [None],
                'bab': 'poor'
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
        armor = self.equipment['armor'] if self.equipment['armor'] else 'None'
        weapon = self.equipment['weapon'] if self.equipment['weapon'] else 'None'
        
        potions = ', '.join(filter(None, self.equipment['potions']))
        arcane_spells = ', '.join(filter(None, self.equipment['arcane_spells']))
        divine_spells = ', '.join(filter(None, self.equipment['divine_spells']))

        equipment_str = f"Armor: {armor}, Weapon: {weapon}, Potions: {potions}, Arcane Spells: {arcane_spells}, Divine Spells: {divine_spells}"
        return f"{self.char_class} - {self.abilities} - Level {self.level} - HP: {self.hp}\n{equipment_str}"

    
    def generate_ability_scores(self, priority):
        self.abilities = Abilities.generate_random(priority)
        # Recalculate HP after generating new ability scores
        self.hp = self.calculate_max_hp()

    def calculate_max_hp(self):
        hit_die = {
            "Fighter": 10,  # represents a d10
            "Rogue": 6,
            "Sorcerer": 4,
            "Wizard": 4,
            "Cleric": 8,
            # Add more classes and their respective hit dice
        }
        max_hit_die = hit_die.get(self.char_class, 8)
        constitution_modifier = self.abilities.calculate_modifier('Constitution')

        #Ensure the minimum value of the modifier is 0
        constitution_modifier = max(0, constitution_modifier)

        max_hp = max_hit_die + constitution_modifier
        return max_hp

    def level_up(self):
        # Increase level and roll a random hit points gain based on character class hit die
        self.level += 1
        hit_die = {
            "Fighter": 10, #represents a d10
            "Rogue": 6,
            "Sorcerer": 4,
            "Wizard": 4,
            "Cleric": 8,
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