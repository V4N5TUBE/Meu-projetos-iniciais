nomes = ["PM3", "Alura", "Latam", "Outros"]

for nome in nomes:
   if nome == "Alura":
       print("Ignorando Alura.")
       continue
   print(f"Nome: {nome}")
