# Calcule o seu IMC (Indice de Massa Corporal)

nome = input('Qual é o seu nome? ')
peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'{nome} tem {peso}kg e {altura}m de altura. Seu IMC é {imc:.2f}.')
