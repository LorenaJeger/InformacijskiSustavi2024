class Osoba:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime

    def prikazi_info(self):
        print(f"Ime: {self.ime}, Prezime: {self.prezime}")


class Kontakt:
    def __init__(self, email, telefon):
        self.email = email
        self.telefon = telefon

    def prikazi_kontakt(self):
        print(f"Email: {self.email}, Telefon: {self.telefon}")


class OsobaSaKontaktom(Osoba, Kontakt):
    def __init__(self, ime, prezime, email, telefon):
        # Poziv konstruktora roditeljskih klasa
        Osoba.__init__(self, ime, prezime)
        Kontakt.__init__(self, email, telefon)

    def prikazi_sve_info(self):
        self.prikazi_info()
        self.prikazi_kontakt()


# Kreiranje instance klase OsobaSaKontaktom
osoba_kontakt = OsobaSaKontaktom("Ana", "Sitar",
                                 "ana.sitar@email.com", "123-456-789")
osoba_kontakt.prikazi_sve_info()


