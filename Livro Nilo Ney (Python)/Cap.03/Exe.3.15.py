cigarros_por_dia = int(input("Quantos cigarros fuma por dia: "))
anos_fumando = float(input("Quantidade de anos que tem fumando: "))
redução_em_minutos = anos_fumando * 365 * cigarros_por_dia * 10
# Um dia tem 24 x 60 minutos
reducao_em_dias = redução_em_minutos / (24 * 60)
print(f"Redução do tempo de vida {reducao_em_dias:8.2f} dias.")