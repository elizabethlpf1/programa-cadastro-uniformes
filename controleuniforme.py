# Variáveis globais
lista_uniforme = []
codigo_uniforme = 0


# Função de cadastro de uniforme
def cadastrar_uniforme(codigo):
    print('Bem Vindo ao Menu de Cadastro de Uniforme')
    print('Código do uniforme: {}'.format(codigo))
    nome = input('Digite o nome do uniforme: ')
    modelo = input('Digite o modelo do uniforme: ')
    tamanho = input('Digite o tamanho do uniforme: ')

    dicionario_uniforme = {
        'codigo': codigo,
        'nome': nome,
        'modelo': modelo,
        'tamanho': tamanho
    }
    lista_uniforme.append(dicionario_uniforme)


# Função de consultar uniforme
def consultar_uniforme():
    print('Bem Vindo ao Menu de Consulta de Uniformes')
    while True:
        opcao_consultar = input('\nEscolha a opção desejada:\n' +
                                '1- Consultar estoque\n' +
                                '2- Consultar uniforme por código ID\n' +
                                '3- Consultar uniforme por modelo\n' +
                                '4- Retornar\n' +
                                '>> ')
        if opcao_consultar == '1':
            print('Você escolheu a opção consultar estoque')
            for uniforme in lista_uniforme:
                print('----------------------------')
                for key, value in uniforme.items():
                    print('{}: {}'.format(key, value))
                print('----------------------------')
        elif opcao_consultar == '2':
            print('Você escolheu a opção consultar uniforme por ID')
            valor_desejado = int(input('Entre com o número do código desejado: '))
            for uniforme in lista_uniforme:
                if uniforme['codigo'] == valor_desejado:
                    print('----------------------------')
                    for key, value in uniforme.items():
                        print('{}: {}'.format(key, value))
                    print('----------------------------')
        elif opcao_consultar == '3':
            print('Você escolheu a opção consultar uniforme por modelo')
            valor_desejado = input('Entre com o modelo desejado: ')
            for uniforme in lista_uniforme:
                if uniforme['modelo'] == valor_desejado:
                    print('----------------------------')
                    for key, value in uniforme.items():
                        print('{}: {}'.format(key, value))
                    print('----------------------------')
        elif opcao_consultar == '4':
            return  # Sai da função e volta para o início
        else:
            print('Opção inválida. Tente novamente.')
            continue  # Volta para o início do laço


# Função para remover uniforme
def remover_uniforme():
    print('Bem Vindo ao Menu de Remover Uniforme')
    valor_desejado = int(input('Entre com o código do uniforme que deseja remover: '))

    for uniforme in lista_uniforme:
        if uniforme['codigo'] == valor_desejado:
            lista_uniforme.remove(uniforme)
            print('Uniforme removido com sucesso!')
            return  # Sai da função após remover o uniforme

    print('Código não encontrado. Tente novamente.')


# Início do programa principal
print('Bem Vindo ao Menu Doação Uniformes Solidária Escola Professora Sebastiana Cobra')
while True:
    opcao_principal = input('\nEscolha a opção desejada:\n' +
                            '1- Cadastrar Uniforme\n' +
                            '2- Consultar Uniforme\n' +
                            '3- Remover Uniforme\n' +
                            '4- Sair\n' +
                            '>> ')
    if opcao_principal == '1':
        codigo_uniforme += 1
        cadastrar_uniforme(codigo_uniforme)
    elif opcao_principal == '2':
        consultar_uniforme()
    elif opcao_principal == '3':
        remover_uniforme()
    elif opcao_principal == '4':
        break
    else:
        print('Opção inválida. Tente novamente.')
        continue  # Volta para o início do laço

