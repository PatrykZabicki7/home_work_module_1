# # sposób dobry dla małych liczb ok.35 . Później czas obliczeń jest zbyt długi.
# def cos(n):
#     if n<2:
#         return n
#     else:
#         return cos(n-1)+cos(n-2)
# print(cos(35))


# Ta metoda jest niezrozumiała do końca !!!
# def fib(n):
#     if n < 2:
#         return n
#     a = 0
#     b = 1
#     for x in range(1, n):
#         a, b = b, a + b
#     return b
# print(fib(20))


# rekurencja wykorzystana do odliczania od n do zera
# def odliczanie(n):
#   if n == 0:
#     print('Blastoff!')
#   else:
#     print(n)
#     odliczanie(n - 1)
#
# odliczanie(5)


# Dodamy dodatkowe wydruki, aby zrozumieć, jak program działa. Ta wersja programu
# odczytuje również liczbę, od której ma sie rozpocząć liczenie.
def countdown(n):
  print('Entering countdown(',n,')')
  if n == 0:
    print('Blastoff!')
  else:
    print(n)
    countdown(n - 1)
  print('Exiting from countdown(',n,')')

limit = int(input("Wprowadź limit: "))
countdown(limit)


