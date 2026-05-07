import re

texto = input("Digite o título dos livro: ") 
letra = input("Digite a letra inicial para pesquisa: ")  
palavras = re.findall(rf'\b{letra}[a-zà-ÿ]*', texto, re.IGNORECASE)
print(palavras)


# programa que solicita um texto e uma letra inicial e retorna todas as palavras do texto que começam com essa letra?


"""re.findall:serve para encontrar todas as palavras no texto
[a-zà-ÿ]* → zero ou mais letras minúsculas, incluindo acentos"""