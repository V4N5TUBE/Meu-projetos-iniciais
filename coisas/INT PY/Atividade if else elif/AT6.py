hr_atual = float(input("Digite a hora atual (24h): "))

if 8 <= hr_atual <= 18:
    print("Permitido")
else:
    print("Não permitido")