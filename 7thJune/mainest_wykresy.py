import math


class Osoba:
    def __init__(self, imie, nazwisko, wiek, waga, wzrost):
        self.imie: str = imie
        self.nazwisko: str = nazwisko
        self.wiek: int = wiek
        self.waga: float = waga
        self.wzrost: float = wzrost

    def wyswietl_info(self):
        print("Imie i nazwisko: " + self.imie + " " + self.nazwisko)
        print("Wiek: " + str(self.wiek))
        print("Waga/wzrost: " + str(self.waga) + "kg/" + str(self.wzrost) + "cm")

    def wiek_za10lat(self):
        return self.wiek + 10

    def oblicz_bmi(self):
        bmi = self.waga / math.pow(self.wzrost, 2)
        if bmi < 18.5:
            print("Niedowaga")
        elif 18.5 < bmi < 25:
            print("Prawidlowa")
        elif 25 < bmi < 30:
            print("Nadwaga")
        elif bmi > 30:
            print("Otylosc")


class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, wiek, waga, wzrost, stanowisko, placa, lata_pracy):
        Osoba.__init__(self, imie, nazwisko, wiek, waga, wzrost)
        self.stanowisko: str = stanowisko
        self.placa: float = placa
        self.lata_pracy: int = lata_pracy

    def wyswietl_info(self):
        # print("Imie i nazwisko: " + self.imie + " " + self.nazwisko)
        # print("Wiek: " + str(self.wiek))
        # print("Waga/wzrost: " + str(self.waga) + "kg/" + str(self.wzrost) + "cm")
        super(Pracownik, self).wyswietl_info()
        print("Stanowisko: " + self.stanowisko)
        print("Placa: " + str(self.placa) + "PLN")
        print("Lata pracy: " + str(self.lata_pracy) + " lat")


if __name__ == "__main__":
    per = Osoba("Jan", "Kowalski", 45, 74.7, 175.1)
    emp = Pracownik("Barbara", "Kowalska", 54, 47.5, 171.4, "Informatyk", 55555.0, 27)

    per.wyswietl_info()
    per.oblicz_bmi()
    print(str(per.wiek_za10lat()))

    emp.wyswietl_info()
    emp.oblicz_bmi()
    print(str(emp.wiek_za10lat()))

    print(isinstance(per, Pracownik))
    print(isinstance(emp, Pracownik))
