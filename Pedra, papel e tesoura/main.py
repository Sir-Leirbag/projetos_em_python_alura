import random

def gerar_elemento():
    opcoes = ['pedra', 'papel', 'tesoura']
    return random.choice(opcoes)

def limpar_entrada(elemento):
    return elemento.lower()

elemento = input('Escolha: pedra, papel ou tesoura? ')
jogada_computador = gerar_elemento()
jogadada_usuario = limpar_entrada(elemento)

if jogadada_usuario == jogada_computador:
    print(f'O computador escolheu: {jogada_computador}')
    print('Empate!')
elif jogadada_usuario == 'pedra' and jogada_computador == 'tesoura':
    print(f'O computador escolheu: {jogada_computador}')
    print('Você venceu!')
elif jogadada_usuario == 'pedra' and jogada_computador == 'papel':
    print(f'O computador escolheu: {jogada_computador}')
    print('O computador venceu!')
elif jogadada_usuario == 'papel' and jogada_computador == 'pedra':
    print(f'O computador escolheu: {jogada_computador}')
    print('Você venceu!')
elif jogadada_usuario == 'papel' and jogada_computador == 'tesoura':
    print(f'O computador escolheu: {jogada_computador}')
    print('O computador venceu!')
elif jogadada_usuario == 'tesoura' and jogada_computador == 'papel':
    print(f'O computador escolheu: {jogada_computador}')
    print('Você venceu!')
elif jogadada_usuario == 'tesoura' and jogada_computador == 'pedra':
    print(f'O computador escolheu: {jogada_computador}')
    print('O computador venceu!')
else:
    print('Jogada inválida')
