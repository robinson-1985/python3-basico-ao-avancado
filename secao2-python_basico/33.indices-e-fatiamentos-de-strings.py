''' Manipulando Strings
* String indíces
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.'''

# indices positivos
texto = 'Python s2'
print(texto[8])

# indices negativos

url = 'www.google.com.br/'
print(url[:-1])

# fatiamento de string - colocamos assim [numeroinicio:numerofinal]

nova_string = texto[2:6]
print(nova_string)

nova_string = texto[:6]
print(nova_string)

nova_string = texto[7:]
print(nova_string)

# pular caracteres
nova_string = texto[0:6:2]
print(nova_string)

# função len
print(len(texto))

for letra in texto:
    print(letra)
