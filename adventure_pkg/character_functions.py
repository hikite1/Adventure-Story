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
            'bab': 'average'
        }

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
        # General equipment dictionary with default values
        general_equipment_dict = {
            'armor': None,
            'shield': None,
            'weapon': None,
            'potions': [],
            'spells': [],
            'scrolls': [],
            'bab': 'average'
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
        return 10 + self.calculate_armor_modifier(armor) + shield_bonus + dexterity_mod
    
    def calculate_init_bonus(self):
        dexterity_mod = self.abilities.calculate_modifier('Dexterity')
        return dexterity_mod

    def calculate_class_specific_modifiers(self, item_type):
        if self.char_class == "Cleric":
            # Add cleric-specific logic
            if item_type == 'armor':
                self.armor_modifier += self.calculate_armor_modifier(self.equipment['armor'])
            elif item_type == 'bab':
                self.armor_modifier += self.calculate_tohit(self.equipment['bab'])
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
            elif item_type == 'bab':
                self.armor_modifier += self.calculate_tohit(self.equipment['bab'])
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
            elif item_type == 'bab':
                self.armor_modifier += self.calculate_tohit(self.equipment['bab'])
            elif item_type == 'potions':
                self.potion_modifier += self.calculate_potion_modifier(self.equipment['potions'][0])
            elif item_type == 'weapon':
                self.weapon_modifier += self.calculate_weapon_modifier(self.equipment['weapon'])
        elif self.char_class == "Sorcerer":
            # Add sorcerer-specific logic
            if item_type == 'armor':
                self.armor_modifier += self.calculate_armor_modifier(self.equipment['armor'])
            elif item_type == 'bab':
                self.armor_modifier += self.calculate_tohit(self.equipment['bab'])
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
            elif item_type == 'bab':
                self.armor_modifier += self.calculate_tohit(self.equipment['bab'])
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
                'arcane_spells': [None],
                'divine_spells': ['Cure Light Wounds'],
                'bab': 'averaqge'
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
                'bab': 'averaqge'
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