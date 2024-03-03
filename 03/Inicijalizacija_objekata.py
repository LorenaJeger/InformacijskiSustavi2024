class Pravokutnik:
    def __init__(self, duzina_stranice_a, duzina_stranice_b):
        self.duzina_stranice_a = duzina_stranice_a
        self.duzina_stranice_b = duzina_stranice_b
        self.imaBoju = False


prvi_pravokutnik = Pravokutnik(5, 9)
print(prvi_pravokutnik.duzina_stranice_b)
# 9
print(prvi_pravokutnik.duzina_stranice_a)
# 5

prvi_pravokutnik.duzina_stranice_a = 10
prvi_pravokutnik.imaBoju = True
print(prvi_pravokutnik.duzina_stranice_a)
# 10
print(prvi_pravokutnik.imaBoju)
# True


