def f(x):
    if x == 7:
        print("f(" + str(x) + ") = -10")
    elif x > 1:
        print("f(" + str(x) + ") = " + str(4*x))
    elif x < -10:
        print("f(" + str(x) + ") = " + str( pow(x+1,2) ))
    else:
        print("f(" + str(x) + ") = 0")

def main():
    x = float(input("Podaj x: "))

    f(x)

if __name__ == "__main__":
    main()