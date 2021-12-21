distancia = float(input('Qual distancia a pecorrer: '))
preco = distancia * 0.50
preco1 = distancia * 0.45
if distancia <= 200:
    print(preco)
elif distancia > 200:
    print(preco1)
