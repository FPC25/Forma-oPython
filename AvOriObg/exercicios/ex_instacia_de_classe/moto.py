from veiculo import Veiculo

class Moto(Veiculo):

    def __init__(self, marca, modelo, tipo):
        '''
            Contrutor da classe filha "Moto".

            parametros:
            - marca (str): marca da moto (herdado da classe mãe)
            - modelo (str): modelo da moto (herdado da classe mãe)
            - tipo (str): O tipo da moto se é esportiva ou casual.
                    
        '''
        super().__init__(marca, modelo)
        self.tipo = tipo.title()

    def __str__(self):
        return f'{super().__str__()} e é uma moto {self.tipo}.'