# Data for Races, Sub-races, Classes and Characteristics
# Testing push/commit

import random

## Races
races = ['dwarf', 'elf', 'halfling', 'half_elf', 'human', 'dragonborn', 'half_orc', 'tiefling', 'gnome']


## Sub-races
s_races = [{'dwarf': ['mountain dwarf', 'hill dwarf']},
           {'elf': ['dark elf', 'high elf', 'wood elf']},
           {'halfling': ['lightfoot halfling', 'stout halfling']},
           {'half_elf': ['half_elf']},
           {'human': ['human']},
           {'dragonborn': ['black', 'blue', 'brass', 'bronze', 'copper', 'gold', 'green', 'red', 'silver']},
           {'tiefling': ['tiefling']},
           {'gnome': ['rock gnome', 'forest gnome']},
           {'half_orc': ['half_orc']}]


## Classes
classes = ['Barbarian', 'Bard', 'Warlock', 'Cleric', 'Druid', 'Sorcerer', 'Fighter', 'Rogue', 'Wizard', 'Monk', 'Paladin', 'Ranger']

###Classes cheat:
# Bárbaro = Barbarian;
# Bardo = Bard;
# Bruxo = Warlock;
# Clérigo = Cleric;
# Druida = Druid;
# Feiticeiro = Sorcerer;
# Guerreiro = Fighter;
# Ladino = Rogue;
# Mago = Wizard;
# Monge = Monk;
# Paladino = Paladin;
# Patrulheiro = Ranger;


"""Characteristics"""

## Alignment

## Abilities
abilities = ['Strength', 'Intelligence', 'Constitution', 'Wisdom', 'Dexterity', 'Charisma']

## Initial Abilities Values according to Race
#_initial_ability_values = [[{'mountain dwarf':     {{'Strength': 2}, {'Intelligence': 0}, {'Constitution': 2}, {'Wisdom': 0}, {'Dexterity': 0}, {'Charisma': 0}}},
#                           {'hill dwarf':         {{'Strength': 0}, {'Intelligence': 0}, {'Constitution': 2}, {'Wisdom': 1}, {'Dexterity': 0}, {'Charisma': 0}}},
#                           {'dark elf':           {{'Strength': 0}, {'Intelligence': 0}, {'Constitution': 0}, {'Wisdom': 0}, {'Dexterity': 2}, {'Charisma': 1}}},
#                           {'high elf':           {{'Strength': 0}, {'Intelligence': 1}, {'Constitution': 0}, {'Wisdom': 0}, {'Dexterity': 2}, {'Charisma': 0}}},
#                           {'wood elf':           {{'Strength': 0}, {'Intelligence': 0}, {'Constitution': 0}, {'Wisdom': 1}, {'Dexterity': 2}, {'Charisma': 0}}},
#                           {'lightfoot halfling': {{'Strength': 0}, {'Intelligence': 0}, {'Constitution': 0}, {'Wisdom': 0}, {'Dexterity': 2}, {'Charisma': 1}}},
#                           {'stout halfling':     {{'Strength': 0}, {'Intelligence': 0}, {'Constitution': 1}, {'Wisdom': 0}, {'Dexterity': 2}, {'Charisma': 0}}},
#                           {'half_elf':           {{'Strength': 0}, {'Intelligence': 0}, {'Constitution': 0}, {'Wisdom': 0}, {'Dexterity': 0}, {'Charisma': 2}}},  # Two other abilities (of ur choice) increased by 1.
#                           {'human':              {{'Strength': 1}, {'Intelligence': 1}, {'Constitution': 1}, {'Wisdom': 1}, {'Dexterity': 1}, {'Charisma': 1}}},
#                           {'dragonborn':         {{'Strength': 2}, {'Intelligence': 0}, {'Constitution': 0}, {'Wisdom': 0}, {'Dexterity': 0}, {'Charisma': 1}}},
#                           {'tiefling':           {{'Strength': 0}, {'Intelligence': 1}, {'Constitution': 0}, {'Wisdom': 0}, {'Dexterity': 0}, {'Charisma': 2}}},
#                           {'rock gnome':         {{'Strength': 0}, {'Intelligence': 2}, {'Constitution': 1}, {'Wisdom': 0}, {'Dexterity': 0}, {'Charisma': 0}}},
#                           {'forest gnome':       {{'Strength': 0}, {'Intelligence': 2}, {'Constitution': 0}, {'Wisdom': 0}, {'Dexterity': 1}, {'Charisma': 0}}},
#                           {'half_orc':           {{'Strength': 2}, {'Intelligence': 0}, {'Constitution': 1}, {'Wisdom': 0}, {'Dexterity': 0}, {'Charisma': 0}}}]]

initial_ability_values = [  # [ s_race, Strength, Intelligence, Constitution, Wisdom, Dexterity, Charisma]
                           ['mountain dwarf',      2,0,2,0,0,0],
                           ['hill dwarf',          0,0,2,1,0,0],
                           ['dark elf',            0,0,0,0,2,1],
                           ['high elf',            0,1,0,0,2,0],
                           ['wood elf',            0,0,0,1,2,0],
                           ['lightfoot halfling',  0,0,0,0,2,1],
                           ['stout halfling',      0,0,1,0,2,0],
                           ['half_elf',            0,0,0,0,0,2],  # Two other abilities (of ur choice) increased by 1.
                           ['human',               1,1,1,1,1,1],
                           ['dragonborn',          2,0,0,0,0,1],
                           ['tiefling',            0,1,0,0,0,2],
                           ['rock gnome',          0,2,1,0,0,0],
                           ['forest gnome',        0,2,0,0,1,0],
                           ['half_orc',            2,0,1,0,0,0]]

#class_path

## Spellbook

## Dices


## Equipment
weapons = []
armors = []
