renda_mensal = float(input("Digite a renda mensal: "))
parcela_desejada = float(input("Digite o valor da parcela desejada: "))


if renda_mensal > 2000 and parcela_desejada <= 0.3 * renda_mensal:
    print("Empréstimo aprovado.")
elif renda_mensal <= 2000:
    print("Empréstimo negado: renda mensal insuficiente.")

else:
    print("Empréstimo negado: parcela desejada excede 30% da renda mensal.")