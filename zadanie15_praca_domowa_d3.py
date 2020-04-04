# Napisz funkcję random_average(n), która wylosuje n liczb naturalnych od 1 do 100,
# zsumuje je, po czym zwróci średnią arytmetyczną z tych liczb.
#
# Ze względu na konstrukcję testów automatycznych użyj w zadaniu poniżeszj formy importu funkcji randint:
#
# import random
# a następnie w kodzie używaj konstrukcji:
#
# random.randint()
import random

def random_average(n):
    lista = []
    i = 0
    while i < n:
        liczba = random.randint(0, 100)
        lista.append(liczba)
        i += 1
    # print(lista)
    suma = sum(lista)
    print("Suma tych liczby wynosi:",suma)

    srednia = suma/n
    print("Średnia arytmetyczna wynosi:",srednia)


random_average(3)
