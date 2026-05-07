from RESTAURANTE.Restaurante import Restaurante
from RESTAURANTE.cardapio.pratos import Prato
from RESTAURANTE.cardapio.bebidas import Bebida


ifood = Restaurante("bistro", "italiana")
bebida_refri = Bebida("guarana", 6.0,"KS")
bebida_refri.aplicar_desconto()
prato_cozinha = Prato("frango grelhado", 15.0,"completo")
prato_cozinha.aplicar_desconto()
ifood.adicionar_cardapio(bebida_refri)
ifood.adicionar_cardapio(prato_cozinha)

def main():
    ifood.exibir_cardapio

if __name__ == '__main__':
    main()