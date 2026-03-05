texto = input("Digite um texto: ")

palavras_longas = []

for letras in texto.split():
    if len(letras) > 10:
        palavras_longas.append(letras)

if palavras_longas:
    print("Palavras longas encontradas: ")
    for letras in palavras_longas:
        print(letras)
else:
    print("Nenhuma palavra longa foi encontrada no texto.")

"""Aqui criamos uma lista vazia chamada palavras_longas.Essa lista vai guardar as palavras que têm mais de 10 letras.

for letras in texto.split():
O split() separa o texto em palavras.
EX: ["ola", "mundo", "python"]

O for vai passar por cada palavra da lista.

if len(letras) > 10:
len() → conta quantas letras a palavra tem

> 10 → verifica se tem mais de 10 letras

palavras_longas.append(letras)

append() significa adicionar algo na lista.

Então se a palavra tiver mais de 10 letras, ela é adicionada na lista.

if palavras_longas:
    
Isso significa:
 Se a lista não estiver vazia
Ou seja, se encontrou alguma palavra longa.
print("Palavras longas encontradas:")

Depois ele percorre a lista:
for palavra in palavras_longas:
    print(palavra)

E imprime cada palavra.
"""