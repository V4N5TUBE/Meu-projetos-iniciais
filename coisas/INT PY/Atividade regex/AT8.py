import re

cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")  
padrao = r'\d{3}\.\d{3}\.\d{3}-\d{2}'

if re.search(padrao, cpf):
    print("O CPF está no formato correto.")
else:
    print("O CPF está no formato incorreto.")

# programa que solicite o CPF de um cliente e verifica se ele está no formato correto. 
