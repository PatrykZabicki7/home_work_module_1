# Napisz funkcję find_first_and_last, która przyjmie listę lub krotkę.
# Następnie zwróć krotkę, która będzie zawierać pierwszy i ostatni element parametru.

def find_first_and_last(lista):
    lista_2 = lista[0], lista[-1]
    return(lista_2)

lista = [3, 1, 8, 7]
print(find_first_and_last(lista))



# def find_first_and_last(lista):
#     return lista[0], lista.pop()    #lista.pop() wycina ostatni element z listy, więc jest to źle zrobione.
#     print(lista)
#
# lista = [3, 1, 8, 7]
# print(find_first_and_last(lista))


# #nie wiem czy powyższy return stworzy listę? Czy return tylko wyświetli w nawiasie wynik?
# # Czy sam fakt w nawiasach zaokrąglonych jest tożsame z listą?
# DOPOWIEDŹ: jest to krotka. Python sam automatycznie wyświetla w nawiasie. Czyli: jak na wojnie mam karabin,
# to jestem żołnierzem.

