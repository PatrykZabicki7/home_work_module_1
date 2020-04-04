# Napisz funkcję o nazwie dogs_age, który przeliczy wiek psa w psich latach.
#
# funkcja powinna przyjmować wiek psa jako parametr,
# dla pierwszych dwóch lat, każdy rok życia psa jest równy 10.5 ludzkiego roku,
# powyżej dwóch lat, każdy rok życia psa, to 4 ludzkie lata,
# funkcja powinna zwrócić wiek psa.

#x = wiek psa jako parametr
def dogs_age(x):
    if x <= 2:
        y = x * 10.5
    else:
        y = 21 + (x-2)*4
    return y

wiek = float(input("Ile lat ma Twój pies?: "))
print("Twój pies ma", dogs_age(wiek),"ludzkich lat.")

# musi być liczba FLOAT bo pies może mieć np. 4,5 roku. Użytkownik może wprowadzić niepełną liczbę.