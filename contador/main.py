#PROBLEMA: Faça um contador de palavras. O projeto deve receber uma frase do usuário e contar quantas vezes cada palavra aparece.

from contador import contar_palavras

frase = input('Digite uma frase: ').strip()
if not frase:
    print('Erro: Nenhuma frase foi digitada.')
else:
    resultado = contar_palavras(frase)
    if resultado:
        print('Contagem de palavras:')
        for palavra, quantidade in resultado.items():
            print(f'{palavra} : {quantidade}')
    else:
        print(f'Nenhuma palavra válida foi encontrada.')
