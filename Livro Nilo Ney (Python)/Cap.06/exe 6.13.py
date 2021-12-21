T = [-10, -8, 0, 1, 2, 5, -2, -4]
maxima = T[0]
minima = T[0]
soma = 0
for i in T:
    if i > maxima:
        maxima = i
    elif i < minima:
        minima = i
    soma = soma + (i / len(T))
print(f'Temperatura maior: {maxima}, Temperatura menor: {minima}')
print(f'A temperatura média é: {soma}')
