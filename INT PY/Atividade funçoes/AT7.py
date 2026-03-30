produtos = input("Digite os produtos separados por vírgula: ").split(",") 

precos = input("Digite os preços separados por vírgula: ").split(",") 
 
for produto, preco in zip(produtos, precos): 
    print(f"{produto.strip()}: {preco.strip()}") 

"""
.split(",") → transforma texto em lista

zip() → junta duas listas

for produto, preco → desempacota dois valores ao mesmo tempo

.strip() → remove espaços extras

f"" → formatação de texto


na linha 5: Aqui temos duas variáveis ao mesmo tempo:

produto

preco

Isso acontece porque o zip() entrega pares.
"""