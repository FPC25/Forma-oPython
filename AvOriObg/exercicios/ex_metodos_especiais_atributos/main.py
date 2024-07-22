from carro import Carro

def main():
    carro1 = Carro('Corola', 'Toyota', 'vermelho')
    carro2 = Carro('Civic', 'Honda', 'Preto')
    carro3 = Carro('Clio', 'Renault', 'Prata')
    
    print(f'{carro1}\n{carro2}\n{carro3}\n')

if __name__ == '__main__':
    main()