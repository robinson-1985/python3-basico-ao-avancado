'''
Tuplas diferentes de lista, não podem serem modificadas.

# Abaixo temos um código simples com tupla:

t1 = (1, 2, 3, 'a', 'Luiz Otávio')

print(type(t1))

# Abaixo vamos iterar a tupla:

t1 = (1, 2, 3, 'a', 'Luiz Otávio')

for v in t1:
    print(v)

# Agora vamos fatiar a tupla:

t1 = (1, 2, 3, 'a', 'Luiz Otávio')

print(t1[2:])  # igual a lista: 2 até o último elemento.


# Podemos fazer uma tupla sem os parênteses:

t1 = 1, 2, 3, 'a', 'Luiz Otávio'

print(t1)

# Podemos fazer uma tupla com apenas um valor, sempre acrescentando a ,

t1 = 1,

print(t1, type(t1))

# Podemos fazer uma concatenação com tuplas:

t1 = 1, 2, 3, 4, 5
t2 = 6, 7, 8, 9, 10
t3 = t1 + t2

print(t3)

# Podemos desempacotar em variáveis:

t1 = 1, 2, 'Gutemberg', 4, 5
t2 = 6, 7, 8, 9, 10
t3 = t1 + t2

n1, n2, n3, *_ = t3
n1, n2, n3, *_, n10 = t3

print(n3, n10)

# Podemos repetir o valor da tupla usando o multiplicador:

t1 = (1, 2, 'Gutemberg', 4, 5) * 20

print(t1)

# Podemos converter a tupla em lista:

t1 = (1, 2, 3, 4, 5)
t1 = list(t1)
t1[1] = 3000

print(t1)'''

# Podemos fazer a tupla que foi transformada em lista voltar a ser tupla:

t1 = (1, 2, 3, 4, 5)
t1 = list(t1)
t1[1] = 3000
t1 = tuple(t1)

print(t1)
