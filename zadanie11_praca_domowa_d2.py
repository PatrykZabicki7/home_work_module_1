# Napisz funkcję format_date, która przyjmie 3 parametry:
#
# day: dzień, xxxxxx
# month: miesiąc, yyyyy
# year: rok. zzzzzz
# Funkcja powinna sprawdzić, czy data jest poprawna:
#
# miesiąc powinen być w granicach (1, 12),
# dzień nie może być większy od 30 - 31 (lub 28 w przypadku lutego, pomiń sprawdzanie lat przestępnych).
# Jeśli któryś z warunków będzie niezgodzny z kalendarzem, funkcja ma zwrócić None.
#
# Funkcja powinna zwrócić sformatowany łańcuch tekstowy w formacie "dzień miesiąc rok".


def format_date(day, month, year):
    miesiace = {1: ("Stycznia", 31),
               2: ("Lutego", 28),
               3: ("Marca", 31),
               4: ("Kwietnia", 30),
               5: ("Maja", 31),
               6: ("Czerwca", 30),
               7: ("Lipca", 31),
               8: ("Sierpnia", 31),
               9: ("Września", 30),
               10: ("Października", 31),
               11: ("Listopada", 30),
               12: ("Grudnia", 31),
    }
    if month in miesiace:
        wybrany_dzien = miesiace[month][1]
        if day<=wybrany_dzien:
            return f"{day} {miesiace[month][0]} {year}"
        else:
            return None
    else:
        return None


print(format_date(23, 7, 2017))

# inne zakończenie. Poniżej są printy. Powyżej są returny.

#             print(day, miesiace[month][0], year)
#         else:
#             print("None")
#     else:
#         print("None")
# format_date(23, 1, 2017)




# prototyp do sprawdzenia funkcjonalności
# def format_date():
#     miesiace = {1: ["Stycznia", 31],
#                2: ["Lutego", 28],
#                3: ["Marca", 31],
#                4: ["Kwietnia", 30],
#                5: ["Maja", 31],
#                6: ["Czerwca", 30],
#                7: ["Lipca", 31],
#                8: ["Sierpnia", 31],
#                9: ["Września", 30],
#                10: ["Października", 31],
#                11: ["Listopada", 30],
#                12: ["Grudnia", 31],
#     }
#     month = int(input("Wprowadź miesiąc: "))
#     day = int(input("Wprowadź dzień: "))
#     if month in miesiace:
#         print("Pierwsza pozycja to miesiąc, druga to długość miesiąca",miesiace[month])
#         print("Wybrałeś miesiąc:",month)
#         wybrany_dzien = miesiace[month][1]
#         if day<=wybrany_dzien:
#             print("Wybrałeś dzień:",day)
#         else:
#             print("Dzień: None")
#     else:
#         print("Miesiąc: None")
# format_date()

