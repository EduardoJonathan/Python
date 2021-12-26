def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    return x / y

while True:
    x = int(input('Insira um número: '))
    print('_' * 30)

    y = int(input('Insira outro número: '))
    print('_' * 30)

    print(f'O resultado dos número {x} + {y} é: ', somar(x, y))
    print('_' * 45)
    print(f'O resultado dos número {x} - {y} é: ', subtrair(x, y))
    print('_' * 45)
    print(f'O resultado dos número {x} x {y} é: ', multiplicar(x, y))
    print('_' * 45)
    print(f'O resultado dos número {x} / {y} é: ', dividir(x, y))
    print('_' * 45)
    print("Deseja Continuar Digite?\n 1-Para Sim\n 0-para Não")
    choose = int(input("Digite o que Deseja: "))
    if choose == 1:
        print('_' * 30)
        continue
    elif choose > 1:
        break
    elif choose == '0':
        break
print('FIM DO PROGRAMA')
