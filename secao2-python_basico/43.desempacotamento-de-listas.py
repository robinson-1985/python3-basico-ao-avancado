''' lista = ['Luiz', 'João', 'Maria']

n1, n2, n3 = lista

print(n2)

* Se acontecer de retirar uma variável, ocorrerá um erro de desempacotamento
de lista. Portanto, para corrigir esse erro utilizamos a seguinte forma:

lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8]

n1, n2, n3, *outra_lista = lista

print(n1, n2, n3)

* Mas, o que aconteceu acima? Foi atribuído as variáveis e criada uma outra
lista.

Observe abaixo:

lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8]

n1, n2, n3, *outra_lista = lista

print(n1, n2, n3, outra_lista)
# Saída: Luiz João Maria [1, 2, 3, 4, 5, 6, 7, 8]

* E se eu quisesse pegar o último valor da lista? Vamos ver:



lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

n1, n2, n3, *outra_lista, ultimo_da_lista = lista

print(ultimo_da_lista)

* Agora vamos pegar os três últimos valores da lista:

lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

*outra_lista, y1, y2, y3 = lista

print(y1, y2, y3)

'''

# Caso vc só queira utilizar algumas variáveis, proceda assim:

lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8]

n1, n2, *_ = lista  # utilize asterisco + underline

print(n1, n2)
