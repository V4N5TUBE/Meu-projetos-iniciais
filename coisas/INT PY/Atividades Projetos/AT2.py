def validar_cpf(cpf):
    if not cpf.isdigit():
        return "Erro: O CPF deve conter apenas números."
    if len(cpf) != 11:
        return "Erro: O CPF deve ter exatamente 11 dígitos."
    return "CPF válido."

cpf = input("Digite seu CPF: ")
print(validar_cpf(cpf))
 
"""essa parte do if not quer dizer:Se não for composto apenas por números. isdigit serve para verificar se a string
tem apenas números. """

"""o len e usado para ler cada caracter da frase e o != Ele é usado para comparar dois valores e verificar se eles 
 não são iguais.a que no caso e o 11"""
    