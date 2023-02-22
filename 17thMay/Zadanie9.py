def objetosc(a, b, H):
    return a*b*H

def powierzchnia(a, b, H):
    return 2*a*b + 2*b*H + 2*a*H

def dlugoscKrawedzi(a, b, H):
    return 4*(a+b+H)

a = float(input("Podaj pierwsza krawedz podstawy prostopadloscianu: "))
b = float(input("Podaj druga krawedz podstawy prostopadloscianu: "))
H = float(input("Podaj wysokosc prostopadloscianu: "))

print("Objetosc = " + str(objetosc(a,b,H)))
print("Powierzchnia = " + str(powierzchnia(a,b,H)))
print("Laczna dlugosc wszystkich krawedzi = " + str(dlugoscKrawedzi(a,b,H)))