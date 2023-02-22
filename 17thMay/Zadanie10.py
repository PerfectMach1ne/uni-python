def osoba():
    imie = str(input("Podaj imie: "))
    nazwisko = str(input("Podaj nazwisko: "))
    miejscowosc = str(input("Podaj miejscowosc: "))
    stanowisko = str(input("Podaj stanowisko: "))

    print(imie + " " + nazwisko + "; miejscowosc " + miejscowosc + "; stanowisko " + stanowisko)

def pensja(godziny):
    if godziny <= 200:
        return godziny * 20
    else:
        return 4000 + (godziny - 200) * 30

osoba()
print(str(pensja(157)))
print(str(pensja(321)))