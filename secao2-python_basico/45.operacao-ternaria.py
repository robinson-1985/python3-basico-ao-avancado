'''
* Podemos utilizar  um código para saber se o usuário está logado ou não:
logged_user = False

if logged_user:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário precisa logar.'

print(msg)

* Agora, posso simplificar o código utilizando operação ternária


logged_user = True
msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'

print(msg)'''

# Vamos para outro exemplo

idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('Você precisa digitar apenas números!')
else:
    idade = int(idade)
    e_maior = (idade >= 18)
    msg = 'Pode acessar!' if e_maior else 'Não pode acessar!'

print(msg)
