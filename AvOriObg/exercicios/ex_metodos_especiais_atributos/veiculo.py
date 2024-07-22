from abc import ABC, abstractmethod

class Veiculo(ABC):

    def __init__(self, modelo, marca):
        self._modelo = modelo.title()
        self._marca = marca.title()

    @abstractmethod
    def ligar(self):
        pass