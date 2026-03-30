distancia = float(input("Digite a distância percorrida (km): "))


if distancia <= 100:
    print("Valor da passagem: R$ 10,00")

elif 100 < distancia <= 200:
    print("Valor da passagem: R$ 20,00")

else:
    print("Valor da passagem: R$ 30,00")