# damage_functions.py

def calculate_damage_assassin(level, damage, hp, energy, final_damage):
    base_dmg = (2 * level + damage) * (level / 9)
    hp_influence = ((hp / 20) * (energy / 40)) * 0.5
    boosted_damage = (1.2 * base_dmg) + hp_influence
    return boosted_damage * final_damage

def calculate_damage_bishop(level, damage, hp, energy, final_damage):
    base_dmg = (level + damage) * (level / 10)
    hp_influence = ((hp / 20) * (energy / 40)) * 0.2
    boosted_damage = (base_dmg * 0.6) + hp_influence
    return boosted_damage * final_damage

def calculate_damage_dark_knight(level, damage, hp, energy, final_damage):
    base_dmg = (level + damage) * (level / 10)
    hp_influence = ((hp / 2) + energy) * 0.7
    boosted_damage = base_dmg + hp_influence
    return boosted_damage * final_damage

def calculate_damage_swan(level, damage, hp, energy, final_damage):
    base_dmg = (2 * level + damage) * (level / 10)
    hp_influence = ((hp / 8) + energy) * 0.6
    boosted_damage = base_dmg + hp_influence
    return boosted_damage * final_damage

# Dictionary for function mapping
damage_calculators = {
    "1": calculate_damage_assassin,
    "2": calculate_damage_bishop,
    "3": calculate_damage_dark_knight,
    "4": calculate_damage_swan
}
