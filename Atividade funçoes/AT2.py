"""usando a função len() para contar os caracteres de uma palavra """


palavra = input("Digite uma palavra: ")

def contar_caracteres(palavra):
    quantidade = len(palavra)
    return quantidade

quantidade_caracteres = contar_caracteres(palavra)

print (f"A palavra '{palavra}' tem {quantidade_caracteres} caracteres.")