class Cetverokut:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def opseg(self):
        return self.a + self.b + self.c + self.d


class Pravokutnik(Cetverokut):
    def __init__(self, a, b):
        super().__init__(a, b, a, b)

    def povrsina(self):
        return self.a * self.b


pravokutnik= Pravokutnik(3,4)
print(pravokutnik.a)
#3
print(pravokutnik.b)
#4
print(pravokutnik.povrsina())
#12
print(pravokutnik.opseg())
#14

cetverokut= Cetverokut(2,3,5,8)
print(cetverokut.opseg())
#18
print(cetverokut.povrsina())


