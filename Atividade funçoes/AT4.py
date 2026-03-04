
def converter_telefones(lista):  

   return [int(telefone) for telefone in lista] 

def verifica_tipos(lista):  

   for num in lista:  

       if not isinstance(num, int):  

           return "Erro na conversão."  

   return "Todos os números foram convertidos corretamente!" 

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

telefones_convertidos = converter_telefones(telefones) 

print(verifica_tipos(telefones_convertidos)) 


"""aparentemente essa parte do for e in e que o python ja entende que lista e que no caso e o telefones e asimila os valores 
   dentro da lista e na parte do int(telefone) apos pegar a lista e passar pra variavel telefone ele passa os numeros dentro dela
   para inteiro"""