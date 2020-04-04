# Napisz aplikację Flaska, która poprosi użytkownika o wpisanie kodu pocztowego (na akcji GET "/"),
# a potem (na akcji POST "/") wyświetli informację:
#
# Kod poprawny, jeżeli kod jest w poprawnym polskim formacie (00-001).
# Kod niepoprawny, w przeciwnym wypadku
# Kod wysyłaj jako parametr code.
#
# Wskazówka: możesz rozbić podany ciąg znaków po myślniku i sprawdzić czy obie części spełniają warunki.
# Wskazówka: Pamiętaj o wyświetleniu guzika do wysłania formularza!

from flask import Flask
from flask import request
app = Flask (__name__)


@app.route("/", methods=["GET", "POST"])
def kody_pocztowe():
    if request.method=="POST":
        kod = request.form["kod"]
        podzielony = kod.split("-")
        part1 = len(podzielony[0])
        part2 = len(podzielony[1])
        if part1 == 2 and part2 == 3:
            return f"""
                <html>
                    <body>
                        <h1>Kod {kod} jest poprawny.</h1>
                    </body>
                </html>"""
        else:
            return f"""
                <html>
                    <body>
                        <h1>Kod {kod} nie jest poprawny.</h1>
                    </body>
                </html>"""
    if request.method=="GET":
        return f"""
            <html>
                <body>
                    <form action="/" method = "POST">
                    <h1>Sprawdzę poprawność wprowadzonego kodu pocztowego!!!.</h1>
                    <label>
                        Podaj kod pocztowy: 
                        <input type="text" name="kod">
                    </label>
                    <label>
                    <button type="submit">
                    Sprawdź kod pocztowy
                    </label>
                </body>
            </html>"""


if __name__ == "__main__":
    app.run()