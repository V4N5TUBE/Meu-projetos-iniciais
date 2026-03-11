# 1) Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao.
# Inicie um atributo chamado disponivel como True por padrão.\
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo.title()
        self.autor = autor.title()
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

# 2) Na classe Livro, adicione um método especial __str__ que retorna uma mensagem formatada com o título, autor e 
# ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
    def __str__(self):
        return f"{self.titulo} | {self.autor} | {self.ano_publicacao}"
    
# 3) Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False.
# Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
    def emprestar_livro(self):
        self.disponivel = False
        
# 4) Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e
# retorna uma lista dos livros disponíveis publicados nesse ano.
    @staticmethod
    def verificar_disponibilidade(ano):
          livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
          return livros_disponiveis
        
Livro.livros = []# Adicionando os livros à lista de livros