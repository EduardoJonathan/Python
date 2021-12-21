ultimo = 0
fila1 = []
fila2 = []
while True:
    print("\nExistem %d clientes na fila 1 e %d na fila 2." % (len(fila1), len(fila2)))
    print("Fila 1 atual:", fila1)
    print("Fila 2 autal:", fila2)
    print("Digite F para adicionar um cliente ao fim da fila 1 (ou G para fila 2),")
    print("ou A para realizar o atendimento a fila 1 (ou B para fila 2")
    print("S para sair.")
    operacao = input("Operação (F, G, A, B ou S):")
    x = 0
    sair = False
    while x < len(operacao):
        if operacao[x] != "A" and operacao[x] != "F":
            fila = fila2
        else:
            fila = fila1
        if operacao[x] == "A" or operacao[x] == "B":
            if (len(fila)) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido}atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operacao[x] == "F" or operacao[x] == "G":
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
