from criador.classe import player
from criador.interface import menu
from criador.dados import *
from criador.funcoes import *

# first-step = choosing race
race_choice_num = menu(races, 'Races')
race_choice = races[race_choice_num - 1]

# second-step = choosing racial trace
s_race_choice_num = menu(sub_div(race_choice,s_races), 'Race traces')
s_race_choice = sub_div(race_choice,s_races)[s_race_choice_num - 1]

# applying info to player() object
character = player(race=race_choice, s_race=s_race_choice)
character.all_atr()
