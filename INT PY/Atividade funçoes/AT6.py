numeros = input("Digite os números separados por espaço: ").split()

""""filter e imprimir apenas os elementos que se encaixa na funcao
lambda e tipo uma funcao so que ela e pra coisas pequena
e o int(x) e pegar o numero que o usuario fez e colocar em inteiro e dps fazer a equacao para ver os pares """
pares = filter(lambda x: int(x) % 2 == 0, numeros) 
    

print("Números pares:", " ".join(pares)) 