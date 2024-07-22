from carro import Carro
from moto import Moto


def main():
    carro1 = Carro('Renault', 'Clio', 4)
    carro2 = Carro('Chevrolet', 'Corsa', 2)
    carro3 = Carro('Honda', 'Civic', 4)
    
    moto1 = Moto('Honda', 'CG 160', 'Casual')
    moto2 = Moto('Honda', 'Biz', 'Casual')
    moto3 = Moto('Yamaha', 'YZF R-3', 'Esportiva')

    print(f'{carro1} \n {carro2} \n {carro3}\n')
    print(f'{moto1} \n {moto2} \n {moto3}\n')

if __name__ == '__main__':
    main()