from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):

    def __init__(self, nome, preco, tamanho):
        '''
            Contrutor para o objeto bebidas do cardapio.

            Parametros:
            - nome (str): nome da bebida.
            - preco (float): preco da bebida.
            - volume (float): volume da bebida.
        '''
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self) :
        return self._nome
    
    def aplicar_desconto(self):
        desconto = 0.08
        self._preco -= (self._preco * desconto)