first_number = float(input("Primeiro número: "))
second_number = float(input("Segundo número: "))
operação=input("Digite a operação a realizar (+, -, * ou /):")
if operação == "+":
    resultado = first_number + second_number
elif operação == "-":
    resultado = first_number - second_number
elif operação == "*":
    resultado = first_number * second_number
elif operação == "/":
    resultado = first_number / second_number
else:
    print("Operação inválida!")
    resultado = 0
print(f"Resultado: {resultado}")
