soma = 0
quantidade = 0
while True:
    n = int(input("Digite um número inteiro: "))
    if n==0:
        break;
    soma = soma + n
    quantidade = quantidade + 1
print(f"Quantidade de números digitados: {quantidade}")
print(f"Soma: {soma}")
print(f"A média é: {soma / quantidade:10.2f}")
