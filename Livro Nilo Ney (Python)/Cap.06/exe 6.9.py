L = [15, 7, 27, 39]
p = int(input('Digite o valor a procurar: '))
v = int(input('Digite outro valor: '))
P = False
V = False
x = 0
y = 0
while x < len(L):
    if L[x] == p:
        P = True
    elif not V:
        y = 1
        if L[x] == v:
            V = True
        elif not P:
            y = 2
        x += 1
    if P:
        print(f'p: {p} Encontrado')
    else:
        print(f'p: {p} Não encontrado')
    if V:
        print(f'v: {v} Encontrado')
    else:
        print(f'v: {v} Não encontrado')
    if y == 1:
        print(f'{p} foi achado antes do {v}')
    else:
        print(f'{v} foi encontrado antes do {p}')
    break
