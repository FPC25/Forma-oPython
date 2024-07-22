from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):

    def __init__(self, nome, preco, descricao):
        '''
            Contrutor para o objeto prato do cardapio.

            Parametros:
            - nome (str): nome do prato.
            - preco (float): preco do prato.
            - descricao (str): descricao do prato.
        '''
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self) :
        return self._nome
    
    def aplicar_desconto(self):
        desconto = 0.05
        self._preco -= (self._preco * desconto)