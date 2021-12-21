notas = [0, 0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 0
while x < 8:
    notas[x] = float(input(f'Notas {x}: '))
    soma += notas[x]
    x += 1
x = 0
while x < 8:
    print(f'Nota {x}:{notas[x]:6.2f}')
    x += 1
print(f'Media:{soma / x:5.2f}')
