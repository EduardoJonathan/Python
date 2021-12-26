print("Qual operação deseja fazer?")
print("_" * 30)
print("1)Digite 1 para Somar\n2)Digite 2 para Subtrair\n3)Digite 3 para Multiplicar\n4)Digite 4 para Dividir")
print("_" * 30)
while True:
    choose = input('Digite um número do menu acima: ')
    if choose > '4':
        print('Desculpe! Insira um número que se encontra no menu')
        continue
    print("_" * 30)
    num0 = int(input("Insira o primeiro número: "))
    num1 = int(input("Insira o segundo número: "))
    result1 = num0 + num1
    result2 = num0 - num1
    result3 = num0 * num1
    result4 = num0 / num1
    if choose == '1':
        print(f'O resultado de {num0} + {num1} é = {result1}')
    elif choose == '2':
        print(f'O resultado de {num0} - {num1} é = {result2}')
    elif choose == '3':
        print(f'O resultado de {num0} * {num1} é = {result3}')
    elif choose == '4':
        print(f'O resultado de {num0} / {num1} é = {result4}')
    break
