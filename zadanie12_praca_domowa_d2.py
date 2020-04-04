# Napisz funkcję find_boundaries, która przyjmie listę liczb.
# Funkcja powinna zwrócić krotkę z najmniejszą i największą liczbą w zestawie.
# Jeśli na liście będzie element, nie będący liczbą, powinien zostać zignorowany.
# W przypadku wprowadzenia pustej listy, funkcja powinna zwrócić None.

def find_boundaries(theme=[]):
    if len(theme)==0 :           #sprawdza czy ilość znaków(len) jest równa zero. Czyli jeżeli list jest pusta to print.
        print("None")
    else:
        temp = []               #tworzę pustą listę i w TO konkretne miejsce będzie wpisywany temp.append(num) !!!!
        for num in theme:
            if (isinstance(num, int)):  #sprawdza czy liczby znajdują sie w zmiennej theme
                temp.append(num)
        print(temp)
        print("Najmniejsza wartość wynosi:",min(temp),"\nNajwiększa wartośc wynosi:",max(temp))
        krotka = (min(temp), max(temp))     #stworzy krotkę z najmniejszą i największą liczbą z listy temp
        print(krotka)

find_boundaries([6, 3, 7, 8, 1, 5, 2, 11, 7])
