class Pravokutnik:
    def __init__(self, duzina_stranice_a, duzina_stranice_b):
        self._duzina_stranice_a = duzina_stranice_a
        self._duzina_stranice_b = duzina_stranice_b
        self._imaBoju = False

    def izracunaj_povrsinu(self):
        return self._duzina_stranice_a * self._duzina_stranice_b


# Primjer korištenja klase
pravokutnik = Pravokutnik(5, 8)
povrsina = pravokutnik.izracunaj_povrsinu()

print(f"Povrsina pravokutnika je: {povrsina}")
# Povrsina pravokutnika je: 40

