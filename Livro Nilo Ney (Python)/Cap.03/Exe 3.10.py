salario = float(input("Digite o salário atual: "))
porcentagem_aumento = float(input("Digite a porcentagem de aumento: "))
aumento = salario * porcentagem_aumento / 100
novo_salario = salario + aumento
print(f"Um aumento de {porcentagem_aumento:5.2f} em um salário de R$ {salario:7.2f}")
print(f"é igual a um aumento de R$ {aumento:7.2f}")
print(f"Resultando em um novo salário de R$ {novo_salario:7.2f}")