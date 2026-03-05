frase = input("Digite uma frase: ")
palavras = frase.split()
print(len(palavras))
print(palavras)

def contar_palavras(frase):
    palavras = frase.split()
    print(palavras)
    return len(palavras)

def limpar_texto(texto):
    texto = texto.lower()
    caracteres = ".,!?:;\"'()[]{}"
    for char in caracteres:
        texto = texto.replace(char, "")
    return texto
""" a funcao .lower serve pra colocar as palavras em minusculo, depois foi criado um variavel chamado caracteres para desconsiderar,
para cada caracteres que foi colocado na string carateres seja removido para vazio = como foi mostrado na linha de codigo 15,
a funcao .replace serve para substituir, neste caso ele vai substituir os caracteres indesejados por nada. para fazer isso e so 
colocar entre aspas um vazio"""

def contar_palavras(frase):
    frase = limpar_texto(frase)
    palavras = frase.split()
    return len(palavras)

def contar_palavras(frase):
    frase = limpar_texto(frase)
    if not frase.strip():
        return {}
    
    palavras = frase.split()
    contagem = {}
    
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    
    return contagem
""""Primeiro, a função limpa a frase para remover coisas desnecessárias. Depois disso, ela verifica se ainda existe algum texto válido.
Se a frase estiver vazia ou só tiver espaços, a função retorna um dicionário vazio, porque não há palavras para contar.

Se houver texto, a frase é separada em várias palavras usando split(), transformando a frase em uma lista de palavras.

Depois, o programa cria um dicionário para fazer a contagem. Nesse dicionário:

--A chave será a palavra

--O valor será quantas vezes essa palavra aparece

Em seguida, um laço for percorre cada palavra da lista.

--Se a palavra já estiver no dicionário, o programa aumenta a contagem em +1.

--Se a palavra ainda não existir, o programa cria a palavra no dicionário e começa a contagem com 1.

No final, a função retorna o dicionário com todas as palavras e suas quantidades na frase."""


