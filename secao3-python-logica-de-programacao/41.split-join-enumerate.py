'''
* Split - Divide uma string
- Usando espaço para separar as strings:

string = 'O Brasil é o país do futebol, o Brasil é penta!'
lista = string.split(' ')

print(lista)

# usando espaço e vírgula para separar as strings

string = 'O Brasil é o país do futebol, o Brasil é penta!'
lista_1 = string.split(' ')
lista_2 = string.split(',')

print(lista_1, lista_2)

# agora vamos iterar as strings

string = 'O Brasil é o país do futebol, o Brasil é penta!'
lista_1 = string.split(' ')
lista_2 = string.split(',')

for valor in lista_1:
    print(valor)

# vamos contar as strings utilizando o método count

string = 'O Brasil é o país do futebol, o Brasil é penta!'
lista_1 = string.split(' ')
lista_2 = string.split(',')

for valor in lista_1:
    print(f'A palavra {valor} apareceu {lista_1.count(valor)} x na frase.,')

# contando as palavras que mais apareceram utilizando o método count

string = 'O Brasil é o país do futebol, o Brasil é penta!'
lista_1 = string.split(' ')
lista_2 = string.split(',')

palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

# utilizando a função capitalize
string = 'O Brasil é o país do futebol, o Brasil é penta!'
lista_1 = string.split(' ')
lista_2 = string.split(',')

for valor in lista_2:
    print(valor.strip().capitalize())

* Join - Juntar uma lista em string.
Ou seja, adicionar elementos a uma lista baseado em algo que queremos.

string = 'O Brasil é o país do futebol, o Brasil é penta!'
lista = string.split(' ')
string2 = ' '.join(lista)

print(string)
print(lista)
print(string2)

* Enumerate - Enumemar elementos da lista # iteráveis.

string = 'O Brasil é o país do futebol, o Brasil é penta!'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])

# vamos colocar uma lista dentro de outra.

lista = [
    [1, 2],
    [3, 4],
    [5, 6],
]

for v in lista:
    print(v[0], v[1])

# vamos enumerar os indíces.

lista = [
    [0, 'Luiz'],
    [1, 'João'],
    [2, 'Maria'],
]

for indice, nome in lista:
    print(indice, nome)'''

# Utilizando o enumerate para fazer o exemplo acima:

lista = ['Luiz', 'João', 'Maria']

for indice, nome in enumerate(lista):
    print(indice, nome)
