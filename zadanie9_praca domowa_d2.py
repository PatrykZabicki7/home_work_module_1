# Napisz funkcję make_tuple, która przyjmie cztery parametry: a, b, c i d.
# Niech parametry c i d bedą opcjonalne i ich standardowe wartości będą wynosiły odpowiednio 3 i 4.
# Zwróć krotkę czterech elementów, której kolejnymi elementami będą wartości parametrów.

def make_tuple(a, b, c=3, d=4):     #podałem z góry ile wynosi `c` i `d`
    krotka = (a, b, c, d)
    return krotka
print(make_tuple(1, 2,))

#teraz mogę podać 4 parametry ale nie muszę. Wystarczą pierwsze dwa. W pamięci
#definicji są podane parametry c i d.