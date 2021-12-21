n0 = int(input('Insira um valor: '))
n1 = int(input('Insira o segundo valor: '))
n2 = int(input('Insira o terceiro valor: '))
maior = n0
menor = n0
if n1 > n0 and n1 > n2:
    maior = n1
if n2 > n0 and n2 > n1:
    maior = n2

if n1 < n2 and n1 < n0:
    menor = n1
if n2 < n1 and n2 < n0:
    menor = n2
print(f'{maior}')
print(f'{menor}')
