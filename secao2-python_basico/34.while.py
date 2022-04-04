'''
While - Estruturas de repetições;
Utilizado para realizar ações enquanto houver uma condição verdadeira.

# while executando um código simples
x = 0
while x < 100:
    print(x)
    x = x + 1
print('Acabou!')

# while utilizando o continue
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue  # ele vai pular o número 3 nesse caso.

    print(x)
    x = x + 1

print('Acabou!')

# while utilizando o break (parada)
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break  # ele vai parar no número 3.

    print(x)
    x = x + 1

print('Acabou!')

# while com matriz
x = 0  # coluna
while x < 10:
    y = 0  # linha

    while y < 5:
        print(f'({x},{y})')
        y += 1
    x += 1

print('Acabou!')'''

# Vamos fazer uma calculadora:

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador inválido!')
