# Napisz aplikację Flask, która poprosi użytkownika o wpisanie liczby naturalnej n (na akcji GET "/"),
# a potem (na akcji POST "/") wyświetli tabelkę zawierającą w kolejnych wierszach:
#
# 2 do potęgi n
# n do potęgi n
# n silnia
# Liczbę wysyłaj jako parametr n.
#
# Wskazówka: Pamiętaj o wyświetleniu guzika do wysłania formularza!

from flask import Flask
from flask import request
app = Flask (__name__)

def silnia_def(n):
    wynik = 1
    if n <= 1:
        return wynik
    else:
        for i in range(1, n+1):
            wynik = wynik * i
        return wynik


@app.route("/", methods=["GET", "POST"])
def kalk():
    if request.method=="POST":
        n = int(request.form["n"])
        potega = 2**n
        potega_n = n**n
        silnia = silnia_def(n)     #f-string można już na samym początku zastosować żeby później tego nie stosować za każdym razem
        return f"""
            <html>
                <body>
                    <table border>
                        <tr>
                            <td>DZIAŁANIE</td> <td>WYNIK</td>
                        </tr>
                        <tr>
                            <td>Dwa do potęgi {n}</td> <td>{potega}</td>
                        </tr>
                        <tr>
                            <td>{n} do potęgi {n}</td> <td>{potega_n}</td>
                        </tr>
                        <tr>
                            <td>Silnia z {n}</td> <td>{silnia}</td>
                        </tr>       
                    </table>
                </body>
            </html>
            """

    if request.method == "GET":
        return"""
            <html>
                <body>
                    <form action="/" method = "POST">
                    <label>
                        Podaj liczbę naturalną: 
                        <input type="number" name="n">
                    </label>
                    <label>
                    <button type="submit">
                    Policz
                    </label>
                </body>
            </html>
            """

if __name__ == "__main__":
    app.run()

# bo cały formularz jest wysyłany taką metodą jaką tutaj wpiszesz
# 15:33
# wpisałeś POST - więc formularz zostanie wysłany metodą POST
# 15:33
# jakbyś wpisał DELETE albo GET
# 15:33
# to zostałby wysłany inną metodą :slightly_smiling_face:
# 15:34
# get wyświetla formularz
# 15:34
# ale to formularz sam ustala jaką metodą chce się wysłać
#
# Patryk Żabicki  15:34
# :smile: i lepiej będzie jak formularz zostanie wysłany POST?
#
# Michał Dobrzycki - mentor  15:35
# tak, takie są zasady wysyłania (opisane w slajdach) :slightly_smiling_face:
# 15:35
# możesz jako developer wpisać co tam chcesz
# 15:35
# tylko mamy pewne standardy i warto się ich trzymać
# 15:35
# przesyłanie danych (i tworzenie czegoś na backendzie) POWINNO być robione metodą POST
# 15:35
# co nie znaczy że nie da się inaczej
#
# Patryk Żabicki  15:36
# aaaa
# 15:36
# Dziękuję bardzo za pomoc :slightly_smiling_face: