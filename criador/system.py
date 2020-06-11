from criador.classe import player
from criador.interface import menu
from criador.dados import *
from criador.funcoes import *

race_choice_num = menu(races,'Races')
race_choice = races[race_choice_num-1]


s_race_choice_num = menu(sub_div(race_choice), 'Race traces')
s_race_choice = sub_div(race_choice)[s_race_choice_num-1]

character =player(race=race_choice, s_race=s_race_choice)
character.all_atr()