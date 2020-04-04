# Program, który ma listę liczb. Funkcja ma zwrócić histogram ze znaków `#`
def histogram():
    lista = [2, 3, "5i", 4]# jeżeli lista zawiera same liczby, to program wypisze histogram. Jeżeli lista zawiera
    # chociaż jeden string(łańcuch) wyświetli `None`
    all_elements_are_integers = all(isinstance(x, int) for x in lista)
    print(all_elements_are_integers)
    if all_elements_are_integers is True:
        for i in lista:
            print(i*"#")
    else:
        print("None")
histogram()


# źle przeczytałem polecenie. Tablica z góry ma być podana. Ale jak na inną treść zadania
# jest dobrze. Brakuje komendy, która sprawdza czy wprowadzony znak jest liczbą czy stringiem.
# Jeżeli jest stringiem, wyświetla informację None. Przy mojej koncepcji jest to bardzo trudne i wszystko do zmiany.

# def histogram(ilosc):
#     lista = []
#     ilosc = int(input("Ile pozycji chcesz wprowadzić do listy?: "))
#     for i in range(1,(ilosc+1)):
#         cyfra = int(input("Podaj cyfrę: "))
#         lista.append(cyfra)
#     print(lista)
#     for i in lista:
#         print(i*"#")
# histogram(1)


# program zrobiony bez użycia funkcji

# lista = []
# ilosc = int(input("Ile pozycji chcesz wprowadzić do listy?: "))
#
# liczba1 = int(input("Podaj cyfrę: "))
# liczba2 = int(input("Podaj kolejną cyfrę: "))
# liczba3 = int(input("Podaj kolejną cyfrę: "))
# liczba4 = int(input("Podaj kolejną cyfrę: "))
#
# lista.append(liczba1)
# lista.append(liczba2)
# lista.append(liczba3)
# lista.append(liczba4)
#
# all_elements_are_integers = all(isinstance(x, int) for x in lista)
# print(all_elements_are_integers)
#
# print(lista)
#
# for i in lista:
#     print(i*"#")