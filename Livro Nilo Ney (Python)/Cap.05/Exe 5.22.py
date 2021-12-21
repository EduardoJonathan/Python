while True:
    print("Menu\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisãoo \n5 - Sair")
    opção = int(input("Escolha uma opção do menu: "))
    if opção == 5:
        break
    elif opção >=1 and opção <5:
        n = int(input("Qual a tabuada para o programa operar: "))
        x = 1
        while x <= 10:
            if opção == 1:
                print(f"{n} + {x} = {n + x}")
            elif opção == 2:
                print(f"{n} - {x} = {n - x}" % (n, x, n - x))
            elif opção == 3:
                print(f"{n} / {x} = {n * x}" % (n, x, n / x))
            elif opção == 4:
                print(f"{n} x {x} = {n / x:5.4f}")
            x= x + 1
    else:
        print("Opção inválida!")
