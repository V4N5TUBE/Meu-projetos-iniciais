import re

dados = input("Digite o nome completo e o ano de nascimento do paciente: ")  
padrao = r'(\w+) (\w+) - (\d{4})'  

resultado = re.search(padrao, dados)

if resultado:
    primeiro_nome = resultado.group(1)
    sobrenome = resultado.group(2)
    ano_nascimento = resultado.group(3)

    print(f"Primeiro Nome: {primeiro_nome}")
    print(f"Sobrenome: {sobrenome}")
    print(f"Ano de Nascimento: {ano_nascimento}")
else:
    print("Formato inválido!")



# programa que solicite o nome completo e o ano de nascimento de um paciente e exiba-os separadamente.

"""padrao = r'(\w+) (\w+) - (\d{4})'": serve para capturar partes específicas de um texto estruturado, usando grupos.
(\w+) → primeira palavra (letras, números ou _)
espaço → " " (literal)
(\w+) → segunda palavra
espaço + - + espaço → " - " (literal)
(\d{4}) → um número com 4 dígitos (geralmente um ano)


.group() → pega partes específicas da regex"""
