# 18:05
n = int(input("Podaj n: "))

lista = []
for i in range(n):
    a = int(input("Podaj liczbe " + str(i) + ": "))
    lista.append(a)

for i in range(len(lista)):
    print(str(lista[i]) + " lista[" + str(i) + "]")

print('================')

for i in range(len(lista)):
    print(lista[::-1][i])

print('================')

lista.sort()

for i in range(len(lista)):
    print(str(lista[i]))

print('================')

list_remove = int(input("Podaj element do usuniecia: "))
lista.remove(list_remove)

for i in range(len(lista)):
    print(str(lista[i]))

print('================')

index_remove = int(input("POdaj indeks elementu do usuniecia: "))
lista.pop(index_remove)

for i in range(len(lista)):
    print(str(lista[i]))

print('================')

element = int(input("Podaj element: "))
element_incidence = 0
last_index = 0

try:
    current_index = lista.index(element)
    print("Indeks pierwszego wystapienia: lista[" + str(current_index) + "]")
    element_incidence = element_incidence + 1
    for el in lista:
        last_index = last_index + current_index
        if el == element:
            element_incidence = element_incidence + 1
            current_index = lista.index(el)
    if element_incidence not in {0, 1}:
        element_incidence = element_incidence - 1
    print("Liczba wystapien elementu: " + str(element_incidence))
except ValueError:
    print("Element nie wystapil w liscie")

print('================')

i = int(input("Podaj indeks i: "))
j = int(input("Podaj indeks j: "))

for el in lista[i:j+1]:
    print(el)
