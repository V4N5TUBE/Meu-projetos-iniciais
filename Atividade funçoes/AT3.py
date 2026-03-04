horario = input("Digite o horário (formato 0-23): ")

def horario_saudacao(hora):
        if 0 <= hora < 12:
            return f"Bom dia!"
        elif 12 <= hora < 18:
            return f"Boa tarde!"
        elif 18 <= hora < 23:
            return f"Boa noite!"
        
print(f"{horario_saudacao(int(horario))}")