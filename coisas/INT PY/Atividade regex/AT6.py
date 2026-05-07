import re

texto = input("Digite o texto a ser revisado: ")

palavra_substituida = input("Digite a palavra a ser substituída: ")

nova_palavra = input("Digite a nova palavra: ")

nova_frase = re.sub(rf"\b{palavra_substituida}\b", nova_palavra, texto)

print("Texto revisado:", nova_frase)


"""programa que solicite um texto, a palavra que será substituída e a nova palavra. O programa deve exibir o texto com as
alterações aplicadas."""