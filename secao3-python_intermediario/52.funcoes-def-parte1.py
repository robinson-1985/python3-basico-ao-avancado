'''def funcao():
    print('Hello world!')


funcao()

print('Hello world!')


def saudacao(msg='Olá', nome='Usuário'):
    print(msg, nome)


saudacao('Luiz Otávio', 'Olá')  # esse argumento está errado!
saudacao('Oi', 'Luiz')
saudacao('Hello', 'Maria')
saudacao('Olá', 'Otávio')
saudacao('Olá', 'João')

# Como o argumento acima está errado, podemos corrigir assim:


def saudacao(msg='Olá', nome='Usuário'):
    print(msg, nome)


saudacao(nome='Zezinho', msg='Hi')  # houve uma inversão dos valores.
saudacao('Oi', 'Luiz')
saudacao('Hello', 'Maria')
saudacao('Olá', 'Otávio')
saudacao('Olá', 'João')'''


def saudacao(msg='Olá', nome='Usuário'):
    nome = nome.replace('e', '3')  # a letra e vai ser mudada para o número 3
    msg = msg.replace('e', '3')
    print(msg, nome)


saudacao(nome='Zezinho', msg='Hi')  # houve uma inversão dos valores.
saudacao('Oi', 'Luiz')
saudacao('Hello', 'Maria')
saudacao('Olá', 'Otávio')
saudacao('Olá', 'João')
