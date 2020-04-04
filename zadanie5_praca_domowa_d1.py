# Napisz funkcję chessboard, który przyjmie parametr n jako opcjonalny. Standardowa wartość parametru ma wynosić 8.
# Funkcja ma zwrócić wielolinijkowy napis reprezentujący szachownicę złożoną ze znaków # i spacji.
# Szachownica powinna mieć wymiary n x n.


def tablica(n): # to jest funkca, która wyświetli planszę n x n.
    result = ""
    for i in range(n):
        result+="#"*n + "\n" # \n powowduje, że po każdym użyciu # n-razy, zaczyna się nowa linijka a w niej znowu # n-razy
    return result
print(tablica(2))


# to jest funkcja, która wyświetli tablicę n x n. Wiersz wypełniony #, następny wypełniony spacją
def tablica2(n):
    result = ""
    for i in range(n):
        if i % 2 == 0:
            result += "#"*n + "\n"
        else:
            result += " "*n + "\n"
    return result
print(tablica2(5))


# to jest funkcja, która wyświetli szachownicę o wymiarach n x n.
def chessboard(n):
    result = ""
    for i in range(n):
        if i % 2 == 0:
            for j in range((n//2)+1): # bez wyrazenia +1 funkcja nie działa poprawnie dla liczb nieparzystych.
                print("#", end = " ")   # Wiersze się zgadzają. Za mała ilość kolumn czyli znaków w wierszu o jedną.
        else:
            for j in range(n//2):
                print(" ", end = "#")
        print()
chessboard(3)
              # jeżeli funkcja w swoim ciele już cos drukuje(print) wtedy nie używamy return.
              # stosuję samo chessboard bo jest to funkcja, która niczego nie zwraca(brak return) bo ma w środku printy.
              # print(chessboard(6)) drukuje to co zwraca funkcja chessboard (a to jest funkcja która nie ma nić zwracać, bo ma w środku printy) więc stosuje samo chessboard


