valor_total = float(input("Digite o valor da conta: "))
porcentagem_gorjeta = int(input("Digite a porcentagem de gorjeta: "))


def calcular_gorjeta(porcentagem_gorjeta, valor_total):
    gorjeta = (porcentagem_gorjeta / 100 ) * valor_total
    return gorjeta

def soma_total(valor_total):
    soma = valor_total + calcular_gorjeta(porcentagem_gorjeta, valor_total)
    return soma


print(f"Valor da gorjeta: {calcular_gorjeta(porcentagem_gorjeta, valor_total):.2f}")
print(f"Total a pagar: {soma_total(valor_total):.2f}")

"""oq eu fiz: criei duas funcoes para calcular porcentagem da gorjeta e dps calcular a somatoria do total da conta e a
porcentagem, o :.2f significa que na saida vai aparecert em float EX: 5,00  """

"""Aqui você está tentando somar:

valor_total (número)

calcular_gorjeta (a função, não o resultado dela)

Você precisa chamar a função passando os valores.

para isso coloque as variavel dentro do parenteses para ela saber qual dos intes para fazer a funcao
"""