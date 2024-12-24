primeira = int(input('Primeira nota: '))
segunda = int(input('Segunda nota: '))

if primeira > segunda:
    print(f'{primeira} é maior que{segunda}')
elif primeira < segunda:
    print(f'{segunda} é maior que a {primeira}')
else:
    print(f'{primeira} e {segunda} são iguais')
