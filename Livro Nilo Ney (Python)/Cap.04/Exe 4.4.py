salario = float(input("Insira um salario: "))
if salario >= 1250:
    porc = salario * 1.10
    print(f'O seu salario de {salario} teve um aumento de {porc:7.2f}')
else:
    porc1 = salario * 1.15
    print(f'O seu salario de {salario} teve um aumento de {porc1:7.2f}')
