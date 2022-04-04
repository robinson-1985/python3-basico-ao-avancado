'''
Variavel com break

variavel = ['Luiz Otavio', 'Joãozinho', 'Maria']

for valor in variavel:
    print(valor)
    break
    print(valor)

# checa se a string começa com tal letra.

variavel = ['Luiz Otavio', 'Joãozinho', 'Maria']

for valor in variavel:
    if valor.startswith('J'):
        print('Começa com J', valor)
    else:
        print('Não começa com J', valor)

# checando a palavra, porém, não distingue minúsculo de maiúscula
variavel = ['Luiz Otavio', 'Joãozinho', 'Maria']

comeca_com_j = False
for valor in variavel:
    if valor.startswith('J'):
        comeca_com_j = True

if comeca_com_j:
    print('Existe uma palavra que começa com J.')
else:
    print('Não existe uma palavra que começa com J.')

# checando a palavra sem distinção entre minúscula de maiúscula

variavel = ['Luiz Otavio', 'Joãozinho', 'Maria']

comeca_com_j = False
for valor in variavel:
    if valor.lower().startswith('j'):
        comeca_com_j = True

if comeca_com_j:
    print('Existe uma palavra que começa com J.')
else:
    print('Não existe uma palavra que começa com J.')

# Vamos diminuir o código acima utilizando o break:

variavel = ['Luiz Otavio', 'Joãozinho', 'Maria']

for valor in variavel:
    print(valor)
    if valor.lower().startswith('j'):
        break
else:
    print('Não existe uma palavra que começa com J.')'''

# Vamos utilizar agora o break:

variavel = ['Luiz Otavio', 'Joãozinho', 'Maria']

for valor in variavel:
    if valor.lower().startswith('j'):
        continue
    print(valor)
