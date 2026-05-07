vendas = input("digite os valores das vendas: ").split()
"""o sum serve para somar tudo dentro da string e o map e pra passar pra cada um essa funcao
o split serve para colocar a string do usuario em uma lista para que ela se torne uma variavel """
total = sum(map(float, vendas))
print(f"o total da venda foi: {total}")
    