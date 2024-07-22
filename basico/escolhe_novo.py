import OriObg.app2 as app2

def escolhe():
    '''
    Função que recebe a escolha do usuario de qual função da aplicação ele deseja usar.
    Versão nova: Funciona para aplicação rodando com python >= 3.10

    Input:
    - opção: Numero que representa a função a ser acessada (Int)

    Output:
    - aplicação: se a escolha for valida encaminha para a função desejada, se não repete a pergunta.
    '''
    try:
        opcao = int(input('Escolha uma opção: '))
        match opcao:
            case 1:
                app2.cadastrar_restaurante()
            case 2:
                app2.listar_restaurantes()
            case 3:
                app2.alterar_estado_restaurante()
            case 4:
                app2.encerrar_app()
            case _:
                app2.opcao_ivalida()
    except:
        app2.opcao_ivalida()

#iniciando o programa
if __name__ == "__main__":
    escolhe()