
def main():
    condition = True
    while condition:
        a = int(input("Podaj liczbe a: "))
        if a == 0:
            print("a musi byc liczba dodatnia!")
        else:
            condition = False

    b = int(input("Podaj liczbe b: "))
    c = int(input("Podaj liczbe c: "))
    d = int(input("Podaj liczbe d: "))

    W = a/a + c/(a+b) - (a+c)/(a+b+d)

    print("W = " + str(W))

if __name__ == "__main__":
    main()