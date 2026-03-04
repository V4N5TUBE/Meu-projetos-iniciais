""" usando a funcao"""


ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o ano de nascimento: "))


def calcular_idade(ano_atual, ano_nascimento):
    idade = ano_atual - ano_nascimento
    return idade

idade = calcular_idade(ano_atual, ano_nascimento)

print (f"Sua idade: {idade} anos")