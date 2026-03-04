""" Faça um programa que solicite ao usuário o peso e a altura de um objeto, e calcule o Índice de Massa Corporal (IMC) do objeto. 
O IMC é calculado dividindo o peso pela altura ao quadrado (IMC = peso / altura^2). Com base no valor do IMC,
 o programa deve classificar o objeto como "Abaixo do peso", "Peso normal" ou "Acima do peso"""

peso = int(input("Digite o peso do objeto em kg: "))
altura = float(input("Digite a altura do objeto em metros: "))

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

if calcular_imc(peso, altura) < 18.5:
    print("Abaixo do peso")

elif calcular_imc(peso, altura) >= 18.5 and calcular_imc(peso, altura) < 25:
    print("Peso normal")

else:
    print("Acima do peso")