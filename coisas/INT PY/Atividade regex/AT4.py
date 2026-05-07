url = input("Digite a URL para validação: ")
"""PARA SER VÁLIDA, A URL DEVE COMEÇAR COM "https://" E TERMINAR COM ".com".""" 
if url.startswith("https://") and url.endswith(".com"):
    print("URL válida!")
else:
    print("URL inválida!")

# programa que peça ao usuário uma URL e informe se ela é válida ou inválida?