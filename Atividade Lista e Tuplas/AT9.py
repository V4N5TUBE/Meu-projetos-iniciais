notas = input("Digite as notas dos alunos separadas por vírgula: ").split(", ")
#for é utilizado para converter os valores de entrada em números decimais
notas = [float(nota) for nota in notas]
#sum*() para determinar o total de elementos. len() para determinar o total de elementos.
media = sum(notas) / len(notas)
print(f"Média final da turma: {media:.2f}")

"""programa que receba as notas finais de todos os alunos e calcule a média da turma"""
