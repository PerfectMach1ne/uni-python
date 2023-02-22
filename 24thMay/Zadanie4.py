import math

a = int(input("Podaj a: "))
b = int(input("Podaj a: "))
c = int(input("Podaj a: "))

delta = b*b - 4*a*c
if delta < 0:
    print("Rownanie nie ma rozwiazan.")
elif delta == 0:
    print("x = " + str(-b / (2*a)))
else:
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print("Rozwiazania rownania to " + str(x1) + " i " + str(x2))
