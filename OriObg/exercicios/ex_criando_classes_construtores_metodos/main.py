from livro import Livro


def main():

    livro1 = Livro('O fim da infância', 'Arthur C. Clarke', 1953)
    livro2 = Livro('2001: Uma odisséia no espaço', 'Arthur C. Clarke', 1951)
    livro3 = Livro('Fahrenheit 451', 'Ray Bradbury', 1953)

    Livro.verificar_disponibilidade(1951)
    livro1.emprestar()
    print(livro1)

    Livro.verificar_disponibilidade(1953)

if __name__ == '__main__':
    main()