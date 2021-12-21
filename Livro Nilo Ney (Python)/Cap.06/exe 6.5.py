ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print("\nExistem %d clientes na fila" % len(fila))
    print("Fila atual:", fila)
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operacao = input("Operação (F, A ou S):")
    x = 0
    sair = False
    while x < len(operacao):
        if operacao[x] == "A":
            if (len(fila)) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operacao[x] == "F":
            ultimo += 1
            fila.append(ultimo)
        elif operacao[x] == "S":
            sair = True
            break
        else:
            print("Operação inválida: %s na posição %d! Digite apenas F, A ou S!" % (operacao[x], x))
        x = x + 1
    if sair:
        break
