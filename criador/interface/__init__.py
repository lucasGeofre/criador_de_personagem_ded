# Interface

def lin(tam=42):
    # print 42 lines
    return '-' * tam


def title(txt):
    # create a title
    print(lin())
    print(txt.center(42))
    print(lin())


def leiaint(msg):
    # read an input integer number and returns the number
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('digite um numero inteiro!')
            continue
        except KeyboardInterrupt:
            print('usuario preferiu não digitar nada')
            return 0
        else:
            return n


def menu_num(lista, txt):
    # creates a menu that read your choice from a numbered list and returns the number of your choice
    title(txt)
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(lin())
    num = leiaint('Sua opção:')
    return num

def menu_choice(lista, txt):
    # creates a menu that read your choice from a numbered list and returns the chosen item
    title(txt)
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(lin())
    num = leiaint('Sua opção:')
    chose_item = lista[num - 1]
    return chose_item
