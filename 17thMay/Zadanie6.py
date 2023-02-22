# Projekt z Vue.js jest do 10 czerwca czy costam
def main():
    tablica = []
    for i in range(10):
        tablica.append(int(input("Podaj "+str(i+1)+"sza liczbe: ")))

    oddSum = 0
    for i in tablica:
        if i % 2 == 1:
            oddSum += i
    print("Suma elementow nieparzystych tablicy = " + str(oddSum))

    divFiveSum = 0
    for i in tablica:
        if i % 5 == 0:
            divFiveSum += i
    print("Suma elementow tablicy podzielnych przez 5 = " + str(divFiveSum))

    evenProd = 1
    for i in tablica:
        if i % 2 == 0:
            evenProd *= i
    print("Iloczyn elementow parzystych tablicy = " + str(evenProd))

    print("Kwadrat sumy liczb nieparzystych = " + str(oddSum ** 2))

if __name__ == "__main__":
    main()