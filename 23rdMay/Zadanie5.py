def forLoop():
    for i in range(1, 101):
        if i % 9 == 0:
            print(str(i) + " jest podzielna przez 9.")

def whileLoop():
    i = 1
    while i <= 100:
        if i % 9 == 0:
            print(str(i) + " jest podzielna przez 9.")
        i += 1

def main():
    print("Z petli for:")
    forLoop()
    print("Z petli while:")
    whileLoop()

if __name__ == "__main__":
    main()