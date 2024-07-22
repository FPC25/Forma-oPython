from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
#restaurantes_suprema = Restaurante('pizza suprema', 'Italiana')
#restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
#restaurante_sushi = Restaurante('Kohaku Sushi', 'Japonesa')

bebida_suco = Bebida('Suco de Melancia', 5.0, 'Grande')
prato_paozinho = Prato('Paozinho', 2.0, 'O melhor pão da cidade')
sobremesa_torta = Sobremesa('Torta Holandesa', 15.0, 'Gelada')

bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()
sobremesa_torta.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(sobremesa_torta)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()