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
        self.list_atr = [{"class": self.clss}, {"race": self.race}, {"sub_clss": self.s_clss},
                         {"sub_race": self.s_race}]

    def all_atr(self):
        for c in self.list_atr:
            print(c)

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
            if n[choice - 1] == 'Intelligence':
                self.intelligence = m[5-i]
                m.pop(5 - i)
                n.pop(choice - 1)
            if n[choice - 1] == 'Constitution':
                self.constituition = m[5-i]
                m.pop(5 - i)
                n.pop(choice - 1)






x = player()
x.choose_atr()
print(x.strength)
