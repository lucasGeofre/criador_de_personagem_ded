from criador.dados import *
from criador.interface import menu
from criador.funcoes import ability
from criador.interface import*


class player:


    def __init__(self, clss='', race='', s_clss='', s_race=''):
        self.clss = clss
        self.race = race
        self.s_clss = s_clss
        self.s_race = s_race
        self.list_prm = [{"class": self.clss},
                         {"race": self.race},
                         {"sub_clss": self.s_clss},
                         {"sub_race": self.s_race}]
    # a method to
    def choose_atr(self):
        m = []
        n = atributes
        for c in range(0, 6):
            m.append(ability())

        for i in range(0, 6):
            cabeçalho(f'These are the values of your atributes: \n{m}')

            choice = menu(n, f'where do you want to put the value: {m[5 - i]}')
            if n[choice - 1] == 'Strength':
                self.strength = m[5-i]
                m.pop(5 - i)
                n.pop(choice - 1)
            elif n[choice - 1] == 'Intelligence':
                self.intelligence = m[5-i]
                m.pop(5 - i)
                n.pop(choice - 1)
            elif n[choice - 1] == 'Constitution':
                self.constituition = m[5-i]
                m.pop(5 - i)
                n.pop(choice - 1)
            elif n[choice - 1] == 'Wisdom':
                self.wisdom = m[5-i]
                m.pop(5 - i)
                n.pop(choice - 1)
            elif n[choice - 1] == 'Dexterity':
                self.dexterity = m[5-i]
                m.pop(5 - i)
                n.pop(choice - 1)
            else:
                self.charisma = m[5 - i]
                m.pop(5 - i)
                n.pop(choice - 1)

    def list_atr(self):
        list_atr = [{'Strength': self.strength},
                         {'Intelligence': self.intelligence},
                         {'Constitution': self.constituition},
                         {'Wisdom': self.wisdom},
                         {'Dexterity': self.dexterity},
                         {'Charisma': self.charisma}]
        for c in list_atr:
            print(c)

    def list_prm(self):
        for c in self.list_prm:
            print(c)


class race:
    def __init__(self, race_name , modifier):
        self.race_name = race_name
        self. modifier =  modifier

class racial_trace(race):
    def __init__(self, race_name, rt_name, rt_modifier):

        super(racial_trace, self).__init__(race_name)
        self.rt_name = rt_name
        self.rt_modifier = rt_modifier


