from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurantes_suprema = Restaurante('pizza suprema', 'Italiana')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_sushi = Restaurante('Kohaku Sushi', 'Japonesa')

restaurante_mexicano.alternar_estado()

restaurante_praca.receber_avaliacao('Gui', 3.4)
restaurante_praca.receber_avaliacao('Lais', 2)
restaurante_praca.receber_avaliacao('Emy', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()