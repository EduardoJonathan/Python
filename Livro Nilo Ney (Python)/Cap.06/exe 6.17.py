estoques = {'Tomate': [1000, 2.30],
            'Alface': [500, 0.45],
            'Batata': [2001, 1.20],
            'Feijão': [100, 1.50],
            }
venda = [['Tomate', 5], ['Batata', 10], ['Alface', 5]]
total = 0
print("venda:")
while True:
    produtos = str(input("Produto:\n"))
    if produtos in estoques:
        quantidade = int(input("Quantidade Vendida do produto: "))
        if quantidade <= estoques[produtos][0]:
            preco = estoques[produtos][1]
            custo = preco * quantidade
            print(f'{produtos:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}')
            estoques[produtos][0] -= quantidade
            total += custo
        else:
            print('Quantidade não disponivel')
    print(f'Custo total: {total:21.2f}\n')
    print("Estoque:\n")
    for chave, dados in estoques.items():
        print("Descrição: ", chave)
        print("Quantidade: ", dados[0])
        print(f'Preço: {dados[1]:6.2f}\n')
