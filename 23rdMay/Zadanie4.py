def forLoop():
    evenSum = 0
    oddSum = 0

    for i in range(L1, L2):
        if i % 2 == 0:
            evenSum += i
        else:
            oddSum += i
    return "Suma liczb parzystych: " + str(evenSum) + "\nSuma liczb nieparzystych: " + str(oddSum)

def whileLoop():
    evenSum = 0
    oddSum = 0

    i = L1
    while i <= L2:
        if i % 2 == 0:
            evenSum += i
        else:
            oddSum += i
        i += 1

    return "Suma liczb parzystych: " + str(evenSum) + "\nSuma liczb nieparzystych: " + str(oddSum)

def stringSwitch(choice):
    return {
        1: forLoop(),
        2: whileLoop()
    }.get(choice, "Niepoprawna opcja.")

def main():
    global L1, L2
    L1 = int(input("Podaj dolna granice L1: "))
    L2 = int(input("Podaj gorna granice L2: "))

    choice = int(input("Wybierz petle: \n1: for\n2: while\n"))
    print(stringSwitch(choice))

if __name__ == "__main__":
    main()