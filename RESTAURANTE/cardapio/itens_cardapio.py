from abc import ABC, abstractmethod

class Itemcardapio(ABC):
    def __init__(self,nome,preco):
        self._nome = nome
        self._preco = preco
    
    @abstractmethod
    def aplicar_desconto(self):
        pass


    
"""Para dizer que uma classe é uma classe abstrata, vamos importar de um pacote chamado ABC. Podemos colocar na primeira linha:
from abc import ABC, abstractmethod. """    