# 5) Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
# 6) No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou 
# não após o empréstimo.

from AT3 import Livro

livro_biblioteca = Livro("Python in Practice", "Emily Coder", 2021)
print(f"Antes de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")
livro_biblioteca.emprestar_livro()
print(f"Depois de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")



# 7) No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de
#livros disponíveis publicados em um ano específico.
ano_especifico = 2020
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}")




# 8) Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e
# exiba a mensagem formatada utilizando o método __str__.
# Certifique-se de corrigir o nome do arquivo para o correto




livro_main1 = Livro("Python para Iniciantes", "Carlos Coder", 2021)
livro_main2 = Livro("Web Development Essentials", "Laura Developer", 2023)

print(livro_main1)
print(livro_main2)