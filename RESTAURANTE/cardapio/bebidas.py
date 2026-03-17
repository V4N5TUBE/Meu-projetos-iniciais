from RESTAURANTE.cardapio.itens_cardapio import Itemcardapio

class Bebida(Itemcardapio):
    def __init__(self,nome,preco,tamanho):
        super().__init__(nome,preco,)
        self.tamanho = tamanho

    def __str__ (self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)


"""herança. Ele se refere à capacidade de uma classe herdar características de uma classe base, mas também adicionar
vou modificar essas características conforme necessário.

A funcao __str__ serve para mostrar no print o nome em forma de string para que o computador leia

onde criaremos o método aplicar_desconto(). Receberemos o próprio objeto self, e o valor de self._preco será -= self._preco
multiplicando-o por 0.05. A utilização de parênteses nessa multiplicação visa maior clareza. O 0.05 representa o desconto que
estamos aplicando, subtraindo assim 5% do preço inicial.
"""