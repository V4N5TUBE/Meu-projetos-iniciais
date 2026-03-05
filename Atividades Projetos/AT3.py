def contar_vogais(texto):  
    vogais = "aeiou"  
    quantidade = 0  
 
    for letra in texto.lower():  
        if letra in vogais:  
            quantidade += 1  
 
    return quantidade  
 
texto = input("Digite um texto: ") 
 
print(f"O texto contém {contar_vogais(texto)} vogais.")

"""
quantidade = 0 linha 15: Essa variável vai guardar quantas vogais existem no texto.
Começa em 0 porque ainda não contamos nada.

for letra in texto.lower() linha 5:
Aqui acontece algo importante.

texto.lower()

Transforma todo o texto em letras minúsculas.

O FOR vai percorrer cada letra do texto.

Se a letra está dentro da variável vogais

Ou seja:

"a" está em "aeiou" ? sim
"p" está em "aeiou" ? não
"""




