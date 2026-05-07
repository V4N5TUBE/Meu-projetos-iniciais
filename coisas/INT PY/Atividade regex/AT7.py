import re

nome = input("Digite o nome do cliente para validação: ")  
if re.fullmatch(r'[A-Z][a-z]*', nome):
    print("Nome válido!")
else:
    print("Nome inválido!")


"""programa que solicite um nome ao usuário e verifique se ele atende às regras.
As regras para um nome válido são:
- Deve começar com uma letra maiúscula.
- Deve ser seguido por letras minúsculas.
- Não deve conter números ou caracteres especiais.
- Nao pode ter numeros"""