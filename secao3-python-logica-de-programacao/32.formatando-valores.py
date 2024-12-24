''' Formatando valores com modificadores

:s - Texto (strings)

:d - Inteiros (int)

:f - Números de ponto flutuante (float)

:.(NÚMERO)f - Quantidade de casas decimais (float)
Ex: .2f

:(CARACTERES) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

Exemplos:

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0>10}')


> - Esquerda;
exemplo:
num_1 = 1
print(f'{num_1:0>10}')

< - Direita;
exemplo:
num_1 = 1
print(f'{num_1:0<10}')

^ - Centro.
Exemplo:
num_1 = 1
print(f'{num_1:0^10}')'''

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0>10.2f}')

nome = 'Otávio Miranda'
print((50-len(nome)) / 2)
print(f'{nome:#^50}')

nome = 'Otávio Miranda'
nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)

nome = 'Otávio Miranda'
nome_formatado = '{n:0<20}'.format(n=nome)
print(nome_formatado)

nome = 'Otávio'
sobrenome = 'Miranda'
nome_formatado = '{0:$^50} {1:#^10}'.format(nome, sobrenome)
print(nome_formatado)

# Outras funções de formatação

nome = 'Otávio Miranda'
nome = nome.ljust(20, '#')
print(nome)

nome = 'Otávio Miranda'
print(nome.lower())  # tudo minúsculo
print(nome.upper())  # tudo maiúsculo
print(nome.title())  # as primeiras letras ficam maiúsculas.
