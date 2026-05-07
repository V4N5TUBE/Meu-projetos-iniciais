despesas = float(input("Digite o valor das despesas: "))
teto_gasto = 3000

if despesas > teto_gasto:
    print("Alerta: despesas acima do teto permitido.")

else:
    print("Despesas dentro do teto permitido.")