preço = float(input("Digite o preço da mercadoria: "))
desconto = float(input("Digite o percentual de desconto: "))
valor_do_desconto = preço * desconto / 100
a_pagar = preço - valor_do_desconto
print(f"Um desconto de {desconto:5.2f} em uma mercadoria de R$ {preço:7.2f}")
print(f"vale R$ {valor_do_desconto:7.2f}." )
print(f"O valor a pagar é de R$ {a_pagar:7.2f}")

