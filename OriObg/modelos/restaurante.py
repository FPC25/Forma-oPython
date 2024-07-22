from modelos.avaliacao import Avaliacao

class Restaurante:
    '''
    Representa um restaurante e suas caracteristicas.
    
    '''

    #variavel global para armazenar os restaurantes cadastrados
    restaurantes = []

    def __init__(self, nome, categoria): #self so indica pro computador qual objeto ta chamando o modulo da classe
        '''
           Instancia de inicialização de um restaurante.

           Parametros:
           - nome (str): nome do restaurante
           - categoria (str): categoria do restaurante
        '''

        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        '''
            Retorna uma representação em string dos dados de um restaurante cadastrado.
        '''
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        '''
            Exibe uma lista formatada de todos os restaurantes.
        '''
        print('{} | {} | {} | {}'.format('Nome'.center(22), 'Categoria'.center(20), 'Avaliacao'.center(20), 'Status'.center(20)))
        for restaurante in cls.restaurantes:
           msg_avaliacao = f'{restaurante.media_avaliacao}({len(restaurante._avaliacao)})' if not type(restaurante.media_avaliacao) == str else f'{restaurante.media_avaliacao}'
           print('- {} | {} | {} | {}'.format(restaurante._nome.center(20), restaurante._categoria.center(20), msg_avaliacao.center(20), restaurante.ativo.center(20)))      

    @property #um decorator do python que permite mudar como um atriburo é lido
    def ativo(self):
        '''
            Uma função proprietaria da função que retorna um simbolo dependendo do estado da propriedade "ativo".
        '''
        return '☑' if self._ativo else '☐'
    
    def alternar_estado(self):
        '''
            Uma função para alterar o estado da propriedade "ativo, representado a atividade do restaurante ou não.
        '''
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        '''
            Registra uma avaliação para o restaurante.

            Parâmetros:
            - cliente (str): O nome do cliente que fez a avaliação.
            - nota (float): A nota atribuida ao restaurante que deve estar entre 0 e 5. Caso não cumpra tal requisito avisa o usuarrio e não contabiliza a nota.
        '''

        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        else:
            print('Error: A avaliação só será considerada se estiver entre 0 e 5.')

    @property
    def media_avaliacao(self):
        '''
            Método que calcula a media aritmetica das avaliações de cada restautante 
        '''
        if not self._avaliacao:
            return 'Não avaliado'
        media = round(sum(avaliacao._nota for avaliacao in self._avaliacao)/len(self._avaliacao), 1)
        return media