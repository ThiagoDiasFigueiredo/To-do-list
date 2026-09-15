def tarefas():
    print('================')
    print('LISTA DE TAREFAS')
    print('================')

    lista_tarefas = []

    usuario = 0

    while usuario != 5:
        print('\nO que deseja fazer?')
        print('[1] Adicionar tarefa')
        print('[2] Remover tarefa')
        print('[3] Verificar tarefas')
        print('[4] Concluir uma tarefa')
        print('[5] Sair')

        usuario = int(input('Digite o que deseja fazer: '))

        if usuario == 1:
            tarefa = input('Digite a tarefa: ')

            nova_tarefa = {
                "Nome": tarefa,
                "Concluida": False
            }

            lista_tarefas.append(nova_tarefa)

            print('Tarefa adicionada!')

        elif usuario == 2:
            if len(lista_tarefas) == 0:
                print('Não foi possível remover nenhuma tarefa!')
                continue

            for i in range(len(lista_tarefas)):
                print(f'{i + 1}: {lista_tarefas[i]["Nome"]}')

            remover = int(input('Digite o elemento que quer remover: '))

            if remover < 1 or remover > len(lista_tarefas):
                print('Tarefa inválida!')
                continue

            else:
                lista_tarefas.pop(remover - 1)
                print('Tarefa removida!')

        elif usuario == 3:
            if len(lista_tarefas) == 0:
                print('Nenhuma tarefa cadastrada!')
                continue

            print('\n--- SUAS TAREFAS ---')

            for i in range(len(lista_tarefas)):
                print(f'{i + 1}: {lista_tarefas[i]["Nome"]}')
                print(f'Concluída: {lista_tarefas[i]["Concluida"]}')
            
        elif usuario == 4:
            if len(lista_tarefas) == 0:
                print('Nenhuma tarefa cadastrada!')
                continue

            print('\n--- SUAS TAREFAS ---')

            for i in range(len(lista_tarefas)):
                print(f'{i + 1}: {lista_tarefas[i]["Nome"]}')
                print(f'Concluída: {lista_tarefas[i]["Concluida"]}')

            mudanca = int(input('Digite a tarefa que você quer mudar de estado:'))
            escolha = int(input('Escolha qual estado você quer: '))
            print('1: False')
            print('2: True')
            escolha = int(input(''))
            if escolha == 1:
                escolha = False
            elif escolha == 2:
                escolha = True
            
            lista_tarefas[mudanca-1]["Concluida"] = escolha
            
    print('Programa encerrado!')


def main():
    tarefas()


if __name__ == '__main__':
    main()