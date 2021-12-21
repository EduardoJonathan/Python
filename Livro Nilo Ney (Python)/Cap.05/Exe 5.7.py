n = int(input("Qual a tabuada para o programar operar: "))
inicio = int(input("Defina o número Inicial da tabuada: "))
fim = int(input("Defina o número final da tabuada: "))
x = inicio
while x <= fim:
    print(f"{n} x {x} = {n * x}")
    x = x + 1