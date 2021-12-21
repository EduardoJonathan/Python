dividendo = int(input("Insira o dividendo:"))
divisor = int(input("Insira o divisor:"))
quociente = 0
x = dividendo
while x >= divisor:
    x = x - divisor
    quociente = quociente + 1
resto = x
print(f"O resto de {dividendo} / {divisor} é {resto}")
