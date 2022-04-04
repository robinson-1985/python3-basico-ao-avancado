''' def funcao(var):
    print(var)


funcao('Valor que eu quero')


def funcao(var):
    print(var)


variavel = funcao('Valor que eu quero')
print(variavel)  # retornará none (sem valor)

# abaixo veremos outra forma para não retornar nenhum valor:


def funcao(var):
    print(var)


variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor!')

# abaixo ele retorna um valor não none.


def funcao(var):
    return var


variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor!')

# vamos aprender função para dividir:

def divisao(n1, n2):
    return n1 / n2


divide = divisao(8, 2)
print(divide)


def divisao(n1, n2):
    if n2 > 0:
        return n1 / n2  # lembrando que ao encontrar o return o programa para


divide = divisao(8, 0)

if divide:
    print(divide)
else:
    print('Conta inválida!')

# para isto podemos fazer assim:


def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2


divide = divisao(8, 2)

if divide:
    print(divide)
else:
    print('Conta inválida!')


def dumb():
    return 1


print(dumb(), type(dumb()))

# podemos fazer assim na variável também:


def dumb():
    return 1.1


var = dumb()
print(var, type(var))

# podemos retornar uma lista:


def dumb():
    return [1, 2, 3, 4, 5]


var = dumb()
print(var, type(var))

# podemos retornar um valor none:


def dumb():
    return


var = dumb()
print(var, type(var))

# podemos retornar um valor booleano:


def dumb():
    return True


var = dumb()
print(var, type(var))

*********************
- Função dentro de outra função:


def f(var):
    print(var)


def dumb():
    return f


var = dumb()('E colocar o meu valor aqui')

- Verificando o valor de cada função:

def f(var):
    print(var)


def dumb():
    return f


var = dumb()
print(id(var), id(f))

if var == f:
    print('var é igual a f')
else:
    print('Blaaaaaaaaaa')

- retornando um valor de função dentro de outra função:
def f(var):
    print(var)


def dumb():
    return f


var = dumb()
var('Pode imprimir algo na tela.')'''

# retornando uma tupla:


def dumb():
    return ('Luiz', 'Otávio')


var = dumb()

print(var, type(var))
