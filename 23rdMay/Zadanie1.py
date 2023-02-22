# AA=18:03
def main():
    base = int(input("Podaj dlugosc podstawy trojkata: "))
    height = int(input("Podaj wysokosc trojkata: "))

    print("Pole trojkata: " + str(0.5 * base * height))
    print("Obwod trojkata: " + str(3 * base))

if __name__ == "__main__":
    main()