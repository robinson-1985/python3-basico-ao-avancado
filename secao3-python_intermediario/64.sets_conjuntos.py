'''
add (adiciona), update (atualiza), clear, discord
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

# a diferença entre os sets e dicionários é que os sets só recebem valores
s1 = {1,2,3,4,5,6,7,8}

print(s1)

# podemos iterar, mas, não acessar o valor
for v in s1:
    print(v)

# para criar um set vazio:
s1 = set()

# para adicionar
s1.add(1)
s1.add(2)
s1.add((1, 2, 3, 4, 'Luiz'))

print(s1)

# para remover:
s1 = set()
s1.add(1)
s1.add(2)
s1.discard(2)

print(s1)


# para fazer um update (é muito similar a função add, porém, ela faz iteração):
s1 = set()
s1.update('a')
s1.update('Python')
s1.update([1,2, 3, 4, 5], {5,6, 7, 8})
print(s1)


# podemos utilizar o set para não duplicarem números:
l1 = [1,2,1,1,3,4,5,6,6,6,6,7,8,9, 'Ivo', 'Ivo']
l1 = set(l1)

# posso fazer o set voltar a ser lista:
l1 = list(l1)

print(l1)

********************************************
s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}

# união dos dois conjuntos
s3 = s1 | s2 

# todos os elementos que estão presentes em ambos os conjuntos
s3 = s1 & s2 

# pegar somente os elementos do set da esquerda (difference)
s3 = s1 - s2 

# pegar os elementos que constam somente naquele set (symetric_difference)
s3 = s1 ^ s2 

print(s3)
'''

l1 = ['Luiz', 'Otávio', 'Ivo']
l2 = ['Otávio', 'Ivo', 'Ivo', 'Luiz', 'Luiz', 'Luiz', 'Luiz', 'Luiz', 'Luiz',]

if set(l1) == set(l2):
    print('L1 é igual a L2')
else:
    print('L1 é diferente de L2')
