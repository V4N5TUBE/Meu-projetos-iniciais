import random
 
def adivinhar_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
 
    while True:
        try:
            palpite = int(input("Tente adivinhar o número (1-100): "))
 
            if not 1 <= palpite <= 100:
                raise ValueError("Número fora do intervalo! Digite um número entre 1 e 100.")
 
            tentativas += 1
 
            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break
 
        except ValueError as e:
            print(f"Entrada inválida: {e}")
 
adivinhar_numero()

"""1️⃣ Importando a biblioteca
import random

Aqui você importa a biblioteca random, que serve para gerar valores aleatórios.

2️⃣ Criando a função
def adivinhar_numero():

Aqui você cria uma função chamada adivinhar_numero.

Ela vai conter todo o jogo de adivinhar o número.

3️⃣ Gerando o número secreto
numero_secreto = random.randint(1, 100)

randint(1, 100) gera um número aleatório entre 1 e 100.

Exemplo:

57

Esse será o número que o jogador precisa descobrir.

4️⃣ Contador de tentativas
tentativas = 0

Essa variável vai guardar quantas vezes o usuário tentou.

5️⃣ Laço infinito
while True:

Esse while cria um loop que nunca para.

O programa só vai parar quando encontrar um break.

6️⃣ Tratamento de erro
try:

O try serve para tentar executar o código.

Se acontecer algum erro, o programa não quebra.

7️⃣ Usuário digita o palpite
palpite = int(input("Tente adivinhar o número (1-100): "))

Aqui:

1️⃣ o usuário digita um número
2️⃣ int() transforma em número inteiro

8️⃣ Verificação do intervalo
if not 1 <= palpite <= 100:

Isso verifica se o número está entre 1 e 100.

Se não estiver:

raise ValueError("Número fora do intervalo! Digite um número entre 1 e 100.")

raise força um erro para avisar o usuário.

9️⃣ Contando as tentativas
tentativas += 1

Isso significa:

tentativas = tentativas + 1

Cada tentativa aumenta +1.

🔟 Comparando o palpite
Se for menor
if palpite < numero_secreto:

Mostra:

Muito baixo! Tente novamente.
Se for maior
elif palpite > numero_secreto:

Mostra:

Muito alto! Tente novamente.
Se acertar
else:

Mostra:

print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")

Depois o jogo termina:

break
1️⃣1️⃣ Tratamento de erro
except ValueError as e:

Se o usuário digitar algo errado como:

abc
@
10.5

O programa não quebra.

Ele mostra:

Entrada inválida
1️⃣2️⃣ Executando a função
adivinhar_numero()

Aqui você chama a função, iniciando o jogo."""