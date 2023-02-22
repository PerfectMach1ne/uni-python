class Prostopadloscian:
    def __init__(self, a, b, H):
        self.podst_a = a
        self.podst_b = b
        self.wysokosc = H

    def objetosc(self):
        return self.podst_a * self.podst_b * self.wysokosc

    def pole_pow_calk(self):
        return 2 * (self.podst_a * self.podst_b + self.podst_a * self.wysokosc + self.podst_b * self.wysokosc)

    def dlugosc_wsz_kraw(self):
        return 4 * (self.podst_a + self.podst_b + self.wysokosc)


if __name__ == "__main__":
    a = int(input("Podaj bok a podstawy prostopadloscianu: "))
    b = int(input("Podaj bok b podstawy prostopadloscianu: "))
    H = int(input("Podaj wysokosc prostopadloscianu: "))

    polyhedra = Prostopadloscian(a, b, H)

    print("Objetosc = " + str(polyhedra.objetosc()))
    print("Pole powierzchni calkowitej = " + str(polyhedra.pole_pow_calk()))
    print("Suma dlugosci wszystkich krawedzi = " + str(polyhedra.dlugosc_wsz_kraw()))
