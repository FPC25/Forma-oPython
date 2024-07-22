from veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, marca, modelo, portas):
        '''
            Contrutor da classe filha "Carro".

            parametros:
            - marca (str): marca do carro (herdado da classe mãe)
            - modelo (str): modelo do carro (herdado da classe mãe)
            - portas (int): numero de portas do carro.
                    
        '''
        super().__init__(marca, modelo)
        self.portas = portas

    def __str__(self):
        return f'{super().__str__()} e tem {self.portas} portas.'