quantidade_de_km = float(input('Quantos KM/H seu carro irá pecorrer: '))
dias = int(input('Está fazendo quantos dias que seu carro foi alugado: '))
preco_por_dia = 60
preco_por_km = 0.15
preco_a_pagar = quantidade_de_km * preco_por_km + dias * preco_por_dia
print(f"Total a pagar: R${preco_a_pagar:7.2f}")