''' nome = input('Qual o seu nome? ')

if nome:
    print(nome)
else:
    print('Você não digitou nada =(')

* Essa expressão acima pode ser resumida com o operador OR:

nome = input('Qual o seu nome? ')

print(nome or 'Você não digitou nada!')

# A primeira expressão que o programa achar ele para:

nome = input('Qual o seu nome? ')

print(nome or None or False or 0 or 'Você não digitou nada!')'''

# quando queremos achar a variavel verdadeira fazemos assim:

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Luiz'

variavel = a or b or c or d or e or f or g
# percebe que o programa vai parar quando achar uma variável verdadeira!

print(variavel)
