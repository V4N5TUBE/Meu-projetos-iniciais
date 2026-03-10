from DeliveryCo.Restaurante import Restaurante

ifood = Restaurante("bistro", "italiana")

ifood.receber_avaliacao("jonas", 10)
ifood.receber_avaliacao("japa", 6)
ifood.receber_avaliacao("jo", 4)

ifood.alternar_ativo()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
