valor_da_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salário: "))
quantidade_anos = int(input("Quantos anos para pagar: "))
meses = quantidade_anos * 12
prestacao = valor_da_casa / meses
if prestacao > salario * 0.3:
    print("Infelizmente você não pode obter o empréstimo")
else:
    print(f"Valor da prestação: R$ %{prestacao:7.2f} empréstimo OK")