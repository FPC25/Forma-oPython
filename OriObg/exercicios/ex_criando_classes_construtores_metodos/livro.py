class Livro:

    livros = []

    def __init__(self, titulo = '', autor = '', ano_publicacao = 0, disponivel = True):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = disponivel
        Livro.livros.append(self)


    def __str__(self):
        disponibilidade = 'disponivel' if self._disponivel else 'indisponivel'
        return  f'O livro "{self._titulo}" foi escrito por {self._autor} em {self._ano_publicacao} e está {disponibilidade} para emprestimo'
        
    
    def emprestar(self):
        self._disponivel = False

    def devolver(self):
        self._disponivel = True

    @staticmethod
    def verificar_disponibilidade(ano):
        correspondentes = [livro._titulo for livro in Livro.livros if livro._ano_publicacao == ano and livro._disponivel]
        print(correspondentes)
        correspondentes = []
        
