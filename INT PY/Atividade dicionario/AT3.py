lista_ana = {"leite", "pão", "café", "açúcar"}

lista_laura = {"pão", "café", "biscoito", "chocolate"}

# .intersection() pega o que está nas duas listas
as_duas = lista_ana.intersection(lista_laura)

# .difference() pega o que está em Laura mas NÃO em Ana
laura = lista_laura.difference(lista_ana)
ana = lista_ana.difference(lista_laura)


# .join() transforma o conjunto em uma string separada por vírgula
print(f"Itens em ambas as listas: {', '.join(as_duas)} ")
print(f"Itens exclusivos de Laura: {', '.join(laura)} ")
print(f"Itens exclusivos de Ana: {', '.join(ana)} ")
