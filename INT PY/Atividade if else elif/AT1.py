''' teste de if else elif para comparar a quantidade de maçãs e bananas e a igualdade entre elas.'''

qt_maca = int(input("Digite a quantidade de maçãs: "))
qt_banana = int(input("Digite a quantidade de bananas: "))

if qt_maca > qt_banana:
    print("A quantidade de maçãs é maior que a quantidade de bananas.")

elif qt_maca < qt_banana:
    print("A quantidade de bananas é maior que a quantidade de maçãs.")

else:
    print("A quantidade de maçãs é igual a quantidade de bananas.")