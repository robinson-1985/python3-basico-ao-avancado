'''
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range


lista = ['A', 'B', 'C', 'D', 'E', 10.5]
print(lista[1])
lista[5] = 'Qualquer outra coisa.'  # modificando o indice da lista
print(lista[0:3])  # fatiamento de lista.
print(lista[:3])  # fatiamento de lista
print(lista[-1])  # achando o último indice da lista.
print(lista[0])  # achando o primeiro indice da lista.
print(lista[::2])  # pedindo o primeiro e último indice e pulando de 2 em 2.

# exemplo de concatenação de strings
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2

print(l1)
print(l2)
print(l3)

# adicionando uma lista a outra utilizando extend
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)

print(l1)
print(l2)

# acrescentando novos valores a lista utilizando o append
l1 = [1, 2, 3]
l2 = [4, 5, 6]

l2.append('b')

print(l2[3])

print(l1)
print(l2)

# acrescentando novos valores a lista utilizando o insert
l1 = [1, 2, 3]
l2 = [4, 5, 6]

l2.insert(0, 'banana')

print(l2[0])

**** FUNÇÃO pop()
Para essa tarefa repetitiva, o Python trás implementado uma função que retorna
determinado elemento e ao mesmo tempo, exclui-o. Se nenhum argumento for
passado pela função pop() a mesma retornará e removerá o último elemento
da lista

l2 = [4, 5, 6]
print(l2)
l2.insert(0, 'banana')
print(l2)
l2.pop()
print(l2)

# excluindo indices:
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l2)
l2.insert(0, 'banana')
print(l2)
del(l2[0])

print(l2)

# iterando indices:
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

soma = 0
for valor in l2:
    soma = soma + valor
print(soma)'''

l2 = ['String', True, 10, -20.5]

for elem in l2:
    print(f'O tipo de elem é{type(elem)} e seu valor é {elem} ')
