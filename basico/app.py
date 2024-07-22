import os
import sys

#verificando a versão e escolhendo a versao da funcao usada
version = sys.version_info[0:2]
if version[0] < 3:
    import escolhe_antigo as esc
elif version[0] == 3:
    if version[1] < 10:
        import escolhe_antigo as esc
    else:
        import escolhe_novo as esc

#var globais
restaurantes = [{'nome': 'Praça', 'categoria': 'Brasileira', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}]

#funções auxiliares
def limpar_terminal(sistema = 'linux'):
    '''
    Função auxiliar que limpa o terminal usando o comando apropriado para o sistema do usuário. Note que para escolher o sistema, é necessário alterar a variavel quando aplicada na função "exibir_subtitulo".

    Input:
    - sistema: Variavel default para o linux (string)
    '''
    if sistema.lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')

def exibir_subtitulo(mensagem):
    '''
    Função recorrente que limpa o terminal da uma mensagem com a formatação de caixa ao redor da mensagem dada
    
    Input:
    - Mensagem: Titulo da funcionalidade usada (String)
    
    Output:
    - Mensagem formatada (String)
    '''
    limpar_terminal()
    linha = '*' * (len(mensagem) + 4)
    print(f'{linha}\n* {mensagem} *\n{linha}')
    print()

def cadastro_restaurante(nome, categoria):
    '''
    Função auxiliar que coloca o cadastro do restaurante em formato de dicionario e então devolve para ser usada na função principal
    
    Inputs:
    - nome: Nome do restaurante (String)
    - categoria: categoria do restaurante (String)

    Outputs:
    - cadastro: O cadastro do restaurante (Dictionary)
    '''

    cadastro = {'nome': nome, 'categoria': categoria, 'ativo': False}
    return cadastro

def voltar_ao_menu():
    '''
    Função recorrente que informa ao usuário que a função terminou e volta para o menu principal

    Input:
    - Qualquer tecla para voltar ao menu.
    '''
    input('\nDigite uma tecla para voltar ao menu principal\n')
    main()

def opcao_ivalida():
    '''
    Uma função recorrente que avisa que o usuário escolheu uma opção que não esta definida no aplicativo
    '''
    print('Opção inválida!\n')
    voltar_ao_menu()

#funcoes principais
def exibir_nome_do_programa():
    '''
    Função responsavel por apresentar o nome do programa do terminal
    '''
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

def menu_opcoes():
    '''
    Função responsavel por apresentar as opções para o usuário.
    '''
    print('1. Cadastrar restaurantes')
    print('2. Listar restaurantes')
    print('3. Ativar/Desativar restaurante')
    print('4. Sair\n')

def cadastrar_restaurante():
    '''
    Essa função é responsavel por cadastrar um novo restaurante.
    
    Input:
    - Nome do restaurante: É pedido para o usuário o nome do restaurante (String)
    - Categoria: A categoria que o restaurante (String)

    Output:
    - Adiciona um cadastro na lista de restaurantes (varivel global)
    '''

    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    restaurantes.append(cadastro_restaurante(nome_do_restaurante, categoria))
    
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu()

def listar_restaurantes():
    '''
    Essa função é responsavel por listar os restaurantes cadastrados.
    
    Output:
    - Lista em forma de tabela dos restaurantes já cadastrados.
    '''
    exibir_subtitulo('Listando restaurantes')

    print('{} | {} | {}\n'.format('  Nome'.center(22), 'Categoria'.center(20), 'Status'.center(20)))
    if len(restaurantes) == 0:
        print('Lista de restaurantes vazia')
    else: 
        for restaurante in restaurantes:
            nome = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
            print(f'- {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}\n')


    voltar_ao_menu()

def alterar_estado_restaurante():
    '''
    Essa função é resposavel por alterar o status do restaurante, se inicialmente ativado, desativa, e vice e versa.

    Output:
    - Statur: Altera o status do restaurante na lista de cadastro
    '''
    exibir_subtitulo('Alterando estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja ativar ou desativar: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante.lower() == restaurante['nome'].lower():
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print(f'Error: O restaurante "{nome_restaurante}" não foi encontrado.')


    voltar_ao_menu()

def encerrar_app():
    '''
    Função responsavel por encerrar o uso da aplicação
    '''
    exibir_subtitulo('Finalizndo o app')

# main
def main():
    exibir_nome_do_programa()
    menu_opcoes()
    esc.escolhe()

#iniciando o programa
if __name__ == "__main__":
    main()
