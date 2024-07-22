class Veiculo:

    def __init__(self, marca, modelo):
        '''
            Contrutor da classe mãe "Veiculo" indicando um tipo de veiculo

            Parametros:
            - marca (str): marca do veiculo.
            - modelo (str): modelo do veiculo.
            - ligado (bool): Estado que se encontra o veiculo.
        '''

        self.marca = marca.title()
        self.modelo = modelo.title()
        self._ligado = False

    def __str__(self):
        return f'O veiculo da marca {self.marca} do modelo {self.modelo} esta desligado' if not self._ligado else f'O veiculo da marca {self.marca} do modelo {self.modelo} esta ligado'
