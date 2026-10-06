# 

min = int(input("Digite os minutos atuais da máquina:  "));y = 1;
resultado = 1;
for x in range (2,min+1,1):
    resultado = resultado * x;
print(f"A senha é LIBERDADE{resultado}");