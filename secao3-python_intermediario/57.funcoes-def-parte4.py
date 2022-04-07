''' # variável com escopo global:

variavel = 'valor'


def func():
    print(variavel)


def func2():
    print(variavel)


func()
func2()


# variável com escopo global agregando outro valor:

variavel = 'valor'


def func():
    print(variavel)


def func2():
    variavel = 'Outro valor'
    print(variavel)


func()
func2()

print(variavel)'''


# alterando o valor da função:

variavel = 'valor'


def func():
    print(variavel)


def func2(arg=None):
    arg = arg.replace('v', 'c')  # trocando v por c
    return arg


func()
outra_variavel = func2(arg=variavel)

print(outra_variavel)
