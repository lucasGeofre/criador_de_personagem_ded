from criador.dados import s_races


def sub_div(n):
    #n deve conter o valor procurado
    for c in range(len(s_races)):
        r_title = str(s_races[c]).split(':')[0][2:-1]
        if r_title == n:
            m = s_races[c][n]
    return m

