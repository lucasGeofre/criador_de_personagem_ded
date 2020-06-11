from criador.dados import races
from criador.interface import menu
class player:

    def __init__(self, clss='', race='', s_clss='', s_race=''):
        self.clss =clss
        self.race = race
        self.s_clss = s_clss
        self.s_race = s_race
        self.list_atr = [{"class": self.clss}, {"race": self.race}, {"sub_clss": self.s_clss}, {"sub_race": self.s_race}]

    def all_atr(self):
        for c in self.list_atr:
            print(c)