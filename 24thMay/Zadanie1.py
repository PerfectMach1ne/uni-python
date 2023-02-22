a = int(input("Podaj pierwsza liczbe"))
b = int(input("Podaj druga liczbe"))
c = int(input("Podaj trzecia liczbe"))

if (a > b and a > c):
    print(str(a))
elif b > c:
    print(str(b))
else:
    print(str(c))