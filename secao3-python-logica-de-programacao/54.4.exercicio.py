'''
4 - Fizz Buzz - Se os parâmetros da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro
da 'função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário,
retorne  o número enviado.'''

from random import randint


def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'fizzbuzz, {n} é divisível por 3 e 5'
    if n % 5 == 0:
        return f'buzz, {n} é divisível por 5'
    if n % 3 == 0:
        return f'fizz, {n} é divisível por 3'
    return n


for i in range(50):
    aleatorio = randint(0, 50)
    print(fb(aleatorio))
