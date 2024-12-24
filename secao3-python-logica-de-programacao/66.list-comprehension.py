l1 = [1,2, 3, 4, 5, 6, 7, 8, 9]
ex1 = [variavel for variavel in l1]

# multiplicando a l1 por 2
ex2 = [v * 2 for v in l1]

# iterando sobre cada elemento da lista
ex3 = [(v, v2) for v in l1 for v2 in range(3)]

# print(ex2)
# print(ex3)

# trocando a letra a por @
l2 = ['Luiz', 'Mauro', 'Maria']
ex4 = [v.replace('a', '@')for v in l2]

# print(ex4)

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)

# ex5 = [(x, y) for x, y in tupla]
# agora iremos inverter o conteúdo da tupla onde tinha chave é valor e vice-versa
ex5 = [(y, x) for x, y in tupla]
# podemos modificar para um dicionário
ex5 = dict(ex5)
# print(ex5)

# posso utilizar mais de um if
l3 = list(range(100))
# aqui utilizamos um if
ex6 = [v for v in l3 if v % 2 == 0] # todos os nº de 0 a 100 divisiveis por 2
# abaixo utilizaremos mais de um if
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0] # todos os nº de 0 a 100 divisiveis por 3 e 8
# print(ex6)

# utilizando o else 
ex7 = [v if v % 3 == 0 else '0' for v in l3] # somente nº divisiveis por 3, se não 0.

# podemos utilizar outras condições com else
ex7 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]
print(ex7)
