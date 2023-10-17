from adventurestory_code import *

#worlds = ""
#enemies = ""
#self = ""
#exit = "Exit"
#play_again = ""
#enter = ""
#dice_result = ""
#battle = ""
#hero = ""
#character = ""
#my_hp = ""
#my_damage = ""
#home_town = ""
#chosen_race = ""
#racial_modifiers = ""
#bab = ""
#strength_mod = ""

def run_tests():
    # Create a test character
    test_character = Character(char_class="Cleric", character_abilities={}, racial_traits={})

    # Set equipment for testing
    test_character.equipment['armor'] = 'Chain Shirt'
    test_character.equipment['shield'] = 'Wooden Shield'

    # Print test results
    print("\nTest Results:")
    print(f"Armor Modifier: {test_character.armor_modifier}")
    print(f"Shield Modifier: {test_character.shield_modifier}")
    print(f"Weapon Modifier: {test_character.weapon_modifier}")
    print(f"Potion Modifier: {test_character.potion_modifier}")
    print(f"Arcane Spell Modifier: {test_character.arcane_spell_modifier}")
    print(f"Divine Spell Modifier: {test_character.divine_spell_modifier}")
    print(f"Max HP: {test_character.hp}")

# Run the tests
run_tests()
