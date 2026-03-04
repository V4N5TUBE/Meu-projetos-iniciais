# Função para converter moeda

def converter_moeda(valor, taxa_cambio):
    return valor * taxa_cambio
taxa_cambio = 5.25  # Exemplo de taxa de câmbio

# Entrada do usuário
valor = float(input("Digite o valor a ser convertido: "))

#saida
valor_convertido = converter_moeda(valor, taxa_cambio)
print(f"O valor convertido é: {valor_convertido:.2f}")