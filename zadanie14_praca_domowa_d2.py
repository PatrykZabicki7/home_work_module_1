# Zadanie 14.
# Napisz funkcję check_palindrome, która pobierze jeden wyraz i sprawdzi, czy jest palindromem.
# Funkcja powinna zwracać True, jeśli łańcuch jest palindromem, False, jeśli nie jest.

def check_palindrome(slowo):
        for litery in slowo:
            if litery[::-1] == litery:
                print("True")
            else:
                print("False")

check_palindrome(["dom", "apapa"])


# # wyniki są przekazywane do listy
# def check_palindrome(slowo):
#     wynik = []
#     for litery in slowo:
#         if litery[::-1] == litery:
#             wynik.append(True)
#         else:
#             wynik.append(False)
#     return wynik
# print(check_palindrome(["dom", "apapa"]))

