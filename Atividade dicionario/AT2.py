#.split() Divide a frase em palavras (lista)
texto1 = set(input("Texto 1: ").lower().split()) 
# set(...) Transforma em conjunto (remove repetidos)
texto2 = set(input("Texto 2: ").lower().split()) 

# Aqui acontece a parte principal .intersection() pega os elementos que estão nos dois conjuntos
comuns = texto1.intersection(texto2) 

print(f"Palavras em comum: {comuns}") 
