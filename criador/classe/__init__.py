class player:

    def __init__(self, clss='0', race='0', hit_points='0',s_clss='0',s_race='0'):
        self.clss = clss
        self.race = race
        self.s_clss = s_clss
        self.hit_points = hit_points
        self.s_race = s_race
        self.list_atr = [{"class": self.clss}, {"race": self.race}, {"hit_points": self.hit_points}, {"sub_clss": self.s_clss}, {"sub_race": self.s_race}]

    def atr(self,atribute):

        for c in self.list_atr:
            m = str(c)
            if m.find(atribute) == 2:
                return c[atribute]

    def all_atr(self):

        for c in self.list_atr:
            print(c)




