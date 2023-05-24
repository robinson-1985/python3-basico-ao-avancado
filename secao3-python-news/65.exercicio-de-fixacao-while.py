nome = 'Robinson Dias'

contador = 0
novo_nome = ''
while contador < len(nome):
    letra = nome[contador]
    novo_nome += f'*{letra}'
    contador += 1

novo_nome += '*' # Adiciona o asterisco no final da string (não faz parte do laço)

print(novo_nome)
