from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):

    def __init__(self, nome, preco, tipo):
        '''
            Contrutor para o objeto prato do cardapio.

            Parametros:
            - nome (str): nome do prato.
            - preco (float): preco do prato.
            - tipo (str): tipo da sobremesa (gelada, quente).
        '''
        super().__init__(nome, preco)
        self._tipo = tipo

    def __str__(self) :
        return self._nome
    
    def aplicar_desconto(self):
        desconto = 0.1
        self._preco -= (self._preco * desconto)