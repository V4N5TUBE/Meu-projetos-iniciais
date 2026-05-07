class Pessoa:
    Pessoas = []

    def __init__(self, nome="", idade= 0, profissao= ""):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.Pessoas.append(self)

        def __str__(self):
            return f"nome: {self.nome} - idade: {self.idade} - profissao: {self.profissao}"

        @property
        def saudacao(self):
            return f"Parabens pela trabalho de {self.profissao}"
        
        def aniversario(self):
            self.idade += 1


    pessoa1 = Pessoas(nome='Alice', idade=25, profissao='Engenheira')
    
    """depois eu tento solucionar"""