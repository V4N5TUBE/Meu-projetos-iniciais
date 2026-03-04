import os

nome_restaurantes = [{'nome': 'ifood', 'categoria': 'Fast Food', 'ativo': False},
                     {'nome': 'food99', 'categoria': 'delivery', 'ativo': True},
                     {'nome': 'Uber Eats', 'categoria': 'Fast Food', 'ativo': False}]

def exibir_nome_do_programa():
    print("""\n
██████╗░███████╗██╗░░░░░██╗██╗░░░██╗███████╗██████╗░██╗░░░██╗░█████╗░░█████╗░
██╔══██╗██╔════╝██║░░░░░██║██║░░░██║██╔════╝██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗
██║░░██║█████╗░░██║░░░░░██║╚██╗░██╔╝█████╗░░██████╔╝░╚████╔╝░██║░░╚═╝██║░░██║
██║░░██║██╔══╝░░██║░░░░░██║░╚████╔╝░██╔══╝░░██╔══██╗░░╚██╔╝░░██║░░██╗██║░░██║
██████╔╝███████╗███████╗██║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░╚█████╔╝╚█████╔╝
╚═════╝░╚══════╝╚══════╝╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░░╚════╝░
 
""")

def exibir_opcoes():
    """essa funcao tem a responsabilidade de exibir as opcoes para o usuario"""
    print('1. Cadastrar restaurantes')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    """essa funcao tem a responsabilidade de finalizar o app"""
    exibir_subtitulo('Encerrando o programa')

def opcao_invalida():
    """essa funcao tem a responsabilidade de tratar opcoes invalidas"""
    os.system('cls') 
    print('Opção inválida\n')
    voltar_menu_principal ()

def exibir_subtitulo(texto):
    """essa funcao tem a responsabilidade de exibir um subtitulo para o usuario"""
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_menu_principal ():
    """essa funcao tem a responsabilidade de voltar para o menu principal apos a execucao de uma acao"""
    input('Pressione Enter para voltar ao menu')
    main()

def cadastrar_novo_restaurante ():
    """essa funcao tem a responsabilidade de cadastrar um novo restaurante
    inputs: nome do restaurante e categoria
    
    outputs: mensagem de sucesso ou erro
    """
    exibir_subtitulo('Cadastrar novo restaurante')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    nome_restaurantes.append(dados_restaurante)
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso!\n')
    voltar_menu_principal ()

def Listar_restaurantes():
    """ essa funcao tem a responsabilidade de listar os restaurantes cadastrados e seu status (ativo ou desativado)"""
    exibir_subtitulo('Listando de restaurantes')
    print(f'{"Nome do restaurante".ljust(23)} | {"Categoria".ljust(20)} | {"Status"}')
    for restaurante in nome_restaurantes:
        nome = restaurante['nome']
        categorias = restaurante['categoria']
        ativo = "Ativo" if restaurante['ativo'] else "Desativado"
        print(f" - {nome.ljust(20)} | {categorias.ljust(20)} | {ativo} \n")

    voltar_menu_principal ()

def ativar_restaurante():
    """essa funcao tem a responsabilidade de ativar ou desativar um restaurante cadastrado

    -restaurante: e a nova variavel que recebe o nome do restaurante digitado pelo usuario

    -restaurante_encontrado: e a variavel que recebe o valor booleano para verificar se o restaurante foi encontrado ou nao

    -na parte do for o restaurante recebe os dados do nome_restaurante
    """
    exibir_subtitulo('Ativar restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar: ')
    restaurante_encontrado = False

    for restaurante in nome_restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'\nO restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'\nO restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'Restaurante {nome_restaurante} não encontrado.\n')

    voltar_menu_principal()

def escolher_opcao():
    """essa funcao tem a responsabilidade de receber a opcao escolhida pelo usuario e direcionar para a funcao correspondente"""
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            Listar_restaurantes()
        elif opcao_escolhida == 3: 
            ativar_restaurante()
        else: 
            finalizar_app()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
