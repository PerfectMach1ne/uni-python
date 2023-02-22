import math

PI = 3.14159

def main():
    choice = input("Wybierz figure:\n1: Romb\n2: Trojkat\n3: Trapez\n4: Rownoleglobok\n")

    if choice == '1':
        e = float(input("Podaj pierwsza przekatna rombu: "))
        f = float(input("Podaj druga przekatna rombu: "))

        print("Pole rombu = " + str(e*f/2))
    elif choice == '2':
        a = float(input("Podaj podstawe trojkata: "))
        h = float(input("Podaj wysokosc trojkata: "))

        print("Pole trojkata = " + str(a*h/2))
    elif choice == '3':
        a = float(input("Podaj pierwsza podstawe trapezu: "))
        b = float(input("Podaj druga podstawe trapezu: "))
        h = float(input("Podaj wysokosc trapezu: "))

        print("Pole trapezu = " + str(h*(a+b)/2))
    elif choice == '4':
        p = float(input("Podaj pierwsza przekatna rownolegloboku: "))
        q = float(input("Podaj druga przekatna rownolegloboku: "))
        alpha = float(input("Podaj kat (w stopniach) miedzy przekatnymi: "))

        print("Pole rownolegloboku = " + str(0.5*p*q*math.sin(alpha*PI/180)))

if __name__ == "__main__":
    main()