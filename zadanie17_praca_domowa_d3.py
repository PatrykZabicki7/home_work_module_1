# Napisz funkcję div, która:
#
# poprosi użytkownika o podanie 2 liczb z klawiatury,
# wprowadzone dane zamieni na liczby naturalne,
# podzieli jedną liczbę przez drugą,
# wyświetli wynik.
# Dodatkowo należy zabezpieczyć się przed wszystkimi możliwymi błędami (niewłaściwe dane, dzielenie przez zero).
#
# Sprawdź w interaktywnej konsoli Pythona, jakie błędy mogą wystąpić i zabezpiecz się przed nimi.

def div():
    try:
        liczba_1 = int(input("Podaj jedną liczbę: "))
        liczba_2 = int(input("Podaj drugą liczbę: "))
        wynik = liczba_1 / liczba_2
    except ValueError:
        return "To nie jest liczba"
    except TypeError:
        return "Wprowadzony znak nie jest liczbą"
    except ZeroDivisionError:
        return "Przez zero również dzielimy."   #błąd wyskakuje tylko jak mianownik jest równy zero.
    return wynik

print(div())