class Carro:
    carros = []
    
    def __init__(self, ano, cor):
        self.ano = ano
        self.cor = cor 
        Carro.carros.append(self)
    

    def __str__(self):
        return f"{self.ano} | {self.cor}"

    def listar_carros():
        for cars in Carro.carros:
            print (f"ano: {cars.ano} | cor: {cars.cor}" )

tracker = Carro("2022", "branco")
song_pro = Carro("2026", "cinza escuro")

Carro.listar_carros()