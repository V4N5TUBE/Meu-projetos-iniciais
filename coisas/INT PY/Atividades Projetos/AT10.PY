def caixa_eletronico(): 
    cedulas = [100, 50, 20, 10, 5, 2] 
 
    try: 
        valor = int(input("Digite o valor do saque: ")) 
 
        if valor <= 0: 
            print("Erro: O valor deve ser positivo.")
        elif valor % 2 != 0: 
            print("Erro: O valor deve ser múltiplo de 2.")
        else: 
            print("Cédulas entregues:")
            
            for cedula in cedulas: 
                quantidade = valor // cedula
                if quantidade > 0:
                    print(f"{quantidade} cédulas de R$ {cedula}")
                    valor = valor % cedula 
 
    except ValueError: 
        print("Erro: Digite um valor numérico válido.") 
 
caixa_eletronico()

"""1️⃣ Criação da função
def caixa_eletronico():

Aqui você cria uma função chamada caixa_eletronico.

Essa função simula um caixa eletrônico que entrega cédulas quando alguém faz um saque.

2️⃣ Lista de cédulas disponíveis
cedulas = [100, 50, 20, 10, 5, 2]

Aqui você cria uma lista com os valores das notas disponíveis no caixa.

Ou seja, o caixa pode entregar:

R$100

R$50

R$20

R$10

R$5

R$2

A lista começa da maior para a menor para facilitar o cálculo.

3️⃣ Tratamento de erro
try:

O try serve para tentar executar o código.

Se o usuário digitar algo errado, o programa não quebra.

4️⃣ Usuário digita o valor
valor = int(input("Digite o valor do saque: "))

Aqui:

o usuário digita o valor

int() transforma em número inteiro

Exemplo:

186
5️⃣ Verificando se o valor é válido
Se o valor for negativo ou zero
if valor <= 0:

Mostra erro:

Erro: O valor deve ser positivo.
Se o valor for ímpar
elif valor % 2 != 0:

O operador % é resto da divisão.

Exemplo:

7 % 2 = 1

Se o resto não for 0, significa que não é divisível por 2.

Então aparece:

Erro: O valor deve ser múltiplo de 2.

Isso acontece porque não existe nota de R$1.

6️⃣ Se o valor for válido
else:
    print("Cédulas entregues:")

O programa começa a calcular quais notas entregar.

7️⃣ Percorrendo as cédulas
for cedula in cedulas:

O for vai passar por cada valor da lista:

100
50
20
10
5
2
8️⃣ Calculando quantas notas
quantidade = valor // cedula

// é divisão inteira.

Exemplo:

186 // 100 = 1

Significa:

1 nota de 100
9️⃣ Verificando se precisa daquela nota
if quantidade > 0:

Se a quantidade for maior que 0, significa que precisamos entregar aquela nota.

🔟 Mostrando as cédulas
print(f"{quantidade} cédulas de R$ {cedula}")

Exemplo:

1 cédula de R$100
1 cédula de R$50
1 cédula de R$20
1 cédula de R$10
1 cédula de R$5
1️⃣1️⃣ Atualizando o valor restante
valor = valor % cedula

Aqui o programa pega o resto que ainda falta pagar.

Exemplo:

186 % 100 = 86

Agora ele continua calculando com 86.

1️⃣2️⃣ Tratamento de erro
except ValueError:

Se o usuário digitar algo como:

abc
@
10.5

O programa mostra:

Erro: Digite um valor numérico válido.
1️⃣3️⃣ Executando a função
caixa_eletronico()

Aqui você chama a função, iniciando o programa.

🧠 Exemplo completo

Usuário digita:

186

Saída:

Cédulas entregues:
1 cédulas de R$ 100
1 cédulas de R$ 50
1 cédulas de R$ 20
1 cédulas de R$ 10
1 cédulas de R$ 5
1 cédulas de R$ 1

(no seu código a última seria 2 dependendo do cálculo)"""

