# System test

## Importing modules
from criador.classes import *
from criador.interface_ import menu
from criador.data import *
from criador.functions import *

## Choosing Race
race_choice_num = menu(races, 'Races')
race_choice = races[race_choice_num - 1]

## Choosing Sub-race
s_race_choice_num = menu(sub_div(race_choice), 'Race traces')
s_race_choice = sub_div(race_choice)[s_race_choice_num-1]

## Choosing Class
clss_choice_num = menu(classes, 'Classes')
clss_choice = classes[clss_choice_num - 1]


# Applying info to player() object
character = Player(race=race_choice, s_race=s_race_choice, clss=clss_choice)
character.choose_abl()
character.my_abl()
character.my_atr()