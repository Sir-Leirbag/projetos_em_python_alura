import os

def adicionar_tarefa(tarefa_adicionada):
    tarefa_adicionada = input('\nDigite a tarefa que deseja adicionar: ')
    lista_de_tarefas.append(tarefa_adicionada)
    print('\nTarefa adicionada!')

def visualizar_tarefas():
    print(lista_de_tarefas)

def remover_tarefa(tarefa_removida):
    tarefa_removida = input('\nDigite a tarefa que será removida: ')
    lista_de_tarefas.remove(tarefa_removida)


'''def sair():
    return quit()'''

lista_de_tarefas = []

def main():
    while True:
        tarefa = ''
        opcoes = (1, 2, 3, 4)
        try:
            opcao = int(input(                         
'''\n1. Adcionar tarefa
2. Visualizar tarefas
3. Remover tarefa
4. Sair
Escolha uma opcão: '''))
        except ValueError:
            print('\nOpção inválida.')
            continue
        if opcao not in opcoes:
            print('Opcão inválida.')
            continue
        elif opcao == 1:
            adicionar_tarefa(tarefa)
            continue
        elif opcao == 2:
            visualizar_tarefas()
            continue
        elif opcao == 3:
            remover_tarefa(tarefa)
        elif opcao == 4:
            break

main()
