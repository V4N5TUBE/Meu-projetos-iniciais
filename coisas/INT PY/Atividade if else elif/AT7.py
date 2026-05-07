nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

def calcular_media(nota_1, nota_2, nota_3):
    media = (nota_1 + nota_2 + nota_3) / 3
    return media

if calcular_media(nota_1, nota_2, nota_3) >= 7:
    print("Aprovado")
elif calcular_media(nota_1, nota_2, nota_3) >= 5 and calcular_media(nota_1, nota_2, nota_3) < 7:
    print("Recuperação")
elif calcular_media(nota_1, nota_2, nota_3) < 5:
    print("Reprovado")
    