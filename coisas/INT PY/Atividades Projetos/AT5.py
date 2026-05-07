import random
 
def gerar_senha():
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    especiais = "!@#$%&*"
 
    senha = [
        random.choice(maiusculas),
        random.choice(minusculas),
        random.choice(numeros),     
        random.choice(especiais)    
    ]
 
    todos_caracteres = maiusculas + minusculas + numeros + especiais
    senha.extend(random.choices(todos_caracteres, k=8))
    random.shuffle(senha)
    return ''.join(senha)
 
print(f"Senha gerada: {gerar_senha()}")

"""Importação da biblioteca

import random

Aqui você está importando a biblioteca random, que serve para gerar valores aleatórios.
Ela permite coisas como:

escolher letras aleatórias
embaralhar listas
gerar números aleatórios

2️⃣ Criando a função

def gerar_senha():

Aqui você criou uma função chamada gerar_senha.
Ela será responsável por criar uma senha aleatória.

3️⃣ Definindo os tipos de caracteres
maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
especiais = "!@#$%&*"

Aqui você criou 4 grupos de caracteres:

Variável	Tipo
maiusculas	letras maiúsculas
minusculas	letras minúsculas
numeros	    números
especiais	símbolos


4️⃣ Começando a criar a senha

senha = [
    random.choice(maiusculas),
    random.choice(minusculas),
    random.choice(numeros),
    random.choice(especiais)
]

Aqui o programa cria uma lista chamada senha.

Ele escolhe 1 caractere aleatório de cada grupo usando:

random.choice()

Isso garante que a senha terá pelo menos:

1 letra maiúscula

1 letra minúscula

1 número

1 símbolo

Exemplo inicial:

['A', 'k', '5', '@']

5️⃣ Juntando todos os caracteres

todos_caracteres = maiusculas + minusculas + numeros + especiais

Aqui ele junta todos os tipos de caracteres em uma única string.

Exemplo:

ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&*

6️⃣ Adicionando mais caracteres

senha.extend(random.choices(todos_caracteres, k=8))
random.choices()

Escolhe vários caracteres aleatórios.

k=8 → escolhe 8 caracteres

extend()

Adiciona esses caracteres na lista.

Agora a senha terá:

4 caracteres iniciais + 8 aleatórios = 12 caracteres

7️⃣ Embaralhando a senha

random.shuffle(senha)

Aqui o programa mistura a ordem da lista.

Exemplo antes:

['A', 'k', '5', '@', 'b', '9', 'F', '2', '&', 'p', 'M', '1']

Depois de embaralhar:

['9', 'A', 'p', '&', '1', 'k', 'F', '@', 'M', '2', 'b', '5']

8️⃣ Transformando a lista em texto

return ''.join(senha)

join() junta todos os caracteres da lista em uma única string.

Exemplo:

9Ap&1kF@M2b5

9️⃣ Mostrando a senha

print(f"Senha gerada: {gerar_senha()}")

Aqui o programa:

1️⃣ chama a função gerar_senha()
2️⃣ gera a senha
3️⃣ imprime na tela

Exemplo de saída:

Senha gerada: 9Ap&1kF@M2b5"""
