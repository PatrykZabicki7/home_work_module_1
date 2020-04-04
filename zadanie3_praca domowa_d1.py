# Napisz funkcję o nazwie circle_circuit, która przyjmując średnicę okręgu zwróci jego obwód.
# Przyjmij, że parametry wejściowe są poprawne. Przyjmij pi=3.14.

def circle_circuit(d):
    obwod = 2*3.14*(d/2)
    return obwod

print(circle_circuit(7))