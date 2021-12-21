dias = int(input("Quantidade de Dias: "))
horas = int(input("Quantidade de Horas: "))
minutos = int(input("Quantidade de Minutos: "))
segundos = int(input("Quantidade de Segundos: "))

total_em_segundos = (dias * 24 * 3600) + (horas * 3600) + (minutos * 60) + segundos
print(f"Convertido em segundos é igual a {total_em_segundos} segundos." )