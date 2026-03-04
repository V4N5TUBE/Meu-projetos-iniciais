desconto = int(input("Digite a porcentagem de desconto: "))
valor_compra = int(input("Digite o valor da compra: "))

def criar_desconto(porcentagem):  

   def calcular_preco(valor_compra):  

       return valor_compra - (valor_compra * (porcentagem / 100))  

   return calcular_preco 

calcular_preco_final = criar_desconto(desconto)

print(f"Preço final com desconto: {calcular_preco_final(valor_compra)}") 