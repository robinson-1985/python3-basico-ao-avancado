''' Quantidade de caracteres.

usuario = input('Digite seu usuario: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

Teste:

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres')
else:
    print('Você foi cadastrado no sistema!')'''

string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(f'A qtd de caracteres digitados foi {len(string1) + len(string2)}')
