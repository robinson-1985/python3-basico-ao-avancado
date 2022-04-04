''' # Na maior parte das linguagens faríamos assim:

x = 10  # Luiz
y = 'Luiz'  # 10

z = x
x = y
y = z

print(f'x={x} e y={y}')

* Em Python fazemos assim:

x = 10  # Luiz
y = 'Luiz'  # 10
x, y = y, x

print(f'x={x} e y={y}')

x = 10  # Luiz
y = 'Luiz'  # 10
x, y = y, x

print(f'x={x} e y={y}')

x = 10  # Luiz
y = 'Luiz'  # 10
x, y = y, x

print(f'x={x} e y={y}')'''

x = 10  # Luiz
y = 'Luiz'  # 10
z = 'Otávio'
x, y, z = z, x, y

print(f'x={x}, y={y}, z={z}')
