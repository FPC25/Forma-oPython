from abc import ABC, abstractmethod
class ItemCardapio(ABC):

    def __init__(self, nome, preco):
        '''
            Contrutor do objeto que inicializa o objeto e cria um item no cardapio.

            Parametros:
            - _nome (str) = nome do item do cardapio
            - _preco (float) = preço do item
        '''
        
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        pass