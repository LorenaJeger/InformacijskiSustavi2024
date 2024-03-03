class Vozilo:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def prikazi_info(self):
        return f"{self.marka}, {self.model}"


class Automobil(Vozilo):
    def __init__(self, marka, model, broj_vrata):
        super().__init__(marka, model)
        self.broj_vrata = broj_vrata

    def prikazi_info(self):
        super().prikazi_info()
        return f"{self.marka}, {self.model}"


class ElektricniAutomobil(Automobil):
    def __init__(self, marka, model, broj_vrata, autonomija):
        super().__init__(marka, model, broj_vrata)
        self.autonomija = autonomija

    def prikazi_info(self):
        super().prikazi_info()
        return f"{self.marka}, {self.model}"


# Kreiranje instance Vozilo
vozilo = Vozilo("Traktor", "Model 1")
print(vozilo.prikazi_info())


# Kreiranje instance Automobil
automobil = Automobil("Volkswagen", "Golf", 4)
print(automobil.prikazi_info())

# Kreiranje instance ElektricnogAutomobil
elektricni_automobil = ElektricniAutomobil("Tesla", "Model 3", 4, 500)
print(elektricni_automobil.prikazi_info())


