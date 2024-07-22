import app as app

def escolhe():
    '''
    Função que recebe a escolha do usuario de qual função da aplicação ele deseja usar.
    Versão antiga: Funciona para aplicação rodando com python < 3.10

    Input:
    - opção: Numero que representa a função a ser acessada (Int)

    Output:
    - aplicação: se a escolha for valida encaminha para a função desejada, se não repete a pergunta.
    '''
    try:
        opcao = int(input('Escolha uma opção: '))
        if (opcao == 1):
            app.cadastrar_restaurante()
        elif (opcao == 2):
            app.listar_restaurantes()
        elif (opcao == 3):
            app.alterar_estado_restaurante()
        elif (opcao == 4):
            app.encerrar_app()
        else:
            app.opcao_ivalida()
    except:
        app.opcao_ivalida()
    

#iniciando o programa
if __name__ == "__main__":
    escolhe()
