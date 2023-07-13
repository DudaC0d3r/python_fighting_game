lista_clientes = []

def menu_principal():
    print('----------MENU PRINCIPAL----------')
    print('(1) Cadastrar novo cliente')
    print('(2) Consultar cliente')
    print('(3) Editar cliente')
    print('(4) Excluir cliente')
    print('(0) Sair')
menu_principal()

first_choise = int(input('Escolha a função desejada: '))
while first_choise < 0 or first_choise > 5:
    print('Opção inválida. Por favor, selecione uma das opções do menu.')
    first_choise = int(input('Escolha a função desejada: '))
else:
    if first_choise == 0:
        print("Programa desenvolvido por @roddyzera. Obrigado por utilizar.")
        import time, sys
        for i in range(0, 10):
            sys.stdout.write("\r{}".format(i))
            sys.stdout.flush()
            time.sleep(1)
        exit()
    elif first_choise == 1:
        print('Cadastrar novo cliente.')
        ident = input('ID: ')
        nome = input('Nome: ')
        telefone = input('Telefone: ')
        endereco = input('Endereço: ')
        print('{}, {}, {}'.format(nome, telefone, endereco))
        lista_clientes.append((ident, nome, telefone, endereco))
        cadastrar_de_novo = input('Deseja cadastrar novo cliente? [s/n]: ')
        while cadastrar_de_novo == 's':
            print('Cadastrar novo cliente.')
            ident = input('ID: ')
            nome = input('Nome: ')
            telefone = input('Telefone: ')
            endereco = input('Endereço: ')
            print('{}, {}, {}'.format(nome, telefone, endereco))
            lista_clientes.append((ident, nome, telefone, endereco))
            cadastrar_de_novo = input('Deseja cadastrar novo cliente? [s/n]: ')
        else:
            first_choise = menu_principal()
            
    elif first_choise == 2:
        print(lista_clientes)

    elif first_choise == 3:
        print('Consultar cliente.')

    elif first_choise == 4:
        print('Consultar cliente.')