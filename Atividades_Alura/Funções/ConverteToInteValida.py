def converteToInt (dados):
    if type(dados) == str:
       return int(dados);
    elif type(dados) == list: 
        return [int(dado) for dado in dados];
    else:
        return("Não deu certo sua conversão, bobinho!");
    
def validaInt (dados):
    if type(dados) == list:
        for x in dados:
            #if type(x) == int:
            if not isinstance (x, int):
                return "Não deu certo sua converção, bobinho!"
            else:
                return "Todos os números foram convertidos corretamente!";    
    elif type(dados) != int:
        return "Não deu certo sua conversão, bobinho!"     
    else:
        return "Todos os números foram convertidos corretamente!";
    

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]
print(f"Vamo testa o bagulho... {validaInt(converteToInt(telefones))}") 