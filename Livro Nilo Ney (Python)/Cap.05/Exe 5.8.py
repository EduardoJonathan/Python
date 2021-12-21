p = int(input("Qual primeiro número: "))
s = int(input("Qual segundo número: "))
x = 1
r = 0
while x <= s:
    r = r + p
    x = x + 1
print(f"{p} x {s} = {r}")
