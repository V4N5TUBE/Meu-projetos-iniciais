from RESTAURANTE.cardapio.itens_cardapio import Itemcardapio

class Prato(Itemcardapio):
    def __init__(self,nome,preco,descricao):
        super().__init__(nome,preco)
        self.descricao = descricao

    def __str__ (self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)


"""
1-a primeira coisa que precisamos fazer para indicar que ela herda informações e atributos da classe ItemCardapio é importá-la.
Nós podemos usar o comando import

2-Para indicar que o prato é uma subclasse do ItemCardapio, escrevemos class Prato(ItemCardapio):. Com essa linha,
estamos dizendo que a classe Prato herda métodos e atributos de outra classe. Assim, dentro da classe Prato,
teremos informações que podemos usar e ações que podemos realizar que são oriundas de outra classe.

Para usar essas informações, vamos substituir pass por super().__init__(nome, preco)
A classe Prato está usando as informações e os atributos da classe ItemCardapio. Sempre que utilizamos a palavra super,
estamos acessando informações de outra classe, nesse caso, da classe ItemCardapio.

3-o atributo self.descrição e atribuir a ele o valor de descrição que estamos passando.
Não somos obrigados a ficar apenas com aquelas informações do ItemCardapio.



"""