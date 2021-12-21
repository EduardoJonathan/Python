kwh = int(input("Informe o consumo de kWh: "))
tipo_instalação = input("Informe o tipo de instação. (R: Residências, I: Indústrias e C: Comércios:")

if tipo_instalação == 'R':
    if kwh <= 500:
        valor_fatura = kwh * 0.40
    else:
        valor_fatura = kwh * 0.65

elif tipo_instalação == 'C':
    if kwh <= 1000:
        valor_fatura = kwh * 0.55
    else:
        valor_fatura = kwh * 0.60

elif tipo_instalação =='I':
    if kwh <= 5000:
        valor_fatura = kwh * 0.55
    else:
        valor_fatura = kwh * 0.60
else:
    print ("O tipo de instalação informado está incorreto!")

print (f"O valor da fatura de é: R$ {valor_fatura:6.2f}.")