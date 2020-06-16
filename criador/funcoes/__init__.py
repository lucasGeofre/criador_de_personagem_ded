from criador.dados import s_races
import random


def sub_div(n, l):
    # this function will return the lists inside the dictionary
    # n is the name of the dictionary
    # l is the list of dictionaries
    for c in range(len(l)):
        r_title = str(l[c]).split(':')[0][2:-1]
        if r_title == n:
            m = l[c][n]
    return m



def ability():
    abt = []
    for c in range(0, 4):
        value = random.randint(1, 6)
        abt.append(value)
        abt.sort(reverse=True)
        abt_value = sum(abt[0:3])
    return abt_value


