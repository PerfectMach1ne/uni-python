
def main():
    PI = 3.14159

    condition = True
    while condition:
        radius = float(input("Podaj promien kola: "))
        if radius <= 0:
            print("Podaj wartosc dodatnia!")
        else:
            condition = False

    circum = 2 * PI * radius
    area = PI * pow(radius, 2)

    print("Obwod kola: " + str(circum))
    print("Pole kolaL: " + str(area))

if __name__ == "__main__":
    main()