def izmjenljivost_liste():
    sastojci = ["jaja", "brašno", "sol", "mlijeko", "marmelada"]
    print(sastojci)
    # ['jaja', 'brašno', 'sol', 'mlijeko', 'marmelada']

    novi_sastojci = sastojci
    novi_sastojci[4] = "vanilija"
    print("novi sastojci: ", novi_sastojci)
    # novi sastojci:  ['jaja', 'brašno', 'sol', 'mlijeko', 'vanilija']
    print("sastojci: ", sastojci)
    # sastojci:  ['jaja', 'brašno', 'sol', 'mlijeko', 'vanilija']

    novi_sastojci_ispravak = sastojci[:]  # vraća kopiju cijele liste
    novi_sastojci_ispravak[4] = "čokolada"
    print("novi_sastojci_ispravak", novi_sastojci_ispravak)
    # novi_sastojci_ispravak ['jaja', 'brašno', 'sol', 'mlijeko', 'čokolada']
    print("sastojci", sastojci)
    # sastojci ['jaja', 'brašno', 'sol', 'mlijeko', 'vanilija']


def metode_liste():
    sastojci = ["jaja", "brašno", "sol", "mlijeko"]
    print(sastojci)
    # ['jaja', 'brašno', 'sol', 'mlijeko']

    sastojci.append("čokoladni sirup")  # dodavanje
    print(sastojci)
    # ['jaja', 'brašno', 'sol', 'mlijeko', 'čokoladni sirup']

    sastojci.insert(2, "pekmez")  # umetanje
    print(sastojci)
    # ['jaja', 'brašno', 'pekmez', 'sol', 'mlijeko', 'čokoladni sirup']

    index = sastojci.index("mlijeko")  # indeks vrijednosti
    print(index)
    # 4

    sastojci.remove("pekmez")  # uklanjanje
    print(sastojci)
    # ['jaja', 'brašno', 'sol', 'mlijeko', 'čokoladni sirup']

    sastojci.reverse()  # obrtanje
    print(sastojci)
    # ['čokoladni sirup', 'mlijeko', 'sol', 'brašno', 'jaja']

    zadnji_element = sastojci.pop()  # izvuci zadnji element
    print(zadnji_element)
    # jaja
    print(sastojci)
    # ['čokoladni sirup', 'mlijeko', 'sol', 'brašno']

    sastojci.pop(2)
    print(sastojci)
    # ['čokoladni sirup', 'mlijeko', 'brašno']

    count = sastojci.count("mlijeko")  # vrati broj pojavljivanja u listi
    print(count)
    # 1


if __name__ == '__main__':
    izmjenljivost_liste()
    metode_liste()
