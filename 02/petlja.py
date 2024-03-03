def while_petlja():
    # inicijaliziramo vrijednost broja koji ćemo kvadrirati
    brojač = 1
    # petlja se nastavlja sve dok je brojač manji od 11
    while brojač < 11:
        print(brojač ** 2)  # ispisujemo kvadrat broja
        brojač += 1  # uvećavamo brojač za 1


def beskonacna_petlja():
    brojač = 1
    # beskonačna petlja jer će uvjet uvijek biti zadovoljen
    while brojač <= 10:
        print(brojač ** 2)


def for_petlja_1():
    lista = list(range(4))
    print(lista)
    # [0, 1, 2, 3]


def for_petlja_2():
    for x in range(11):  # zaglavlje naredbe for
        print(x ** 2, end=" ")  # tijelo naredbe for
        # 0 1 4 9 16 25 36 49 64 81 100


def for_petlja_3():
    for x in range(1, 11, 2):
        print(x ** 2, end=" ")
        # 1 9 25 49 81


def for_petlja_4():
    for x in range(10, 0, -1):
        print(x ** 2, end=" ")
        # 100 81 64 49 36 25 16 9 4 1


def ugniježdena_petlja():
    for redak in range(1, 11):
        ispisRetka = str()
        for stupac in range(1, 11):
            umnožak = redak * stupac
            ispisRetka += str.format(" {0:>3}", umnožak)
        print(ispisRetka)


def break_naredba():
    for i in range(1, 20, 2):
        if i % 5 == 0:
            break
        print(i, end=" ")


# 1 3


def continue_naredba():
    for broj in range(0, 11):
        if broj % 2 == 0:
            continue
        if broj % 5 == 0:
            break
        print(broj, end=" ")
# 1 3


if __name__ == '__main__':
    # while_petlja()
    # beskonacna_petlja()
    # for_petlja_1()
    # for_petlja_2()
    # for_petlja_3()
    # for_petlja_4()
    # ugniježdena_petlja()
    # break_naredba()
    continue_naredba()
