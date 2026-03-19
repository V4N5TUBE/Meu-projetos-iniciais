# p.strip() Remove espaços extras
permissoes_principais = set(p.strip() for p in input("Permissões principais: ").lower().split(','))

# for p in :É um loop (for) que percorre cada pedaço do texto digitado
permissoes_solicitadas = set(p.strip() for p in input("Permissões solicitadas: ").lower().split(','))

# .issubset() verifica se tudo que está nas solicitadas está nas principais
eh_subconjunto = permissoes_solicitadas.issubset(permissoes_principais)

if eh_subconjunto:
    print("As permissões solicitadas fazem parte das permissões principais.")
else:
    print("As permissões solicitadas não fazem parte das permissões principais.")



"""Quando pedimos para o usuário digitar as permissões, ele pode inserir os valores de forma inconsistente,
com espaços extras, letras maiúsculas e minúsculas misturadas, ou até mesmo separadores errados. Se não tratarmos a entrada
corretamente, comparações podem falhar.

Para garantir que os dados estejam sempre no mesmo formato, utilizamos três funções principais:

    strip(): Remove espaços extras e cada permissão pode ter espaços antes ou depois da vírgula.

    lower(): Converte para letras minúsculas, assim, se o usuário digitar "EXECUÇÃO" e compararmos com "execução",
    a verificação pode falhar, pois Python diferencia maiúsculas e minúsculas.

    split(','): Divide a string em uma lista de elementos e transforma a entrada do usuário em uma lista separada por vírgula,
    permitindo criar um conjunto posteriormente.
"""