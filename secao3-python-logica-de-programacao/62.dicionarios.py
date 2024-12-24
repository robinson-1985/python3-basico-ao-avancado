''' Os dicionários são coleções de itens e seus elementos são armazenados de
forma não ordenada. Seus elementos contém uma chave e valor, isto é:

Uma chave que vai servir para indexar (posicionar) determinado elemento no
dicionário. Este valor aceita diversos tipos: listas, outros dicionários,
inteiros, strings e etc.

Sua sintaxe básica é: {'chave': 'valor'}. Utiliza-se {} para delimitar o
dicionário e a chave é separada do valor por dois pontos :

d1 = {'chave1': 'valor da chave'}

print(d1)

# Criando nova chave:

d1 = {'chave1': 'valor da chave'}
d1['nova_chave'] = 'Valor da nova chave'

print(d1)'''

# Acessando o valor de uma chave:

''' d1 = {'chave1': 'valor da chave'}
d1['nova_chave'] = 'Valor da nova chave'

print(d1['chave1'])'''

# Existe uma maneira diferente de criar dicionários:

'''d1 = dict(chave1='valor da chave', chave2='valor da outra chave')
d1['nova_chave'] = 'Valor da nova chave'

print(d1['chave1'])'''

# Posso utilizar qualquer dado imutáveis em chaves

d1 = {
    'chave1': 'valor',
    'chave2': 'Outro valor',
    'chave3': 'Tupla',
}

#  d1['nomedachave'] = 'Agora ela existe'
'''
- Adicionando nova chave no dicionário:

d1.update({'nova_chave': 'novo_valor'})

print(d1[(1, 2, 3, 4)])

if d1.get('nomedachave') is not None:
    print(d1.get('nomedachave'))

print(123)

# deletando chave no dicionário:

del d1['chave1']

print(d1)

# checando um valor

print('chave1' in d1)
print('chave2' in d1.keys())
print('chave3' in d1.values())

# checando quantos pares tem no dicionário:

print(len(d1))

# iterando dicionário

for k in d1:
    print(k)

# iterando e mostrando os valores

for v in d1.values():
    print(v)

# Acessar chave e valor

for i in d1.items():
    print(i[0], i[1])

# desempacotar a chave e valor

for m, n in d1.items():
    print(m, n)

clientes = {
    'cliente1': {
        'nome': 'Luiz',
        'sobrenome': 'Otávio',
    },
    'cliente2': {
        'nome': 'Mario',
        'sobrenome': 'Henrique',
    },
    'cliente3': {
        'nome': 'João',
        'sobrenome': 'Carlos',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

d1 = {1:'a', 2:'b', 3:'c'}
v = d1

v[1] = 'Luiz'

print(d1)
print(v)

v = d1.copy()
v[1] = 'Luiz'

print(d1)
print(v)

d1 = {1:'a', 2:'b', 3:'c', 'd': ['Luiz', 'Otávio']}
v = d1.copy()

v[1] = 'Luiz'

print(v['d'][0])

print(d1)
print(v)

import copy

d1 = {1:'a', 2:'b', 3:'c', 'd': ['Luiz', 'Otávio']}
v = copy.deepcopy(d1)

v[1] = 'Luiz'

v['d'][0] = 'Joãozinho'

print(d1)
print(v)

# convertendo chave em dicionário

lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

d1 = dict(lista)
print(d1)
print(d1['c3'])'''
