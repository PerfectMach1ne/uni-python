class Samochod:
    def __init__(self, marka, model, rocznik, przebieg):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.przebieg = przebieg

    def wczytaj(self):
        self.marka = str(input("Podaj marke samochodu: "))
        self.model = str(input("Podaj model samochodu: "))
        self.rocznik = int(input("Podaj rocznik samochodu: "))
        self.przebieg = int(input("Podaj przebieg samochodu: "))

    def wypisz(self):
        print(self.marka + " " + self.model + " " + str(self.rocznik) + " " + str(self.przebieg))


if __name__ == '__main__':
    car = Samochod("Volvo", "v70", 2005, 51174)
    car.wypisz()
    car.wczytaj()
    car.wypisz()