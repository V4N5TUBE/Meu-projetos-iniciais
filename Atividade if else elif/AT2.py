""" teste para calcular o tempo total gasto em atividades A, B e C, onde o usuário deve informar os dias para cada atividade.
O programa deve validar se os valores são positivos e, caso contrário, exibir uma mensagem de erro.
 """

at_a = int(input("Digite os dias para a atividade A: "))
at_b = int(input("Digite os dias para a atividade B: "))
at_c = int(input("Digite os dias para a atividade C: "))

if at_a < 0 or at_b < 0 or at_c < 0:
    print("Valor inválido. Digite um número positivo para os dias.")

else:
   tempo_total = at_a + at_b + at_c
   print(f"Tempo total de atividades: {tempo_total} dias")