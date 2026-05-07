import re

texto = input("Digite a descrição da receita: ")  
numero = re.findall(r'\d+', texto)[0]  
print(f"O número da receita é: {numero}")


# programa que receba um texto com uma descrição e exiba uma mensagem com o número encontrado.

# é uma regex (expressão regular) usada para encontrar números em um texto.