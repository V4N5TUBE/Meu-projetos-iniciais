import random

lista_opcoes = ["pedra", "papel", "tesoura"]

escolha_usuario = input(f"Escolha pedra, papel ou tesoura? ").lower()
escolha_computador = random.choice(lista_opcoes)

if escolha_usuario in lista_opcoes:
    print(f"Computador escolheu: {escolha_computador}")

    if escolha_usuario == escolha_computador:
        print("Empate!")
    elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
         (escolha_usuario == "papel" and escolha_computador == "pedra") or \
         (escolha_usuario == "tesoura" and escolha_computador == "papel"):
        print("Você venceu!")
    else:
        print("Você perdeu!")
else:
    print("Opção inválida")
    

