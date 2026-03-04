quantidade = float(input("Quantidade de itens:" ))
valor = float(input("Valor do item: "))
cadastro = input("E cadastrado? (s/n): ").lower

print("Valor total: R$", quantidade * valor)

if cadastro == "s":
    print("Desconto de 10%: R$", (quantidade * valor) * 0.1)
    print("Valor a pagar: R$", (quantidade * valor) - ((quantidade * valor) * 0.1))

elif cadastro == "n":
    print("Valor a pagar: R$", quantidade * valor)