string = '0123456789012345678901234567890123456789012345678901234567890123456789'
n = 10
contadores = [i for i in range(0, len(string), n)] # separa em grupo de 10 em 10
tuplas = [(i, i+n) for i in range(0, len(string), n)] # separa os conjuntos de 0,10 por diante 
lista = [string[i:i+n] for i in range(0, len(string), n)] # mostram os grupos de 0 a 9
retorno = '.'.join(lista) # acrescenta pontuação entre os grupos de 0 a 9

# o .join sempre irá acrescentar algo e agregar. Ex: "-".join, "@".join
# retorno = '@'.join(lista)

print(contadores)
print(tuplas)
print(lista)
print(retorno)
