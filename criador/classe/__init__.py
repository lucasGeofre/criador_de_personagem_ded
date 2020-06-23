# Classes

from criador_de_personagem_ded.criador.dados import *
from criador_de_personagem_ded.criador.funcoes import *
from criador_de_personagem_ded.criador.interface import *


## Defining class Player

class Player:

    def __init__(self, clss='', race='', clss_path='', s_race=''):
        self.clss = clss
        self.race = race
        self.clss_path = clss_path
        self.s_race = s_race
        self.strength = 0
        self.charisma = 0
        self.intelligence = 0
        self.constituition = 0
        self.wisdom = 0
        self.dexterity = 0

        self.list_prm = [{"class": self.clss},
                         {"race": self.race},
                         {"sub_clss": self.clss_path},
                         {"sub_race": self.s_race}]

        self.list_abl = [{'Strength': self.strength},
                         {'Intelligence': self.intelligence},
                         {'Constitution': self.constituition},
                         {'Wisdom': self.wisdom},
                         {'Dexterity': self.dexterity},
                         {'Charisma': self.charisma}]

    ### Print Attributes
    def my_atr(self):
        print("\n", "-" * 42)
        print("Your attributes:\n")
        for c in range(len(self.list_prm)):
            p1 = str(self.list_prm[c]).split(':')[0][2:-1]
            p2 = str(self.list_prm[c]).split(':')[1][2:-2]
            if p2 != '':
                print(p1, ":", p2)

    ### Print Abilities
    def my_abl(self):
        print("\n", "-" * 42)
        print(" Your Abilities: \n")
        for c in range(len(self.list_abl)):
            p1 = str(self.list_abl[c]).split(':')[0][2:-1]
            p2 = str(self.list_abl[c]).split(':')[1][1:-1]
            print(p1, ":", p2)

    # Choose Abilities values with dies method
    def choose_abl(self):

        # Pull initial ability values from the selected race
        if self.race != 'dragonborn':
            list = initial_abl_list(self.s_race)[0]
        else:
            list = initial_abl_list(self.race)[0]

        # Create lists of ability values and the name of abilities
        values = []
        abl = abilities
        for c in range(0, 6):
            values.append(random_ability_values())

        # Selecting each value for abilities
        for i in range(0, 6):
            title(f'These are the values for your abilities: \n{values}')

            choice = menu_num(abl, f'where do you want to put the value: {values[5 - i]}')
            if abl[choice - 1] == 'Strength':
                self.strength += values[5 - i] + list[0]
                values.pop(5 - i)
                abl.pop(choice - 1)
            elif abl[choice - 1] == 'Intelligence':
                self.intelligence += values[5 - i] + list[1]
                values.pop(5 - i)
                abl.pop(choice - 1)
            elif abl[choice - 1] == 'Constitution':
                self.constituition += values[5 - i] + list[2]
                values.pop(5 - i)
                abl.pop(choice - 1)
            elif abl[choice - 1] == 'Wisdom':
                self.wisdom += values[5 - i] + list[3]
                values.pop(5 - i)
                abl.pop(choice - 1)
            elif abl[choice - 1] == 'Dexterity':
                self.dexterity += values[5 - i] + list[4]
                values.pop(5 - i)
                abl.pop(choice - 1)
            else:
                self.charisma += values[5 - i] + list[5]
                values.pop(5 - i)
                abl.pop(choice - 1)

        # Update list of abilities
        self.list_abl = [{'Strength': self.strength},
                         {'Intelligence': self.intelligence},
                         {'Constitution': self.constituition},
                         {'Wisdom': self.wisdom},
                         {'Dexterity': self.dexterity},
                         {'Charisma': self.charisma}]

    def choose_race(self):

        ## Choosing Race
        self.race = menu_choice(races, 'Races')

        ## Choosing Sub-race
        self.s_race = menu_choice(s_races.get(self.race), 'Race traces')

        ## Updating list of attributes
        self.list_prm = [{"class": self.clss},
                         {"race": self.race},
                         {"sub_clss": self.clss_path},
                         {"sub_race": self.s_race}]

    def choose_class(self):

        ## Choosing Class
        clss_choice_num = menu_num(classes, 'Classes')
        self.clss = classes[clss_choice_num - 1]

        ## Updating list of attributes
        self.list_prm = [{"class": self.clss},
                         {"race": self.race},
                         {"sub_clss": self.clss_path},
                         {"sub_race": self.s_race}]

    ### Print character sheet

    def my_sheet(self):  # todo finish this function
        pass


class Race:
    def __init__(self, race_name, modifier):
        self.race_name = race_name
        self.modifier = modifier


class RacialTrace(Race):
    def __init__(self, race_name, rt_name, rt_modifier):
        super(RacialTrace, self).__init__(race_name)
        self.rt_name = rt_name
        self.rt_modifier = rt_modifier
