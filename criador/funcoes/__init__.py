# Functions

from criador_de_personagem_ded.criador.dados import initial_ability_values, s_races
import random


## Random select of ability values for the player to choose

def random_ability_values():
    abl_list = []
    abl_value = 0
    for c in range(0, 4):
        value = random.randint(1, 6)
        abl_list.append(value)
        abl_list.sort(reverse=True)
        abl_value = sum(abl_list[0:3])
        if abl_value < 8:
            abl_value = 8
    return abl_value


## Get the list of ability values for each race

def initial_abl_list(name):
    list = []
    for c in range(len(initial_ability_values)):
        if name == initial_ability_values[c][0]:
            list.append(initial_ability_values[c][1:7])
    return list


## Select the menu item for you

def random_choice():
    pass

