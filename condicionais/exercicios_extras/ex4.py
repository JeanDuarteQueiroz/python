assinatura = input("Informe o tipo de assinatura (B,S,G ou P) que possui:  ").upper();
fat_total = float(input("Informe o seu faturamento anual:  "));

if (assinatura) == "B":
    bonus = float(fat_total*0.3)
    print("Baseado na sua assinatura atual sobre o faturamento anual de {:.2f} O bônus que você deve pagar é: {:.2f}".format(fat_total, bonus));
elif (assinatura) == "S":
    bonus = float(fat_total*0.2)
    print("Baseado na sua assinatura atual sobre o faturamento anual de {:.2f} O bônus que você deve pagar é: {:.2f}".format(fat_total, bonus));
elif (assinatura) == "G":
    bonus = float(fat_total*0.1)
    print("Baseado na sua assinatura atual sobre o faturamento anual de {:.2f} O bônus que você deve pagar é: {:.2f}".format(fat_total, bonus));
elif (assinatura) == "P":
    bonus = float(fat_total*0.05)
    print("Baseado na sua assinatura atual sobre o faturamento anual de {:.2f} O bônus que você deve pagar é: {:.2f}".format(fat_total, bonus));
else: 
    print("Assinatura inválida!!");