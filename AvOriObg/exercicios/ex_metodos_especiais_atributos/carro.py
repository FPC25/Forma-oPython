from veiculo import Veiculo

class Carro(Veiculo):
    
    def __init__(self, modelo, marca, cor):
        super().__init__(modelo, marca)
        self._cor = cor
        self._ligado = False

    def __str__(self):
        return f'Modelo: {self._modelo} | Marca: {self._marca} | Cor: {self._cor}'

    def ligar(self):
        self._ligado = True