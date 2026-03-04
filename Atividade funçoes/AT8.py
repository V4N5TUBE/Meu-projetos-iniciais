x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
operador_matematico = (input("Escolha a operação (| + | - | * | / |): "))

soma = lambda x,y: x + y

subtrair = lambda x,y: x - y

multiplicar = lambda x,y: x * y

dividir = lambda x,y: x / y if y != 0 else "Erro: Divisão por zero"


if operador_matematico == "+":
    print(f"o resultado da equacao e: {soma(x,y)}")

elif operador_matematico == "-":
    print(f"o resultado da equacao e: {subtrair(x,y)}")

elif operador_matematico == "*":
    print(f"o resultado da equacao e: {multiplicar(x,y)}")

elif operador_matematico == "/":
    print(f"o resultado da equacao e: {dividir(x,y)}")

else:
    print("operacao iinvalida")

"""essa parte de puxar denovo o x e y e para que puxe os valores, la em cima nas funcoes ele fala apenas onde vai pegar e 
nao realmente vai puxar"""