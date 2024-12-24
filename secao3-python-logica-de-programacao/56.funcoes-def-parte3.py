# *args  **kwargs

'''
- Lembrando que os args ficam empacotados em forma de tuplas.


def func(*args):
    print(args)


lista = [1, 2, 3, 4, 5]
n1, n2, *n = lista
print(n1, n2, n)

# posso verificar somente o valor da lista:


def func(*args):
    print(args)


lista = [1, 2, 3, 4, 5]
print(lista)

# posso desempacotar o valor de cada item da lista:


def func(*args):
    print(args)


lista = [1, 2, 3, 4, 5]
print(*lista)


# podemos desempacotar o valor de cada item da lista com separador:


def func(*args):
    print(args)


lista = [1, 2, 3, 4, 5]
print(*lista, sep='-')  # posso utilizar , . / ou seja qq símbolo.


# Acessando o primeiro e último valor com args

def func(*args):
    print(args)
    print(args[0])  # primeiro valor
    print(args[-1])  # último valor
    print(len(args))  # verificando quantos valores tem dentro da tupla.


func(1, 2, 3, 4, 5)

# fazendo cast de tupla em lista


def func(*args):
    args = list(args)
    args[0] = 20
    print(args)


func(1, 2, 3, 4, 5)


# ou podemos trabalhar somente com tuplas mesmo:


def func(*args):
    for v in args:
        print(v)


func(1, 2, 3, 4, 5)


# podemos desempacotar o valor da tuplas e acrescentar valores a ela:


def func(*args):
    print(args)


lista = [1, 2, 3, 4, 5]
print(*lista, 10, 20, 30, 40, 50)


# podemos desempacotar o valor da tuplas e unir duas tuplas:


def func(*args):
    print(args)


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
print(*lista, *lista2)


# kwargs: keys arguments.


def func(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Pedro', sobrenome='Lima')

# quando temos certeza de encontrar um dado utilizamos o kwarg assim:


def func(*args, **kwargs):
    print(args)

    idade = kwargs.get('idade')
    print(idade)


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Pedro', sobrenome='Lima', idade=30)'''


# já na incerteza utilizamos kwargs assim:


def func(*args, **kwargs):
    print(args)

    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print('Idade não existe.')


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Pedro', sobrenome='Lima')
