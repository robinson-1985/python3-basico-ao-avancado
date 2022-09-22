print('Escolha entre as alternativas abaixo e responda: ')

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2? ',
        'respostas': {
            'a': '4',
            'b': '10',
            'c': '6',
        },
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 1+2? ',
        'respostas': {
            'a': '1',
            'b': '3',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 1-1? ',
        'respostas': {
            'a': '0',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'a',
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 8/4? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '2',
        },
        'resposta_certa': 'c',
    },

}

# agora vamos iterar as perguntas:
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'[{pk}]: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
    
    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('EHHHHHHH!!! Você acertou!!!!!')
        respostas_certas += 1

    else:
        print('IXIIII!!! VOCÊ ERROU!!!')

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%')
