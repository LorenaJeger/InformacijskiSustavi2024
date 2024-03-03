class Oblik:
    def __init__(self, boja):
        self.boja = boja


class Krug(Oblik):
    def __init__(self, boja, radius):
        super().__init__(boja)
        self.radius = radius


class Zivotinja:
    def __init__(self, ime):
        self.ime = ime

    def jede(self):
        print(f"{self.__class__.__name__} jede životinjsku hranu.")


class Pas(Zivotinja):
    def __init__(self, ime, pasmina):
        super().__init__(ime)
        self.pasmina = pasmina

    # Nadjačavanje metode jede()
    def jede(self):
        print(f"{self.__class__.__name__} {self.ime} {self.pasmina} jede posebnu hranu za pse.")


class Racun:
    def __init__(self, vlasnik, banka):
        self.vlasnik = vlasnik
        self.banka = banka


class Kartica:
    def __init__(self, broj, stanje):
        self.broj = broj
        self.stanje = stanje


# Klasa BankovniRacun koja nasljeđuje od klasa Racun i Kartica
class BankovniRacun(Racun, Kartica):
    def __init__(self, vlasnik, banka, broj, stanje):
        Racun.__init__(self, vlasnik, banka)
        Kartica.__init__(self, broj, stanje)


krug = Krug("Crvena", 5)
print(f"Boja kruga: {krug.boja}, Radius: {krug.radius}")

mačka = Zivotinja("Mačka")
mačka.jede()

pas = Pas("Rex", "Njemački ovčar")
pas.jede()

bankovni_racun = BankovniRacun("Ana Bundek", "Erste banka", "123456789", 1000)
print(
    f"Vlasnik: {bankovni_racun.vlasnik}, Banka: {bankovni_racun.banka}, Broj kartice: {bankovni_racun.broj}, Stanje: {bankovni_racun.stanje}")
