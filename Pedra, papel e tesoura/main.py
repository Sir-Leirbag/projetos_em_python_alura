import random

def gerar_elemento():
    opcoes = ['pedra', 'papel', 'tesoura']
    return random.choice(opcoes)

def limpar_entrada(elemento):
    elemento = elemento.islower()

elemento = input('Escolha: pedra, papel ou tesoura? ')
jogada_computador = gerar_elemento()

if elemento == jogada_computador:
    print(f'O computador escolheu: {jogada_computador}')
    print('Empate!')
elif elemento == 'pedra' and jogada_computador == 'tesoura':
    print(f'O computador escolheu: {jogada_computador}')
    print('Você venceu!')
elif elemento == 'pedra' and jogada_computador == 'papel':
    print(f'O computador escolheu: {jogada_computador}')
    print('O computador venceu!')
elif elemento == 'papel' and jogada_computador == 'pedra':
    print(f'O computador escolheu: {jogada_computador}')
    print('Você venceu!')
elif elemento == 'papel' and jogada_computador == 'tesoura':
    print(f'O computador escolheu: {jogada_computador}')
    print('O computador venceu!')
elif elemento == 'tesoura' and jogada_computador == 'papel':
    print(f'O computador escolheu: {jogada_computador}')
    print('Você venceu!')
elif elemento == 'tesoura' and jogada_computador == 'pedra':
    print(f'O computador escolheu: {jogada_computador}')
    print('O computador venceu!')
else:
    print('Jogada inválida')
