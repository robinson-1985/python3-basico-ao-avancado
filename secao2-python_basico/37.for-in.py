'''
For in in Python (utilizados para coisas finitas)
Iterando strings com for
Função range(start=0, stop, step=1)

texto = 'Python'

for letra in texto:
    print(letra)

*** Posso fazer de uma maneira mais difícil:
for n, letra in enumerate(texto):
    print(n, letra)

# Função range(start=0, stop, step=1)

# Função range padrão:
for n in range(10):
    print(n)

# Função range positiva:
for n in range(20, 100, 10):
    print(n)

# Função range negativa:
for n in range(20, 10, -1):
    print(n)

# podemos achar os múltiplos de um número:
for n in range(0, 100, 8):
    print(n)

# podemos achar os múltiplos de um número assim tb:
for n in range(100):
    if n % 8 == 0:
        print(n)

# podemos usar o recurso da letra em maiúscula:
texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)'''

# continue - pula para o próximo laço;
texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        continue
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)

# break - termina o laço.
texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra

print(nova_string)
