'''
- expressões anônimas ou lambda

* Em uma função fazemos assim:

def funcao(arg, arg2):
    return arg * arg2


var = funcao(2, 2)

* Já na expressão anônima esse é o procedimento:

a = lambda x, y: x * y

print(a(2, 2))

* Mas, para que serve exatamente lambda?
Você pode ordenar uma lista, por exemplo, ao invés de usar o sort

# abaixo estamos utilizando o sort como forma normal de ordenar a lista

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]
lista.sort()
print(lista)

# abaixo utilizamos o valor preço(P) para ordenar a lista:
- Para ordenar a lista podemos utilizar funções:

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]


def func(item):
    return item[1]


lista.sort(key=func)  # do mais barato para o mais caro.
print(lista)


# abaixo utilizamos o valor preço(P) para ordenar a lista:

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]


def func(item):
    return item[1]


lista.sort(key=func, reverse=True)  # do mais caro para o mais barato.
print(lista)

- Percebemos, porém, que a função se torna verbosa ao utilizarmos nessa
expressão. Para isto, utilizamos a expressão lambda:

- Ordem normal

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

lista.sort(key=lambda item: item[1])
print(lista)

- Ordem invertida

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

lista.sort(key=lambda item: item[1], reverse=True)
print(lista)

- Ordem normal utilizando o sorted

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

print(sorted(lista, key=lambda i: i[1]))

# Ordem inversa utilizando o sorted

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

print(sorted(lista, key=lambda i: i[1], reverse=True))'''

# Ordenando inversamente pelo número do produto:

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

print(sorted(lista, key=lambda i: i[0], reverse=True))
